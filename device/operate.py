from utils.pyminitouch_seo.actions import MNTDevice

device = None


def operate_simulator(device_id, host):
    global device
    device = MNTDevice(device_id, host)


def return_device():
    global device
    return device


def operate_adb_tap(x, y):
    device.tap([(x, y)], pressure=100)


def operate_adb_swipe(x1, y1, x2, y2):
    device.swipe(
        [(x1, y1, x2, y2)],
        duration=500,
        pressure=50
    )
    # device.stop()

# if __name__ == '__main__':
#     operate_simulator('127.0.0.1:62001')
