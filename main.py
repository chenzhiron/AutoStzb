import sys

import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'venv', 'Lib', 'site-packages')
sys.path.append(lib_p)

from ocr.main import ocr_default
from config.paths import path

# from dispatcher.main import start_scheduler

if __name__ == '__main__':
    result = ocr_default(path)
    print(result)
    # start_scheduler()
    # while 1:
    #     pass

# import subprocess
#
# # 指定exe文件路径
# exe_path = "path/to/your/exe/file.exe"
#
# # 启动exe文件
# subprocess.Popen(exe_path)
