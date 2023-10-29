from device.operate import operate_adb_tap
from modules.general.generalExecuteFn import reg_ocr_verify, executeFn, executeClickArea
from modules.general.module_options_name import shili
from modules.module_shili.address_area import shili_area, shili_click


def module_click_shili():
    executeFn(
        reg_ocr_verify(shili_area, 2),
        shili
    )
    x, y = executeClickArea(shili_area)
    operate_adb_tap(x, y)
