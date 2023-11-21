from modules.Class.OperatorSteps import ClickOperatorSteps
from modules.general.module_options_name import zhaomu, shili, zhengbing, queding, biaoji, person_battle, retreat_name, \
    battle_site_name
from modules.general.option_verify_area import zhaomu_area, shili_click, zhengbing_page_verify_area, click_list_x_y, \
    zhengbing_click, zhengbing_page_swipe_sure, queding_area, zhengbing_page_area, address_going_require, \
    address_sign_verify, address_sign_area, address_sign_land_area, click_draw_area, click_draw_detail_area, \
    person_battle_area, battle_site, retreat_discern_require_area, \
    retreat_discern_require_area_xy, retreat_require_click, retreat_append_click, retreat_append_click_xy, cancel_sign, \
    address_area_start


# 点击势力
click_shili = ClickOperatorSteps(zhaomu_area, [zhaomu], shili_click[0], shili_click[1])
# 点击部队
click_budui = ClickOperatorSteps(zhengbing_page_verify_area, [shili], click_list_x_y[0], click_list_x_y[1])
# 点击征兵
click_zhengbing = ClickOperatorSteps(zhengbing_page_area, [zhengbing], zhengbing_click[0], zhengbing_click[1])

# 点击确认征兵，在此处是同一个页面 不需要校验
click_zhengbing_sure = ClickOperatorSteps(0, None, zhengbing_page_swipe_sure[0], zhengbing_page_swipe_sure[1])
# 征兵确认
click_zhengbing_require = ClickOperatorSteps(queding_area, [queding], queding_area[0], queding_area[1])

# 回到主页模块
# click_out_map = ClickOperatorSteps(0, None, 0, 0)

# 点击出征/ 扫荡  在此处是同一个页面 不需要校验
click_chuzheng_or_saodang = ClickOperatorSteps(0, None, address_going_require[0], address_going_require[1])

# 如果没有点击标记，则点击一次
click_sign_init = ClickOperatorSteps(0, None, address_area_start[0], address_area_start[1])

# 点击标记
click_sign = ClickOperatorSteps(address_sign_verify, [biaoji], address_sign_area[0], address_sign_area[1])

# 点击标记下方土地
click_sign_options = ClickOperatorSteps(0, None, address_sign_land_area[0], address_sign_land_area[1])

# 点击战报
click_battle = ClickOperatorSteps(zhaomu_area, ['招募'], click_draw_area[0], click_draw_area[1])

# 查看个人详情
click_battle_main = ClickOperatorSteps(person_battle_area, [person_battle], click_draw_detail_area[0],
                                       click_draw_detail_area[1])

# 战报内部点击战斗地点
click_battle_retreat = ClickOperatorSteps(battle_site, [battle_site_name], battle_site[0], battle_site[1])

# 重复确认
click_battle_require = ClickOperatorSteps(retreat_discern_require_area, [queding], retreat_discern_require_area_xy[0],
                                          retreat_discern_require_area_xy[1])
# 点击平局队伍
click_battle_lists = ClickOperatorSteps(0, None, retreat_require_click[0], retreat_require_click[1])
# 点击撤退按钮
click_battle_retreat_append = ClickOperatorSteps(retreat_append_click, [retreat_name], retreat_append_click_xy[0],
                                                 retreat_append_click_xy[1])

# 取消标记
click_unmark = ClickOperatorSteps(0, None, cancel_sign[0], cancel_sign[1])
