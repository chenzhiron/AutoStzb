import time

from modules.module_duiwu.module_duiwu import module_click_zhengbing_duiwu
from modules.module_fanhui.module_fanhui import module_return_main
from modules.module_shili.module_shili import module_click_shili
from modules.module_zhengbing.module_zhengbing import module_zhengbing_click, module_swipe_zhengbing_click, \
    module_zhengbing_affirm_btn, module_zhuangbing_time
from path.img import path


def zhengbing(i):
    module_click_shili(path, '势力')
    module_click_zhengbing_duiwu(i)
    module_zhengbing_click()
    module_swipe_zhengbing_click()
    module_zhengbing_affirm_btn('确认证兵')
    module_zhuangbing_time()
    time.sleep(1)
    module_return_main()
    time.sleep(1)
    module_return_main()
