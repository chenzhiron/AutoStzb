import sys

import os


p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'venv', 'Lib', 'site-packages')
sys.path.append(lib_p)

# from web.main import start_web
import threading
from device.operate import operate_simulator, disconnect_simulator
from device.automation import automate
from config.const import operate_url, operate_port

# from modules.tasks.zhengbing import zhengbing
# from modules.tasks.battle import battle
# from ocr.main import ocr_txt_verify
# from modules.tasks.saodang import saodang
from modules.pageSwitch.page_switch import handle_in_map_conscription

if __name__ == '__main__':
    try:
        # 模拟器截图方案
        operate2 = threading.Thread(target=automate)
        operate2.setDaemon(True)
        operate2.start()

        # 模拟器点击方案
        operate = threading.Thread(target=operate_simulator(operate_url+':'+str(operate_port)))
        operate.setDaemon(True)
        operate.start()
        # time.sleep(20)
        handle_in_map_conscription(1)
        # start_web()
        disconnect_simulator()
    except Exception as e:
        print('发生了错误', e)
        disconnect_simulator()
