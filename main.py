import sys

import os

p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'venv', 'Lib', 'site-packages')
sys.path.append(lib_p)
from modules.tasks.zhengbing import zhengbing
from device.operate import operate_simulator, return_device

if __name__ == '__main__':
    try:
        operate_url = '127.0.0.1:62001'
        operate_simulator(operate_url, '127.0.0.1')
        # adb_tap(555,555)
        zhengbing(3)
        device = return_device()
        device.stop()
        # start = time.time()
        # module_click_shili()
        # end = time.time()
        # print(end - start)
    except Exception as e:
        device = return_device()
        device.stop()

