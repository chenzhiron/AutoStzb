# 点击方案
from device.pyminitouch_seo.actions import MNTDevice

device = None


def operate_simulator(device_id):
    global device
    device = MNTDevice(device_id)


def disconnect_simulator():
    if device:
        device.stop()


def operate_adb_tap(x, y):
    device.tap([(x, y)], pressure=100)


def operate_adb_swipe(x1, y1, x2, y2):
    device.swipe(
        [(x1, y1), (x2, y2)],
        duration=1000,
        pressure=50
    )

# if __name__ == '__main__':
#     operate_simulator('127.0.0.1:62001')
