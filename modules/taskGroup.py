import time

from modules.Class.accidental import select_active_lists, battle_info, handle_out_map
from modules.Class.clickSetup import click_shili, click_budui, click_zhengbing, click_zhengbing_sure, \
    click_zhengbing_require, click_chuzheng_or_saodang, click_sign_options, click_sign, click_sign_init, click_battle, \
    click_battle_main, click_battle_retreat, click_battle_require, click_battle_lists, click_battle_retreat_append, \
    click_unmark, click_battle_active, click_next_sign
from modules.Class.originalSetup import chuzheng_max_time, zhengbing_max_time, click_options_options
from modules.Class.swipeSetup import swipe_zhengbing


def handle_in_map_conscription(instance):
    times = 0
    # 需要捕获征兵队伍
    while 1:
        if click_zhengbing_require.applyClick():
            instance.change_config_storage_by_key('next_times', times)
            handle_out_home()
            return instance
        if swipe_zhengbing.applySwipe():
            times = zhengbing_max_time()
            if times == 0:
                instance.change_config_storage_by_key('next_times', times)
                handle_out_home()
                return instance
        if click_zhengbing.applyClick():
            continue
        if click_budui.applyClick(instance.lists):
            continue
        if click_shili.applyClick():
            continue
        if click_zhengbing_sure.applyClick():
            continue


def handle_in_lists_action(instance):
    if click_options_options.verify_txt != instance.txt:
        click_options_options.verify_txt = instance.txt
        task_group = instance.task_group[:]
        if task_group[-1].__name__ != 'handle_in_unmark':
            task_group.append(handle_in_unmark)
            instance.change_config_storage_by_key('task_group', task_group)
    # 出征部队
    while 1:
        if click_options_options.applyOriginalClick():
            continue
        result = select_active_lists(instance.lists)
        if type(result) == int:
            instance.change_config_storage_by_key('next_times', result)
            instance.change_config_storage_by_key('setup', instance.setup - 1)
            return instance
        times = chuzheng_max_time()
        if not (times is None):
            click_chuzheng_or_saodang.applyClick(status=True)
            instance.change_config_storage_by_key('next_times', times)
            return instance
        if click_sign.applyClick():
            click_sign_options.applyClick(status=True, offset_y=instance.offset)
            continue
        if click_sign_init.applyClick(status=True):
            continue


# 点击查看战报
def handle_in_battle_result(instance):
    start_time = time.time()
    while 1:
        if click_battle.applyClick():
            continue
        if click_battle_main.applyClick():
            instance.change_config_storage_by_key('battle_result', battle_info())
            end_time = time.time()
            instance.change_config_storage_by_key('next_times', instance.next_times - (end_time - start_time)
            if instance.next_times - (end_time - start_time) > 0 else 0)
            handle_out_home()
            return instance


# 点击撤退函数
def handle_in_draw_battle(instance):
    status1 = True
    status2 = True
    status3 = True
    status4 = True
    while 1:
        if status2:
            if click_battle_require.applyClick():
                status2 = False
                continue
        if status1:
            if click_battle_retreat.applyClick(status=True):
                status1 = False
                continue
        if status3:
            if click_battle_lists.applyClick(status=True):
                status3 = False
                continue
        if status4:
            if click_battle_active.applyClick():
                status4 = False
                continue
        if click_battle_retreat_append.applyClick():
            return instance


# 取消标记
def handle_in_unmark(instance=None):
    while 1:
        if click_sign.applyClick():
            time.sleep(1)
            click_unmark.applyClick()
            res = click_next_sign.getImgOcr()
            if res[0] is None:
                instance.change_config_storage_by_key('status', False)
            instance.change_config_storage_by_key('next_times', 1)
            handle_out_home()
            return instance
        if click_sign_init.applyClick(status=True):
            continue
        if click_sign_options.applyClick(status=True):
            continue


# 返回首页
def handle_out_home():
    while 1:
        if handle_out_map.verifyOcr():
            handle_out_map.applyClick()
        else:
            return None
