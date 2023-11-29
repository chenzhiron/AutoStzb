import sys
import os
import threading
p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'toolkit', 'Lib', 'site-packages')
sys.path.append(lib_p)

from device.AutoMation import automation
from device.operate import init
from web.web import start_web
from config.const import web_port

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

        start_web(web_port)

    except Exception as e:
        print('主线程发生了错误', e)
