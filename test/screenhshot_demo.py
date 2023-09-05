from config.img import path
from device.main_device import connect_device

if __name__ == '__main__':
    device = connect_device()
    device.screenshot().save(path)
