from modules.task.OperatorSteps import *
from modules.task.general.module_options_name import *
from modules.task.general.option_verify_area import *

return_main = OutOperatorSteps(huodon_area, '活动', 1530, 50)

# 点击空白回到静态页
click_empty = EntryOperatorSteps(None, '', address_empty[0], address_empty[1])

# 征兵流程 常规
# ~~~~~~~~~~~~ start ~~~~~~~~~~~~~
# 主页 进入 势力
verfiy_main = VerifyOperatorSteps(huodon_area, '活动', 410, 800)

# 点击部队
click_budui = VerifyOperatorSteps(shili_area, shili, jizun_duiwu[0], jizun_duiwu[1])

# 点击征兵
click_zhengbing = VerifyOperatorSteps(zhengbing_area, zhengbing, zhengbing_area[0], zhengbing_area[1])

# 滑动征兵进度条
swipe_zhengbing = SwipeOperatorSteps(zhengbing_swipe_verify, '征兵数量', zhengbing_page_swipe)

# 征兵时间
zhengbing_max_time = OcrOperatorSteps(zhengbing_time_area, '', 'await_time')

# 点击确认征兵，在此处是同一个页面 不需要校验
click_zhengbing_sure = EntryOperatorSteps([1250, 798, 1430, 840], '确认证兵', queren_area[0], queren_area[1])

# 征兵确认
click_zhengbing_require = VerifyOperatorSteps(queren_sure, queding, queren_sure[0], queren_sure[1])

# ~~~~~~~~~~~~ end ~~~~~~~~~~~~~

# 额外情况 补充
# 征兵已满
click_satify = VerifyOperatorSteps(zhengbing_page_swipe_verify, [zhengbing_satisfy], zhengbing_page_swipe_sure_xy[0],
                                   zhengbing_page_swipe_sure_xy[1])

# ~~~~~~~~~~~~
# 出征 + 扫荡选项
click_big_land = VerifyOperatorSteps(huodon_area, '活动', 1410, 100)
# 跳转土地位置
click_land_x = InputOperatorSteps('', [1430, 835, 1550, 880], '跳转', 1200, 860)
click_land_y = InputOperatorSteps('', [1430, 835, 1550, 880], '跳转', 1330, 860)
click_land_require = VerifyOperatorSteps([1430, 835, 1550, 880], '跳转', 1430, 860)
# 跳转后点击土地中心
click_land_center = Land_EntryOperatorSteps(None, '', 800, 450)
# 扫荡
click_sign_land_saodang = ExtraOperatorSteps([950, 230, 1400, 540], '扫荡', 920, 250)
# 出征
click_sign_land_chuzheng = ExtraOperatorSteps([950, 250, 1400, 660], '出证', 920, 250)
# 选择部队
click_going_lists = VerifyOperatorSteps([0, 690, 200, 750], '请选择部队', 800, 700)
# ~
# 识别时间
going_max_time = OcrOperatorSteps([770, 645, 895, 695], '', '_speed_time')
# 点击出征
click_chuzheng = VerifyOperatorSteps([1350, 804, 1425, 850], '出证', 1350, 825)
# 点击扫荡
click_saodang = VerifyOperatorSteps([1350, 804, 1425, 850], '扫荡', 1350, 825)

# ~~~~~~~~~~~~ end ~~~~~~~~~~~~~

# 战报模块0.....
# 主页 进入 战报
verfiy_main_info = VerifyOperatorSteps(huodon_area, '活动', 145, 670)
# 点击战报筛选
click_search_screen = VerifyOperatorSteps([1555, 438, 1600, 505], '筛选', 1580, 480)
# 战报搜索

click_search_x = InputOperatorSteps('', [1400, 618, 1500, 655], '搜索', 1180, 635)
click_search_y = InputOperatorSteps('', [1400, 618, 1500, 655], '搜索', 1300, 635)
# 点击搜索
click_search = EntryOperatorSteps([1400, 618, 1500, 655], '搜索', 1440, 635)
# 判断状态
lists_status = StatusOcrOperatorSteps([675, 270, 870, 420], '', '_list_status')
# 平局 ~~~~~~~~~
# 查询兵力
# 我方
search_persons = NumberOcrOperatorSteps('person', [90, 235, 250, 280], '')
# 敌方
search_enemy = NumberOcrOperatorSteps('enemy', [1321, 235, 1475, 280], '')

# 平局撤退
click_info_require = EntryOperatorSteps(None, '', 790, 208)
click_go_require = VerifyOperatorSteps([860,570,1065,615], '确定', 980, 595)
# 撤退中的土地
click_state_info = ChetuitOperatorSteps([660,350,965,525], '', 800, 450)
click_chetui = VerifyOperatorSteps([1445,375,1570,406], '撤退', 1515,390)
click_chetui_require = VerifyOperatorSteps([1330,805,1530,845], '撤退', 1430,822)
