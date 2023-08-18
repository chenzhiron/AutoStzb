from tools.reg_coordinates import reg_coor
from device.main import return_device


def reg_list_name(list_name):
    name = []
    for v in list_name:
        name.append(v['text'])
    return name


def group_txt_click(list_txt, auto_txt):
    name = ''
    for v in list_txt:
        name += v['text']
    if auto_txt == name:
        d = return_device()
        res = reg_coor(list_txt[0]['position'])
        d.click(res[0], res[1])
        return True
    else:
        return False
