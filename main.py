from device.main import connect_device
from path.img import path
from task.modules_start.module_start import module_click_start
from task.module_shili.module_shili import module_click_shili
from task.module_duiwu.module_duiwu import (module_ocr_duiwu_name,
                                            module_click_duiwu,
                                            module_click_chuzheng_duiwu,
                                            module_click_zhengbing_duiwu,
                                            module_reg_zhengbing_page)
from task.module_fanhui.module_fanhui import module_return_main
from task.module_zhengbing.module_zhengbing import module_zhengbing_click

max = 0
status = False
if __name__ == '__main__':
    d = connect_device()
    # d.screenshot().save(path)
    # module_click_start(d, path, '开始游戏', 'ch_PP-OCRv3')
    # result = module_ocr_duiwu_name(d, path,True)
    # print(result)
    # module_click_chuzheng_duiwu(d, 4)
    # module_return_main(d)
    # module_return_main(d)
    while 1:
        if module_click_shili(d, path, '势力'):
            while 1:
                if module_reg_zhengbing_page(path):
                    module_click_zhengbing_duiwu(d, 1)
                    while 1:
                        module_zhengbing_click(d)
                        status = True
                        break
                else:
                    max += 1
                    print(max)
                    if max == 50:
                        break
                if status:
                    break
        else:
            if status:
                break
            module_return_main(d)
            break
    print('end')
