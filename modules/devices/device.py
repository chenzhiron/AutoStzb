import time
import threading
import os 

from adbutils import adb
import uiautomator2 as u2
import numpy as np
from PIL import Image
from io import BytesIO
import requests
from modules.devices.automation import automate

def reg_grb565(data):
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
    return img_array


def send_get_request(url):
    try:
        response = requests.get(url)
        # 检查响应状态码
        if response.status_code == 200:
            data = response.content
            # res reg_grb565(data)
            image_data = BytesIO(data)
            with Image.open(image_data) as img:
                res = img.rotate(-90, expand=True)
                res = np.array(res)
                return res
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
        simulator = config['simulator']
        print('simulator', simulator)
        adb.connect(simulator)
        self.screen_await = config['screen_await']
        # self.screenshots_thread = threading.Thread(target=running_screenshot,args=(simulator,))
        # self.screenshots_thread.setDaemon(True)
        # self.screenshots_thread.start()
        self.d = u2.connect(simulator)
        print(self.d.info)
        # self.url = 'http://127.0.0.1:53516/screenshot?width=1600&height=900'
        self.url = 'http://127.0.0.1:53516/preview?width=1600&height=900'

    def getScreenshots(self):
        time.sleep(self.screen_await)
        imgs = self.d.screenshot()
        res = np.array(imgs)
        return res
        return send_get_request(self.url)
    
    def operateTap(self, x, y):
        self.d.click(x, y)

    def operateSwipe(self, points_list, steps=3):
        for v in points_list:
            x1, y1, x2, y2 = v
            self.d.swipe(x1, y1, x2, y2, steps=steps)
        time.sleep(0.3)
    def operateInput(self, txt):
        self.d.clear_text()
        self.d.send_keys(txt)
    
    def oprtateDrag(self, points_list):
            x1, y1, x2, y2 = points_list
            self.d.drag(x1, y1, x2, y2)
