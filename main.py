import sys

import os



p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'venv', 'Lib', 'site-packages')
sys.path.append(lib_p)
from modules.tasks.zhengbing import zhengbing
from device.operate import operate_simulator, return_device
from modules.tasks.battle import battle
from ocr.main import ocr_txt_verify

if __name__ == '__main__':
    try:
        operate_url = '127.0.0.1:62001'
        operate_simulator(operate_url)

        # 选择出征队伍页面校验
        result = ocr_txt_verify((0,540,200,600))
        print(result)

        # zhengbing(3)
        # result = battle()
        device = return_device()
        device.stop()
    except Exception as e:
        device = return_device()
        device.stop()

