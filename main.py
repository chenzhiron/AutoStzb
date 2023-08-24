import sys
import os


p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'venv', 'Lib', 'site-packages')
sys.path.append(lib_p)

arguments = sys.argv
print('参数', arguments)


from device.main_device import connect_device
from tasks.zhengbing.main import zhengbing

if __name__ == '__main__':
    d = connect_device()
    # zhengbing(4)
    # chuzheng('出证', 4)
    # d.screenshot().save(path)
    print('end')
