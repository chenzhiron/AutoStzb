from device.main import connect_device
from modules.module_going.module_going import chuzheng
from tasks.zhengbing.main import zhengbing
max = 0
status = False
if __name__ == '__main__':
    d = connect_device()
    zhengbing(4)
    # chuzheng('出证', 3)
    # d.screenshot().save(path)
    # 开始游戏
    # module_click_start(path, '开始游戏')
    # 点击势力
    # module_click_shili(path, '势力')
    # 主城队伍点击数
    # module_click_zhengbing_duiwu(4)
    # 出征页面点击队伍数
    # module_click_chuzheng_duiwu(1)
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
    # module_zhuangbing_time()
    print('end')
