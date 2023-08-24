from device.main_device import return_device


curr_w = 1600 - 80
curr_h = 900 - 800

main_w = 1600 - 70
main_h = 900 - 850


def module_return_main():
    device = return_device()
    device.click(curr_w, curr_h)
    return True


def module_return_index():
    device = return_device()
    device.click(main_w, main_h)
    return True