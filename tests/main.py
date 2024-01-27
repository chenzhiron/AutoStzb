import time

import numpy as np

from tests.config.config import globalConfig
from tests.devices.device import Devices
from ocr.main import ocrDefault
device = Devices(globalConfig)
area = (1190.0, 280.0, 1262.0, 330.0)
if __name__ == '__main__':
    device.startDevices()
    time.sleep(3)
    img = device.getScreenshots()
    res = ocrDefault(np.array(img))

    # res = ocrDefault(np.array(img.crop(area)))
    print(res)
    device.stop()
