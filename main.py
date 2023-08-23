from device.main import connect_device
from modules.modules_start.module_start import module_click_start
from tasks.zhengbing.main import zhengbing
from path.img import path

status = False
if __name__ == '__main__':
    d = connect_device()
    zhengbing(5)
    # chuzheng('出证', 3)
    # d.screenshot().save(path)

    print('end')

