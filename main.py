import sys
import os

p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'venv', 'Lib', 'site-packages')
sys.path.append(lib_p)
from device.main_device import connect_device
from tasks.zhengbing.main import zhengbing

arguments = sys.argv
print('参数', arguments)

args = arguments[1:]

if __name__ == '__main__':
    d = connect_device()

    if int(args[0]) == 0:
        pass
    elif int(args[0]) == 1:
            zhengbing(int(args[1]))
    # chuzheng('出证', 4)
    # d.screenshot().save(path)
    print('end')
