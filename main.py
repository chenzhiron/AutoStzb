import sys

import io
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'venv', 'Lib', 'site-packages')
sys.path.append(lib_p)

from communication.comsumer import start_run_websocket_thread
from dispatcher.main import start_scheduler

if __name__ == '__main__':
    start_run_websocket_thread()
    start_scheduler()
    while 1:
        pass

# import subprocess
#
# # 指定exe文件路径
# exe_path = "path/to/your/exe/file.exe"
#
# # 启动exe文件
# subprocess.Popen(exe_path)