import time
import threading
import os 

import uiautomator2 as u2
import numpy as np
import requests
from modules.devices.automation import automate

adbpath = os.path.join(os.getcwd(), 'toolkit', 'adb')
os.environ['PATH'] += adbpath

def send_get_request(url):
    try:
        start_time = time.time()
        # 发送GET请求
        response = requests.get(url)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.content
            img_array = np.frombuffer(data, dtype=np.uint16)
            # 将RGB_565转换为8位的RGB三通道
            # 注意：你可能需要根据实际情况调整掩码和位移
            r5 = ((img_array & 0xF800) >> 11).astype(np.uint8)
            g6 = ((img_array & 0x07E0) >> 5).astype(np.uint8)
            b5 = (img_array & 0x001F).astype(np.uint8)

            # 将5位或6位通道转换为8位通道
            r8 = ((r5 * 255.0) / 31.0).astype(np.uint8)
            g8 = ((g6 * 255.0) / 63.0).astype(np.uint8)
            b8 = ((b5 * 255.0) / 31.0).astype(np.uint8)
            # 组装为8位RGB图像的三通道数据
            img_array = np.stack((r8, g8, b8), axis=-1)
            # 重塑数组以匹配图像的宽度和高度
            img_array = img_array.reshape(900, 1600, 3)
            
            print("请求成功，响应时间：", time.time() - start_time)
            return img_array
        else:
            print("请求失败，状态码：", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("请求发生异常:", e)
        return None

def running_screenshot(simulator):
    automate(simulator)

class Devices:
    def __init__(self, config) -> None:
        simulator = config['Simulator']['url']
        print('simulator', simulator)
        self.screenshots_thread = threading.Thread(target=running_screenshot,args=(simulator,))
        self.screenshots_thread.setDaemon(True)
        self.screenshots_thread.start()
        self.d = u2.connect(simulator)
        print(self.d.info)
        time.sleep(3)
        self.url = 'http://127.0.0.1:53516/screenshot?width=1600&height=900'

    def getScreenshots(self):
        return send_get_request(self.url)
    
    def operateTap(self, x, y):
        self.d.click(x, y)

    def operateSwipe(self, points_list):
        for v in points_list:
            x1, y1, x2, y2 = v
            self.d.swipe(x1, y1, x2, y2, steps=3)
        time.sleep(0.5)
    def operateInput(self, txt):
        self.d.clear_text()
        self.d.send_keys(txt)
