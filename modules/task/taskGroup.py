import time

from config.task_or_web_common import zhengbingType
from modules.task.Class.accidental import select_active_lists, battle_info, handle_out_map
from modules.task.Class.clickSetup import *
from modules.task.Class.originalSetup import chuzheng_max_time, zhengbing_max_time, click_options_options
from modules.task.Class.swipeSetup import swipe_zhengbing
from modules.general.module_error_txt import zhengbing_error, chuzheng_error, zhanbao_error, chetui_error, sign_error, \
    returnmain_error
from modules.log.log import logger


# 对一张图，切换页面和页面点击都会有延迟，对一张截图进行 区域识别 并点击

# 征兵
def handle_in_map_conscription(instance):
    logger.info('开始征兵模块')
    times = 0
    # 需要捕获征兵队伍
    while 1:
        if int(time.time()) - instance.elapsed_time > 120:
            logger.error(zhengbing_error)
            raise Exception(zhengbing_error)
        if click_satify.applyClick():
            logger.info('征兵已满')
            instance.change_config_storage_by_key('next_times', times)
            if instance.type == zhengbingType:
                instance.change_config_storage_by_key('status', False)
            handle_out_home(instance)
            return instance
        if click_zhengbing_require.applyClick():
            logger.info('确认确认征兵')
            instance.change_config_storage_by_key('next_times', times)
            if instance.type == zhengbingType:
                instance.change_config_storage_by_key('setup', instance.setup - 1)
            handle_out_home(instance)
            return instance
        if swipe_zhengbing.applySwipe():
            logger.info('滑动征兵进度条')
            times = zhengbing_max_time()
            if instance.type == zhengbingType:
                times = times + 300
        if click_zhengbing.applyClick():
            logger.info('点击征兵按钮')
            continue
        if click_budui.applyClick(instance.lists):
            logger.info('选择主城部队')
            continue
        if click_shili.applyClick():
            logger.info('选择势力')
            continue
        if click_zhengbing_sure.applyClick():
            logger.info('确认征兵')
            continue


# 出征/扫荡
def handle_in_lists_action(instance):
    if click_options_options.verify_txt != instance.txt:
        click_options_options.verify_txt = instance.txt
    # 出征部队
    while 1:
        if int(time.time()) - instance.elapsed_time > 120:
            logger.error(chuzheng_error)
            raise Exception(chuzheng_error)
        if click_options_options.applyOriginalClick():
            continue
        result = select_active_lists(instance.lists)
        if type(result) == int:
            logger.info('等待')
            clik_empty.applyClick(status=True)
            instance.change_config_storage_by_key('next_times', result)
            instance.change_config_storage_by_key('setup', instance.setup - 1)
            return instance
        times = chuzheng_max_time()
        if not (times is None):
            logger.info(click_options_options.verify_txt)
            click_chuzheng_or_saodang.applyClick(status=True)
            instance.change_config_storage_by_key('next_times', times)
            instance.change_config_storage_by_key('speed_time', times)
            return instance
        if click_sign.applyClick():
            click_sign_options.applyClick(status=True, offset_y=instance.offset)
            logger.info('点击标记下的土地')
            continue
        if click_sign_init.applyClick(status=True):
            logger.info('点击标记')
            continue


# 点击查看战报
def handle_in_battle_result(instance):
    start_time = time.time()
    instance.change_config_storage_by_key('battle_time', 0)
    while 1:
        if int(time.time()) - instance.elapsed_time > 120:
            logger.error(zhanbao_error)
            raise Exception(zhanbao_error)
        if click_battle.applyClick():
            logger.error('点击战报')
            continue
        if click_battle_main.applyClick():
            logger.error('战报详情')
            battle_result = battle_info()
            instance.change_config_storage_by_key('battle_result', battle_result)
            if battle_result['status'] == '平局':
                # 平局处理
                person = battle_result['person_number'].split('/')
                enemy = battle_result['enemy_number'].split('/')
                logger.info('我方剩余兵力:' + person[0])
                logger.info('守军剩余兵力:' + enemy[0])
                person_result = int(person[0]) >= int(int(person[1]) * instance.residue_person_ratio)
                enemy_result = int(enemy[0]) <= int(int(enemy[1]) * instance.residue_enemy_ratio)
                if person_result and enemy_result:
                    # 平局等待
                    instance.change_config_storage_by_key('battle_time', max(300 - (int(time.time() - start_time)), 1))
                    instance.change_config_storage_by_key('setup', instance.setup - 1)
                else:
                    # 平局点击撤退
                    instance.change_config_storage_by_key('next_times', 1)
            else:
                # 胜利 /战败跳过撤退任务
                instance.change_config_storage_by_key('setup', instance.setup + 1)
                instance.change_config_storage_by_key('next_times', instance.speed_time)
            # 跳过征兵
            if hasattr(instance, 'skip_conscription') and instance.skip_conscription:
                instance.change_config_storage_by_key('setup', instance.setup + 1)
            handle_out_home(instance)
            return instance


# 点击撤退函数
def handle_in_draw_battle(instance):
    while 1:
        if click_battle.applyClick():
            logger.info('点击战报')
            continue
        if click_battle_main.applyClick():
            logger.info('战报详情')
            while 1:
                if int(time.time()) - instance.elapsed_time > 120:
                    logger.error(chetui_error)
                    raise Exception(chetui_error)
                if click_battle_retreat_append.applyClick():
                    logger.info('撤退成功')
                    instance.change_config_storage_by_key('next_times', instance.speed_time)
                    break
                if click_battle_active.applyClick():
                    logger.info('部队撤退点击')
                    continue
                if click_battle_lists.applyClick():
                    continue
                if click_battle_retreat.applyClick():
                    continue
                if click_battle_require.applyClick():
                    continue
            return instance


# 取消标记
def handle_in_unmark(instance=None):
    while 1:
        if int(time.time()) - instance.elapsed_time > 120:
            raise Exception(sign_error)
        if click_sign.applyClick():
            time.sleep(1)
            click_unmark.applyClick()
            res = click_next_sign.getImgOcr()
            if res[0] is None:
                instance.change_config_storage_by_key('status', False)
            instance.change_config_storage_by_key('next_times', 1)
            handle_out_home(instance)
            instance.change_config_storage_by_key('circulation', 1)
            return instance
        if click_sign_init.applyClick(status=True):
            continue
        if click_sign_options.applyClick(status=True):
            continue


# 返回首页
def handle_out_home(instance):
    while 1:
        if int(time.time()) - instance.elapsed_time > 120:
            raise Exception(returnmain_error)
        if handle_out_map.verifyOcr():
            handle_out_map.applyClick()
        else:
            logger.info('返回主页')
            return None
