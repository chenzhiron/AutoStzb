from ocr.ocr_model_name import vertical_model_name
from tools.reg_screenshot import general_screenshot_tools
from task.modules_start.module_start_area import start_area
from ocr.main import ocr_txt_click


def module_click_start(path, auto_text):
    general_screenshot_tools(start_area)
    return ocr_txt_click(path, auto_text, model=vertical_model_name)
