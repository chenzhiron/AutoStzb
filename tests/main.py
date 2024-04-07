from config.config import globalConfig
from modules.devices.device import Devices

from modules.task.setups import *
from modules.task.steps import *

device = Devices(globalConfig)

if __name__ == '__main__':
    res = PingJuChetui(device, {}).run()
    print(res)
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
