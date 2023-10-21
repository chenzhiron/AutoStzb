import sys

import os
import time

from web.main import start_web

p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'venv', 'Lib', 'site-packages')
sys.path.append(lib_p)

import threading
from device.main import automate
from device.operate import operate_simulator, return_device


# from modules.tasks.zhengbing import zhengbing
# from modules.tasks.battle import battle
# from ocr.main import ocr_txt_verify


# 点击方案
def start_simulator():
    operate_url = '127.0.0.1:62001'
    operate_simulator(operate_url)


def work_adb():
    automate()


# 选择出征队伍页面校验
# result = ocr_txt_verify((0, 540, 200, 600))
# print(result)

# zhengbing(3)
# result = battle()


if __name__ == '__main__':
    try:
        # 模拟器截图方案
        operate2 = threading.Thread(target=work_adb)
        operate2.setDaemon(True)
        operate2.start()

        # 模拟器点击方案
        operate = threading.Thread(target=start_simulator)
        operate.setDaemon(True)
        operate.start()

        start_web()
        # operate = threading.Thread(target=start_web)
        # operate.setDaemon(True)
        # operate.start()

        device = return_device()
        if device is not None:
            device.stop()
    except Exception as e:
        print(e)
        device = return_device()
        if device is not None:
            device.stop()
