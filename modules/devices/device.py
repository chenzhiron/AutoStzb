import time

import uiautomator2 as u2
from adbutils import adb
from PIL import Image
import io
import requests
import subprocess
import os 

adbpath = os.path.join(os.getcwd(), 'toolkit', 'adb')
os.environ['PATH'] += adbpath
command = 'adb.exe shell CLASSPATH=/data/local/tmp/DroidCast_raw-release-1.1.apk app_process /system/bin ink.mol/droidcast_raw.Main --port=53516'
def subprocess_run(command):
    # 使用 subprocess.run() 执行命令，并捕获其输出和状态
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL)
    return result

def send_get_request(url):
    try:
        # 发送GET请求
        response = requests.get(url)
        # 检查响应状态码
        if response.status_code == 200:
            # 返回响应内容
            return Image.open(io.BytesIO(response.content)) 
        else:
            print("请求失败，状态码：", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("请求发生异常:", e)
        return None


screenshots_prop = subprocess_run(command)
class Devices:
    def __init__(self, config) -> None:
        simulator = config['Simulator']['url']
        print('simulator', simulator)
        self.d = u2.connect(simulator)
        print(self.d.info)
        adb.device(simulator).forward('tcp:53516', 'tcp:53516')
        self.url = 'http://127.0.0.1:53516/preview'

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
