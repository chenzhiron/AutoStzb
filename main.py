import sys
import os
import threading
import time

p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'toolkit', 'Lib', 'site-packages')
sys.path.append(lib_p)




from device.AutoMation import automation
from device.operate import Mntdevice, init
from modules.taskGroup import handle_in_draw_battle, handle_in_unmark, handle_out_home
from modules.tasks import Task
# from web.main import start_web

if __name__ == '__main__':
    try:
        # 模拟器截图方案
        operate2 = threading.Thread(target=automation.automate)
        operate2.setDaemon(True)
        operate2.start()
        # 模拟器点击方案
        operate = threading.Thread(target=init)
        operate.setDaemon(True)
        operate.start()
        time.sleep(3)
        task1 = Task(2, 0)
        task1.change_config_storage_by_key('lists', 1)
        task1.change_config_storage_by_key('txt', '出证')
        task1.change_config_storage_by_key('offset', 40)
        task1.next_start()

        while 1:
            pass
        # start_web()
        # handle_in_draw_battle()
    except Exception as e:
        print('主线程发生了错误', e)
