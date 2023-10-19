# http 截图方案
import time

import requests

import numpy as np
from PIL import Image
from io import BytesIO

from device.automation3 import connect_device

from device.operate import operate_simulator, operate_adb_swipe, operate_adb_tap

url = 'http://127.0.0.1:53515/screenshot'


def start_adb():
    connect_device()


adb_connection = None


def get_screenshot(area):
    response = requests.get(url)
    if response.status_code == 200:
        image = (Image.open(BytesIO(response.content))).crop(area)
        return np.array(image)
    else:
        print('截图失败')
        return None


def adb_tap(x, y):
    start = time.time()
    operate_adb_tap(x, y)
    end = time.time()
    print(end - start)


def adb_swipe(x1, y1, x2, y2):
    operate_adb_swipe(x1, y1, x2, y2)
