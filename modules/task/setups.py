from modules.task.OperatorSteps import *
from modules.task.general.module_options_name import *
from modules.task.general.option_verify_area import *

return_main = OutOperatorSteps(huodon_area, active_name, 1530, 50)

# 点击空白回到静态页
click_empty = EntryOperatorSteps(None, '', address_empty[0], address_empty[1])

# 征兵流程 常规
# ~~~~~~~~~~~~ start ~~~~~~~~~~~~~
# 主页 进入 势力
verfiy_main = VerifyOperatorSteps(huodon_area, active_name, 410, 800)

# 点击部队
click_budui = VerifyOperatorSteps(shili_area, shili_name, jizun_duiwu[0], jizun_duiwu[1])

# 点击征兵
click_zhengbing = VerifyOperatorSteps(zhengbing_area, zhengbing_name, zhengbing_area[0], zhengbing_area[1])

# 滑动征兵进度条
swipe_zhengbing = SwipeOperatorSteps(zhengbing_swipe_verify, zhengbing_number_name, zhengbing_page_swipe)

# 征兵时间
zhengbing_max_time = OcrOperatorSteps(zhengbing_time_area, '', 'await_time')

# 点击确认征兵，在此处是同一个页面 不需要校验
click_zhengbing_sure = EntryOperatorSteps(click_zhengbing_sure_area, require_zhengbing_name, queren_area[0], queren_area[1])

# 征兵确认
click_zhengbing_require = VerifyOperatorSteps(queren_sure, queding_name, queren_sure[0], queren_sure[1])

# ~~~~~~~~~~~~
# 出征 + 扫荡选项
click_big_land = VerifyOperatorSteps(huodon_area, active_name, 1410, 100)
# 跳转土地位置

click_land_x = GotoOperatorSteps('', click_land_x_area, moving_name, 1200, 860, 0)
click_land_y = GotoOperatorSteps('', click_land_y_area, moving_name, 1330, 860, 1)
click_land_require = VerifyOperatorSteps(click_land_require_area, moving_name, 1430, 860)
# 跳转后点击土地中心
click_land_center = Land_EntryOperatorSteps(None, '', 800, 450)
# 扫荡
click_sign_land_saodang = ExtraOperatorSteps(click_sign_land_saodang_area, saodang_name, 920, 250)
# 出征
click_sign_land_chuzheng = ExtraOperatorSteps(click_sign_land_chuzheng_area, chuzheng_name, 920, 250)
# 选择部队
click_going_lists = VerifyOperatorSteps(click_going_lists_area, going_list_txt_name, 800, 700)
# ~
# 识别时间
going_max_time = OcrOperatorSteps(going_max_time_area, '', '_speed_time')
# 点击出征
click_chuzheng = VerifyOperatorSteps(click_chuzheng_area, chuzheng_name, 1350, 825)
# 点击扫荡
click_saodang = VerifyOperatorSteps(click_saodang_area, saodang_name, 1350, 825)

# ~~~~~~~~~~~~ end ~~~~~~~~~~~~~

# 战报模块0.....
# 主页 进入 战报
verfiy_main_info = VerifyOperatorSteps(huodon_area, active_name, 145, 670)
# 点击战报筛选
click_search_screen = VerifyOperatorSteps(click_search_screen_area, screen_name, 1580, 480)
# 战报搜索

click_search_x = InputOperatorSteps('', click_search_x_area, search_name, 1180, 635)
click_search_y = InputOperatorSteps('', click_search_y_area, search_name, 1300, 635)
# 点击搜索
click_search = EntryOperatorSteps(click_search_area, search_name, 1440, 635)
# 判断状态
lists_status = StatusOcrOperatorSteps(lists_status_area, '', '_list_status')
# 平局 ~~~~~~~~~
# 查询兵力
# 我方
search_persons = NumberOcrOperatorSteps('person', search_persons_area, '')
# 敌方
search_enemy = NumberOcrOperatorSteps('enemy', search_enemy_area, '')

# 平局撤退
click_info_require = EntryOperatorSteps(None, '', 790, 208)
click_go_require = VerifyOperatorSteps(click_go_require_area, queding_name, 980, 595)
# 撤退中的土地
click_state_info = ChetuitOperatorSteps(click_state_info_area, '', 800, 450)
click_chetui = VerifyOperatorSteps(click_chetui_area, retreat_name, 1515,390)
click_chetui_require = VerifyOperatorSteps(click_chetui_require_area, retreat_name, 1430,822)
