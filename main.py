import sys

import os
import threading
p = os.getcwd()
# parent_dir = os.path.dirname(p)
# sys.path.append(parent_dir)
sys.path.append(p)
lib_p = os.path.join(p, 'toolkit', 'Lib', 'site-packages')
sys.path.append(lib_p)

from device.operate import operate_simulator, disconnect_simulator
from device.automation import automate
from config.const import operate_url, operate_port
from web.main import start_web

if __name__ == '__main__':
    try:
        # 模拟器截图方案
        operate2 = threading.Thread(target=automate)
        operate2.setDaemon(True)
        operate2.start()

        # 模拟器点击方案
        operate = threading.Thread(target=operate_simulator(operate_url + ':' + str(operate_port)))
        operate.setDaemon(True)
        operate.start()
        # handle_in_map_conscription(1)
        start_web()
        disconnect_simulator()
    except Exception as e:
        print('发生了错误', e)
        disconnect_simulator()
