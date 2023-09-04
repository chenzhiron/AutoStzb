import time

from config.img import path
from modules.module_duiwu.module_duiwu import module_click_zhengbing_duiwu
from modules.module_fanhui.module_fanhui import module_return_main, module_return_index
from modules.module_shili.module_shili import module_click_shili
from modules.module_zhengbing.module_zhengbing import module_zhengbing_click, module_swipe_zhengbing_click, \
    module_zhengbing_affirm_btn, module_zhengbing_computed_time, module_zhuangbing_require


def zhengbing(i):
    module_click_shili(path)
    module_click_zhengbing_duiwu(i)
    module_zhengbing_click(path)
    module_swipe_zhengbing_click(path)
    maxtime = module_zhengbing_computed_time(path)
    module_zhengbing_affirm_btn()
    module_zhuangbing_require(path)
    time.sleep(1)
    module_return_main()
    time.sleep(1)
    module_return_main()
    time.sleep(1)
    module_return_index()
    return maxtime[0]
