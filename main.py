from device.main import connect_device
from path.img import path
from task.modules_start.module_start import module_click_start
from task.module_shili.module_shili import module_click_shili
from task.module_duiwu.module_duiwu import module_ocr_duiwu_name
if __name__ == '__main__':
    d = connect_device()
    # module_click_start(path, '开始游戏')
    # module_click_shili(path, '势力')
    result = module_ocr_duiwu_name(d, path,True)
    print(result)
