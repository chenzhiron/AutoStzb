from device.main import return_device
from ocr.main import ocr_txt_verify
from tools.team_direction import chuzheng_direction, zhengbing_direction
from modules.module_duiwu.address_area import discern_area


def module_click_chuzheng_duiwu(i):
    x, y = chuzheng_direction(i)
    device = return_device()
    device.click(x, y)
    return True


def module_click_zhengbing_duiwu(i):
    time_number = 0
    from path.img import path
    while 1:
        if ocr_txt_verify(path, '势力', discern_area):
            x, y = zhengbing_direction(i)
            device = return_device()
            device.click(x, y)
            return True
        else:
            time_number += 1
        if time_number == 50:
            raise Exception("点击队伍，进入征兵页面。执行失败")
