from adbutils import adb

device = 0


def connect_device():
    global device
    device = adb.device()
    return device


def return_device():
    global device
    return device
