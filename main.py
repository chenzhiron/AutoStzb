from device.main import connect_device
from path.img import path
from task.modules_start.module_start import module_click_start
from task.module_shili.module_shili import module_click_shili
from task.module_duiwu.module_duiwu import (
    module_click_chuzheng_duiwu,
    module_click_zhengbing_duiwu,
    module_reg_zhengbing_page,
)
from task.module_fanhui.module_fanhui import module_return_main
from task.module_zhengbing.module_zhengbing import module_zhengbing_click
from task.module_zhengbing.module_zhengbing import module_swipe_zhengbing_click, module_zhengbing_affirm_btn, module_zhuangbing_time

max = 0
status = False
if __name__ == '__main__':
    d = connect_device()
    # 开始游戏
    # module_click_start(path, '开始游戏')
    # 点击势力
    # module_click_shili(path, '势力')
    # 主城队伍点击数
    # module_click_zhengbing_duiwu(4)
    # 出征页面点击队伍数
    # module_click_chuzheng_duiwu(4)
    # 返回上一个页面
    # module_return_main()
    # module_return_main()
    # 队伍页面点击征兵按钮
    # module_zhengbing_click()

    # while 1:
    #     if module_click_shili(d, path, '势力'):
    #         while 1:
    #             if module_reg_zhengbing_page(path):
    #                 module_click_zhengbing_duiwu(d, 1)
    #                 while 1:
    #                     module_zhengbing_click()
    #                     status = True
    #                     break
    #             else:
    #                 max += 1
    #                 print(max)
    #                 if max == 50:
    #                     break
    #             if status:
    #                 break
    #     else:
    #         if status:
    #             break
    #         module_return_main(d)
    #         break

    # 队伍页面拖动征兵滚动条
    # module_swipe_zhengbing_click()

    #确认征兵
    # module_zhengbing_affirm_btn('确认证兵')

    # 队伍征兵时间计算
    module_zhuangbing_time()
    print('end')
