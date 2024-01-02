# 点击方案
from config.const import operate_port, operate_change_port, operate_url
from config.paths import adb
from device.pyminitouch.actions import MNTDevice

device_id = operate_url + ':' + str(operate_port)
Mntdevice = MNTDevice(device_id, adb, operate_change_port, operate_url)


def operateTap(x, y):
    Mntdevice.tap([(x, y)])


def operateSwipe(x1, y1, x2, y2):
    Mntdevice.swipe(
        [(x1, y1), (x2, y2)],
        duration=1000,
        pressure=50
    )

# if __name__ == '__main__':
#     operate_simulator('127.0.0.1:62001')
