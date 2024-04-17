import sys
import os
# 获取当前脚本所在目录的绝对路径
script_path = os.path.abspath(os.path.dirname(__file__))

# 添加脚本所在目录到模块搜索路径
sys.path.append(script_path)

from st import stzb
from modules.web.web import start_web
import threading
import webbrowser
if __name__ == '__main__':
    # try:
        new_thread = threading.Thread(target=start_web)
        new_thread.setDaemon(True)
        new_thread.start()
        threading.Timer(3, lambda: webbrowser.open('http://127.0.0.1:9091')).start()
        stzb.loop()
        
    # except Exception as e:
    #     print(e)
