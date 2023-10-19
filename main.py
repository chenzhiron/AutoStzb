import sys

import os
import time

p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'venv', 'Lib', 'site-packages')
sys.path.append(lib_p)
from modules.module_shili.module_shili import module_click_shili

if __name__ == '__main__':
    start = time.time()
    module_click_shili()
    end = time.time()
    print(end - start)
