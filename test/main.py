import time

import numpy as np

from test.config.config import globalConfig
from test.devices.device import Devices
from ocr.main import ocrDefault
device = Devices(globalConfig)
area = (1263.0, 806.0, 1400.0, 835.0)
if __name__ == '__main__':
    device.startDevices()
    time.sleep(3)
    img = device.getScreenshots()
    # res = ocrDefault(np.array(img))

    res = ocrDefault(np.array(img.crop(area)))
    print(res)
    device.stop()
