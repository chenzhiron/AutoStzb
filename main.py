import sys
import os
import threading
import time

p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'toolkit', 'Lib', 'site-packages')
sys.path.append(lib_p)


from device.operate import operate_simulator, disconnect_simulator
from device.automation import automate
from config.const import operate_url, operate_port, web_port
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

        time.sleep(2)
        main_process_id = os.getpid()
        print(main_process_id)
        start_web()
        disconnect_simulator()
    except Exception as e:
        print('主线程发生了错误', e)
        disconnect_simulator()
