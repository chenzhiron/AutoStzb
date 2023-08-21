from device.main import connect_device

from tools.reg_screenshot import general_screenshot_tools
from maps.map_area import base_area
from path.img import path
from ocr.main import ocr_default

if __name__ == '__main__':
    d = connect_device()
    general_screenshot_tools(base_area)
    result = ocr_default(path)
    print(result)