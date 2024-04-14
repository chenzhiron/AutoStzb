from config.config import globalConfig
from modules.devices.device import Devices

from modules.task.setups import *
from modules.task.steps import *

device = Devices(globalConfig)

if __name__ == '__main__':
    ress = device.getScreenshots()
    left, top, right, bottom = (985,400,1540,812)
    resss = ocrDefault(ress[top:bottom, left:right])
    print(resss)
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
