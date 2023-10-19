# http 截图方案
import time

import requests

import numpy as np
from PIL import Image
from io import BytesIO

from device.automation3 import connect_device, return_url, return_device
from config.paths import adb
import subprocess

url = 'http://127.0.0.1:53515/screenshot'


def start_adb():
    connect_device()
    # global url
    # url = return_url()


def device():
    return return_device()


adb_connection = None


def get_screenshot(area):
    response = requests.get(url)
    if response.status_code == 200:
        image = (Image.open(BytesIO(response.content))).crop(area)
        return np.array(image)
    else:
        print('截图失败')
        return None


def get_adb_connection():
    global adb_connection
    if adb_connection is None:
        adb_connection = subprocess.Popen([adb, 'devices'], stdout=subprocess.PIPE)
    return adb_connection


def execute_adb_shell_command(cmd, ip='127.0.0.1', port=53515):
    connection = get_adb_connection()
    process = subprocess.Popen(
        [adb, '-s', f'{ip}:{port}', 'shell', cmd],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()


def adb_tap(x, y):
    start = time.time()
    execute_adb_shell_command(f'input tap {x} {y}')
    end = time.time()
    print(end - start)


def adb_swipe(x1, y1, x2, y2, duration=250):
    execute_adb_shell_command(f'input swipe {x1} {y1} {x2} {y2} {duration}')
