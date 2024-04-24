# from config.config import globalConfig
# from modules.devices.device import Devices

# from modules.task.setups import *
# from modules.task.steps import *
from PIL import Image
import numpy as np
# device = Devices(globalConfig)
# from modules.utils.utils import img_bytes_like
from modules.ocr.main import ocrDefault
# address_execute_list = [
#     [(800, 720)],
#     [(675, 720), (938, 720)],
#     [(575, 720), (800, 720), (1050, 720)],
#     [(480, 720), (720, 720), (930, 720), (1160, 720)],
#     [(380, 720), (600, 720), (820, 720), (1040, 720), (1260, 720)]
# ]
# img = Image.open('./2.jpg').crop((260,190,900, 620))

if __name__ == '__main__':
    ress = ocrDefault('./3.png')
    for v in ress[0]:
        print(v)
    # print(ress)
    # res = PingJuChetui(device, {}).run()
    # print(res)
    # res = ZhengBing(device, {
    #     "x": "684",
    #     "y":"738"
    # }).run()
    # res = ZhanBao(device, {
    #     "x": "684",
    #     "y":"738"
    # }).run()
    # res = ChuZheng(device, {
    #     'x': "685",
    #     "y": "737"
    # }).run()
    # print(res)
