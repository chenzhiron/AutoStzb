from device.main import return_device

# 地址参数需要改变
curr_w = 1600 - 170
curr_h = 900 - 855


def module_return_main():
    device = return_device()
    device.click(curr_w, curr_h)
    return True
