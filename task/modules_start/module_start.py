from ocr.main import ocr_txt_click

def module_click_start(device, path, auto_text):
    device.screenshot().save(path)
    return ocr_txt_click(path, auto_text)
