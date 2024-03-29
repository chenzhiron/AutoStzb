from config.config import globalConfig
from modules.devices.device import Devices

from modules.task.setups import click_zhengbing_require
from modules.task.steps import ZhengBing

device = Devices(globalConfig)

if __name__ == '__main__':
    # res = device.getScreenshots()
    res333 = ZhengBing(device, {}).run()

    # click_zhengbing_require.verifyOcr(res)
    # res = click_zhengbing_require.verifyTxt()
    print('ocr promise', res333)
    device.ws.close()
