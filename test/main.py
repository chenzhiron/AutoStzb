import time

import numpy as np

from test.config.config import globalConfig
from test.devices.device import Devices
from ocr.main import ocrDefault
device = Devices(globalConfig)
if __name__ == '__main__':
    device.startDevices()
    time.sleep(3)
    device.operateTap(410, 800)
    for v in range(10):
        img = device.getScreenshots()
        res = ocrDefault(np.array(img))
        print(res)
    device.stop()
