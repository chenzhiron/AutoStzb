import sys
import os
# 获取当前脚本所在目录的绝对路径
script_path = os.path.abspath(os.path.dirname(__file__))

# 添加脚本所在目录到模块搜索路径
sys.path.append(script_path)

script_dir = os.path.dirname(os.path.abspath(__file__))

# adb命令的相对路径（注意双反斜杠用于转义）
adb_relative_path = os.path.join('toolkit', 'adb', 'adb.exe')

# 构建完整的adb命令路径
adb_path = os.path.join(script_dir, adb_relative_path)

# 设置环境变量，将adb命令所在目录添加到PATH中
os.environ['PATH'] = f"{adb_path};{os.environ['PATH']}"
print(os.environ['PATH'])

from st import stzb
from modules.web.web import start_web
import threading
if __name__ == '__main__':
    # try:
        new_thread = threading.Thread(target=start_web)
        new_thread.setDaemon(True)
        new_thread.start()
        # threading.Timer(3, lambda: webbrowser.open('http://127.0.0.1:9091')).start()
        stzb.loop()
        
    # except Exception as e:
    #     print(e)
