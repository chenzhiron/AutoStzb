from tests.config.config import globalConfig
from tests.devices.device import Devices

device = Devices(globalConfig)
if __name__ == '__main__':
    print(device.getScreenshots())
    # data = device.getScreenshots()
    # print(data)
