from device.operate import operateTap
from modules.task.Class.OperatorSteps import ClickOperatorSteps
from modules.general.module_options_name import *
from modules.general.option_verify_area import *
from modules.utils import ocr_reg
# 点击空白回到静态页
clik_empty = ClickOperatorSteps(0, None, address_empty[0], address_empty[1])

# 点击势力
click_shili = ClickOperatorSteps(zhaomu_area, [zhaomu], shili_click[0], shili_click[1])
# 点击部队
click_budui = ClickOperatorSteps(zhengbing_page_verify_area, [shili], click_list_x_y[0], click_list_x_y[1])
# 点击征兵
click_zhengbing = ClickOperatorSteps(zhengbing_page_area, [zhengbing], zhengbing_click_xy[0], zhengbing_click_xy[1])

# 点击确认征兵，在此处是同一个页面 不需要校验
click_zhengbing_sure = ClickOperatorSteps(0, None, zhengbing_page_swipe_sure_xy[0], zhengbing_page_swipe_sure_xy[1])
# 征兵确认
click_zhengbing_require = ClickOperatorSteps(queding_area, [queding], queding_area_xy[0], queding_area_xy[1])
# 征兵已满
click_satify = ClickOperatorSteps(zhengbing_page_swipe_verify, [zhengbing_satisfy], zhengbing_page_swipe_sure_xy[0], zhengbing_page_swipe_sure_xy[1])
# 点击出征/ 扫荡  在此处是同一个页面 不需要校验
click_chuzheng_or_saodang = ClickOperatorSteps(0, None, address_going_require[0], address_going_require[1])

# 如果没有点击标记，则点击一次
click_sign_init = ClickOperatorSteps(0, None, address_area_start[0], address_area_start[1])

# 点击标记
click_sign = ClickOperatorSteps(address_sign_verify, [biaoji], address_sign_area[0], address_sign_area[1])

# 点击标记下方土地
click_sign_options = ClickOperatorSteps(0, None, address_sign_land_area[0], address_sign_land_area[1])

# 点击战报
click_battle = ClickOperatorSteps(zhaomu_area, [zhaomu], click_draw_area[0], click_draw_area[1])

# 查看个人详情
click_battle_main = ClickOperatorSteps(person_battle_area, [person_battle, battle_bf2, battle_info_txt], click_draw_detail_area[0],
                                       click_draw_detail_area[1])

# 战报内部点击战斗地点
click_battle_retreat = ClickOperatorSteps((690, 670, 840, 708), [battle_site_name], battle_site[0], battle_site[1])

# 重复确认
click_battle_require = ClickOperatorSteps(queding_area, [queding], queding_area_xy[0],
                                          queding_area_xy[1])
# 点击平局队伍, 验证方法重写
click_battle_lists = ClickOperatorSteps(retreat_area_require, [saodang, chuzheng], retreat_require_click[0],
                                        retreat_require_click[1])


def applyChangeClick(self):
    result = ocr_reg(self.getImgOcr())
    if any(item in result for item in self.verify_txt):
            operateTap(self.x, self.y)
            return True
    return False


click_battle_lists.applyClick = applyChangeClick.__get__(click_battle_lists)

# 点击撤退
click_battle_active = ClickOperatorSteps(retreat_click_area, [retreat_name], retreat_click_area_xy[0],
                                         retreat_click_area_xy[1])
# 二次确定点击撤退按钮
click_battle_retreat_append = ClickOperatorSteps(retreat_append_click, [retreat_name], retreat_append_click_xy[0],
                                                 retreat_append_click_xy[1])

# 取消标记
click_unmark = ClickOperatorSteps(0, None, cancel_sign[0], cancel_sign[1])

# 下一个标记
click_next_sign = ClickOperatorSteps(chuzheng_area, None, 0, 0)
