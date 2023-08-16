from device.main import connect_device
from path.img import path
from task.modules_start.module_start import module_click_start
from task.module_shili.module_shili import module_click_shili
from task.module_duiwu.module_duiwu import module_ocr_duiwu_name,module_click_duiwu
if __name__ == '__main__':
    d = connect_device()
    # d.screenshot().save(path)
    # module_click_start(d, path, '开始游戏', 'ch_PP-OCRv3')
    # module_click_shili(d,path, '势力')
    # result = module_ocr_duiwu_name(d, path,True)
    # print(result)
