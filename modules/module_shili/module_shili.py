from device.main import adb_tap
from modules.general.generalExecuteFn import reg_ocr_verify, executeFn, executeClickArea
from modules.general.module_options_name import shili
from modules.module_shili.address_area import shili_area


def module_click_shili():
    result = executeFn(
        reg_ocr_verify(shili_area, 2),
        shili
    )
    if result:
        adb_tap(340, 600)
