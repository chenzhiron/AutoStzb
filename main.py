import sys

import os
import time

from device.main import adb_tap

p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'venv', 'Lib', 'site-packages')
sys.path.append(lib_p)
from modules.module_shili.module_shili import module_click_shili
from tasks.zhengbing import zhengbing

if __name__ == '__main__':
    # adb_tap(555,555)
    zhengbing(3)
    # start = time.time()
    # module_click_shili()
    # end = time.time()
    # print(end - start)
