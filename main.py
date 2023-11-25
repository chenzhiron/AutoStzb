import sys
import os
import threading


p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'toolkit', 'Lib', 'site-packages')
sys.path.append(lib_p)

# from modules.taskGroup import handle_in_draw_battle
from device.AutoMation import automation
from device.operate import Mntdevice
# from web.main import start_web

if __name__ == '__main__':
    try:
        # 模拟器截图方案
        operate2 = threading.Thread(target=automation.automate)
        operate2.setDaemon(True)
        operate2.start()

        while 1:
            pass
        # start_web()
        # handle_in_draw_battle()
    except Exception as e:
        # automation.disconnect()
        Mntdevice.stop()
        print('主线程发生了错误', e)
        # disconnect_simulator()
