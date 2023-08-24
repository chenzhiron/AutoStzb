from device.main_device import connect_device


if __name__ == '__main__':
    d = connect_device()
    d.swipe(500,500, 500,100)