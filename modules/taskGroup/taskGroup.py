import time

from modules.Class.accidental import select_active_lists, battle_info
from modules.Class.clickSetup import click_shili, click_budui, click_zhengbing, click_zhengbing_sure, \
    click_zhengbing_require, click_chuzheng_or_saodang, click_sign_options, click_sign, click_sign_init, click_battle, \
    click_battle_main, click_battle_retreat, click_battle_require, click_battle_lists, click_battle_retreat_append, \
    click_unmark
from modules.Class.originalSetup import chuzheng_max_time, zhengbing_max_time, click_options_options
from modules.Class.swipeSetup import swipe_zhengbing


def handle_in_map_conscription():
    # 需要捕获征兵队伍
    while 1:
        if click_shili.applyClick():
            continue
        if click_budui.applyClick():
            continue
        if click_zhengbing.applyClick():
            continue
        if swipe_zhengbing.applySwipe():
            times = zhengbing_max_time()
            if not (times is None):
                pass
        if click_zhengbing_require.applyClick():
            # 此处还有退出函数代码
            break
        if click_zhengbing_sure.applyClick():
            continue


def handle_in_lists_action():
    txt = '扫荡'
    if click_options_options.verify_txt != txt:
        click_options_options.verify_txt = txt
    # 出征部队
    while 1:
        if click_options_options.applyOriginalClick():
            continue
        result = select_active_lists(1)
        if type(result) == int:
            return result
        times = chuzheng_max_time()
        if not (times is None):
            click_chuzheng_or_saodang.applyClick(status=True)
            return
        if click_sign.applyClick():
            click_sign_options.applyClick(status=True)
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
        if click_battle_retreat.applyClick(status=False):
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
