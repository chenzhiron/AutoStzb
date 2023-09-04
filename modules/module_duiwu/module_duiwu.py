from device.main_device import return_device
from modules.module_duiwu.address_area import discern_area
from ocr.main import ocr_txt_verify
from tools.team_direction import chuzheng_direction, zhengbing_direction


def module_click_chuzheng_duiwu(i):
    x, y = chuzheng_direction(i)
    device = return_device()
    device.click(x, y)
    return True


def module_click_zhengbing_duiwu(i):
    time_number = 50
    device = return_device()
    from config.img import path
    while time_number > 0:
        if ocr_txt_verify(path, '势力', discern_area):
            x, y = zhengbing_direction(i)
            device.click(x, y)
            return True
        else:
            time_number -= 1
    if time_number <= 0:
        raise Exception("点击队伍，进入征兵页面。执行失败")


# if __name__ == '__main__':
#     connect_device()
#     module_click_zhengbing_duiwu(5)
    # module_click_chuzheng_duiwu(5)