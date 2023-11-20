# 点击方案
from device.pyminitouch.actions import MNTDevice
from config.paths import adb
from config.const import operate_url, operate_port, operate_change_port

device_id = operate_url + ':' + str(operate_port)

Mntdevice = MNTDevice(device_id, adb, operate_change_port)


def operate_adb_tap(x, y):
    Mntdevice.tap([(x, y)])


def operate_adb_swipe(x1, y1, x2, y2):
    Mntdevice.swipe(
        [(x1, y1), (x2, y2)],
        duration=1000,
        pressure=50
    )

# if __name__ == '__main__':
#     operate_simulator('127.0.0.1:62001')
