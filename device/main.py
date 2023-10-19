# http 截图方案
import requests

import numpy as np
from PIL import Image
from io import BytesIO

from device.automation3 import connect_device, return_url, return_device
from config.paths import adb
import subprocess

url = 'http://127.0.0.1:53516/screenshot'


def start_adb():
    connect_device()
    # global url
    # url = return_url()


def device():
    return return_device()


def get_screenshot(area):
    response = requests.get(url)
    if response.status_code == 200:
        image = (Image.open(BytesIO(response.content))).crop(area)
        return np.array(image)
    else:
        print('截图失败')
        return None


def execute_adb_shell_command(cmd):
    subprocess.run([adb, 'shell', cmd])


def adb_tap(x, y):
    execute_adb_shell_command(f'input tap {x} {y}')


def adb_swipe(x1, y1, x2, y2, duration=250):
    execute_adb_shell_command(f'input swipe {x1} {y1} {x2} {y2} {duration}')
