import time

from modules.Class.accidental import select_active_lists, battle_info
from modules.Class.clickSetup import click_shili, click_budui, click_zhengbing, click_zhengbing_sure, \
    click_zhengbing_require, click_chuzheng_or_saodang, click_sign_options, click_sign, click_sign_init, click_battle, \
    click_battle_main, click_battle_retreat, click_battle_require, click_battle_lists, click_battle_retreat_append, \
    click_unmark
from modules.Class.originalSetup import chuzheng_max_time, zhengbing_max_time, click_options_saodang, \
    click_options_chuzheng
from modules.Class.swipeSetup import swipe_zhengbing


def handle_in_map_conscription():
    # 需要捕获征兵队伍
    while 1:
        if click_shili.applyClick(1):
            continue
        if click_budui.applyClick(1):
            continue
        if click_zhengbing.applyClick():
            continue
        if swipe_zhengbing.applySwipe():
            continue
        times = zhengbing_max_time()
        if times == 0:
            return None
        if click_zhengbing_sure.applyClick():
            continue
        if click_zhengbing_require.applyClick(1):
            # 此处还有退出函数代码
            break


def handle_in_lists_action():
    txt = '扫荡'
    # 出征部队
    while 1:
        if click_options_saodang.applyOriginalClick() if txt == '扫荡' else click_options_chuzheng.applyClick():
            continue
        times = chuzheng_max_time()
        if times != 0:
            click_chuzheng_or_saodang.applyClick(status=True)
            return
        result = select_active_lists(1)
        if type(result) == int:
            return result
        if click_sign.applyClick():
            continue
        if click_sign_init.applyClick(status=True):
            continue


def handle_in_battle_result():
    while 1:
        if click_battle.applyClick():
            continue
        if click_battle_main.applyClick():
            continue
        result = battle_info()
        return None


def handle_in_draw_battle():
    while 1:
        if click_battle_retreat.applyClick():
            continue
        if click_battle_require.applyClick():
            continue
        if click_battle_retreat_append.applyClick():
            continue
        if click_battle_require.applyClick():
            return
        if click_battle_lists.applyClick(status=True):
            continue


def handle_in_unmark():
    while 1:
        if click_sign.applyClick():
            time.sleep(1)
            click_unmark.applyClikk()
            return
        if click_sign_options.applyClick(status=True):
            continue
