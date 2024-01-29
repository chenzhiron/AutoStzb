import numpy as np


from tests.config.config import globalConfig
from tests.devices.device import Devices
from ocr.main import ocrDefault

device = Devices(globalConfig)
area = (444, 628, 462, 660)
if __name__ == '__main__':
    try:
        device.startDevices()
        device.operateTap(200, 340)
        # img = device.getScreenshots()
        # # res = ocrDefault(np.array(img))
        # ress = img.crop(area)
        # ress.save('1.png')
        # res = ocrDefault(np.array(ress))
        # print(res)
        # device.closeDevice()
    except:
        device.closeDevice()

