from device.main_device import return_device
from modules.module_fanhui.module_fanghui_area import curr_w, curr_h, main_w, main_h


def module_return_main():
    device = return_device()
    device.click(curr_w, curr_h)
    return True


def module_return_index():
    device = return_device()
    device.click(main_w, main_h)
    return True
