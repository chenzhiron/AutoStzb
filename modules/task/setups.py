from modules.task.OperatorSteps import *
from modules.task.general.module_options_name import *
from modules.task.general.option_verify_area import *

# 点击空白回到静态页
click_empty = EntryOperatorSteps([0, 0, 0, 0], None, address_empty[0], address_empty[1])



# 点击势力
click_shili = VerifyOperatorSteps(zhaomu_area, [zhaomu], shili_click[0], shili_click[1])

# 点击部队
click_budui = VerifyOperatorSteps(shili_area, [shili], jizun_duiwu[0], jizun_duiwu[1])

# 点击征兵
click_zhengbing = VerifyOperatorSteps(zhengbing_area, [zhengbing], zhengbing_area[0], zhengbing_area[1])

# 滑动征兵进度条
swipe_zhengbing = SwipeOperatorSteps(zhengbing_swipe_verify, [require_zhengbing], zhengbing_page_swipe)

# 征兵时间
zhengbing_max_time = OcrOperatorSteps(zhengbing_time_area, None, 'elapsed_time')

# 点击确认征兵，在此处是同一个页面 不需要校验
click_zhengbing_sure = EntryOperatorSteps([0, 0, 0, 0], None, queren_area[0], queren_area[1])

# 征兵确认
click_zhengbing_require = VerifyOperatorSteps(queren_sure, [queding], queren_sure[0], queren_sure[1])
# 征兵已满
click_satify = VerifyOperatorSteps(zhengbing_page_swipe_verify, [zhengbing_satisfy], zhengbing_page_swipe_sure_xy[0],
                                   zhengbing_page_swipe_sure_xy[1])

# 选择部队出征 方法得重写
click_list_going = VerifyOperatorSteps(computed_going_time_area, [saodang, chuzheng], 800, 200)
# 出征时间
chuzheng_time = OcrOperatorSteps(computed_going_time_area, 'None', 'speed_time')

# 点击 出征/ 扫荡  在此处是同一个页面 不需要校验
click_chuzheng_or_saodang = EntryOperatorSteps([0, 0, 0, 0], None, address_going_require[0], address_going_require[1])

# 如果没有点击标记，则点击一次
click_sign_init = EntryOperatorSteps([0, 0, 0, 0], None, address_area_start[0], address_area_start[1])

# 点击标记
click_sign = VerifyOperatorSteps(address_sign_verify, [biaoji], address_sign_area[0], address_sign_area[1])

# 点击标记下方土地
click_sign_options = EntryOperatorSteps([0, 0, 0, 0], None, address_sign_land_area[0], address_sign_land_area[1])

# 点击战报
click_battle = VerifyOperatorSteps(zhaomu_area, [zhaomu], click_draw_area[0], click_draw_area[1])

# 查看个人详情
click_battle_main = VerifyOperatorSteps(person_battle_area, [person_battle, battle_bf2, battle_info_txt],
                                        click_draw_detail_area[0],
                                        click_draw_detail_area[1])

# 战报内部点击战斗地点
click_battle_retreat = VerifyOperatorSteps((690, 670, 840, 708), [battle_site_name], battle_site[0], battle_site[1])

# 重复确认
click_battle_require = VerifyOperatorSteps(queding_area, [queding], queding_area_xy[0],
                                           queding_area_xy[1])
# 点击平局队伍, 验证方法重写
# click_battle_lists = ClickOperatorSteps(retreat_area_require, [saodang, chuzheng], retreat_require_click[0],
#                                         retreat_require_click[1])
# def applyChangeClick(self):
#     result = ocr_reg(self.getImgOcr())
#     if any(item in result for item in self.verify_txt):
#         # operateTap(self.x, self.y)
#         return True
#     return False
#
#
# click_battle_lists.applyClick = applyChangeClick.__get__(click_battle_lists)

# 点击撤退
click_battle_active = VerifyOperatorSteps(retreat_click_area, [retreat_name], retreat_click_area_xy[0],
                                          retreat_click_area_xy[1])
# 二次确定点击撤退按钮
click_battle_retreat_append = VerifyOperatorSteps(retreat_append_click, [retreat_name], retreat_append_click_xy[0],
                                                  retreat_append_click_xy[1])

# 取消标记
click_unmark = EntryOperatorSteps([0, 0, 0, 0], None, cancel_sign[0], cancel_sign[1])

# 下一个标记
# click_next_sign = OcrOperatorSteps(chuzheng_area, None, 0, 0)
# ------------------------------------------------------------------

verfiy_main = VerifyOperatorSteps(huodon_area, ['活动'], 410, 800)

