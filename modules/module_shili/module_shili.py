from device.main_device import return_device
from modules.general.generalExecuteFn import reg_ocr_verify, executeFn, executeClickArea
from modules.general.module_options_name import shili
from modules.module_shili.address_area import shili_area


def module_click_shili():
    device = return_device()
    result = executeFn(
        reg_ocr_verify(shili_area, 2),
        shili
    )
    if result:
        device.click(340, 600)
    return True
