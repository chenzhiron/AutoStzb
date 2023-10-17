from adbutils import adb

device = 0


def connect_device():
    global device
    device = adb.device('127.0.0.1:62001')
    return device


def return_device():
    global device
    return device
