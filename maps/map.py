from maps.reg_img.main import convert_to_grayscale
from device.main import connect_device
from path.img import path


def reg_map(path):
    convert_to_grayscale(path)


if __name__ == '__main__':
    device = connect_device()
    device.screenshot().save(path)
    reg_map(path)
