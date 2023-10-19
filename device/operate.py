from pyminitouch import MNTDevice

device = None


def operate_simulator(device_id):
    global device
    device = MNTDevice(device_id)


def operate_adb_tap(x, y):
    # single-tap
    device.tap([(x, y)], pressure=100)
    device.stop()


def operate_adb_swipe(x1, y1, x2, y2):
    device.swipe(
        [(x1, y1), (x2, y2)],
        duration=500,
        pressure=50,
        no_down=True,
        no_up=True,
    )
    device.stop()

# if __name__ == '__main__':
#     operate_simulator('127.0.0.1:62001')
