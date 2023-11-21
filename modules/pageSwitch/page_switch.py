import time

import numpy as np
from config.custom import customConfig

from device.AutoMation import automation
from device.operate import operate_adb_tap, operate_adb_swipe
from modules.taskConfigStorage.main import change_config_storage_by_key, update_config_storage, \
    get_config_storage_by_key_value
from modules.utils.main import calculate_max_timestamp, computedexecuteClickArea
from modules.general.module_options_name import shili, zhengbing, require_zhengbing, zhengbing_satisfy, queding, \
    going_list_txt, person_battle, battle_details, biaoji, retreat_name, zhaomu, battle_site_name
from modules.general.option_verify_area import address_area_start, address_sign_verify, address_sign_land_area, \
    address_execute_order_area, address_execute_list, computed_going_time_area, computed_going_list_area, \
    address_going_require, click_draw_area, click_draw_detail_area, person_battle_area, person_detail_battle_area, \
    person_status_number_area, enemy_status_number_area, status_area, shili_area, zhengbing_page_verify_area, \
    click_list_x_y, zhengbing_page_area, zhengbing_page_swipe_verify, zhengbing_page_swipe, zhengbing_time_area, \
    queding_area, tili_area, zhaomu_area, return_area, bianduilists, retreat_area, retreat_click_area, \
    retreat_append_click, battle_site, retreat_discern_require_area, retreat_require_click, sigin_action_area, \
    cancel_sign
from ocr.main import ocr_default


# 回到首页
def handle_out_map():
    while 1:
        try:
            image = automation.get_screenshots()
            result = ocr_default(np.array(image.crop(zhaomu_area)))
            result = ocr_reg(result)
            if len(result) > 0 and result[0] == '招募':
                return True
            else:
                x, y = return_area
                operate_adb_tap(x, y)
        except Exception as e:
            print('返回主页面发生了错误', e)
            return False


# 队伍征兵
def handle_in_map_conscription(taskid):
    l = get_config_storage_by_key_value(taskid, 'lists')
    update_config_storage(taskid, {'type': 1,
                                   'times': 0
                                   }
                          )
    while 1:
        try:
            image = automation.get_screenshots()
            # 点击势力
            if appear_then_click(image.crop(zhaomu_area), shili_area, [zhaomu]):
                continue
            # 选择部队
            if appear_then_click(image.crop(zhengbing_page_verify_area),
                                 zhengbing_page_verify_area,
                                 [shili], False):
                x, y = click_list_x_y
                operate_adb_tap(x * l, y)
                continue
            # 点击征兵按钮
            if appear_then_click(image.crop(zhengbing_page_area), zhengbing_page_area, zhengbing):
                continue
            # 拖动进度条 并点击征兵
            if appear_then_click(image.crop(zhengbing_page_swipe_verify), zhengbing_page_swipe_verify,
                                 [require_zhengbing, zhengbing_satisfy],
                                 False):
                for v in zhengbing_page_swipe:
                    # if enhance:
                    #     operate_adb_swipe(v[0], v[1], int(v[2] * 0.2), v[3])
                    # else:
                    operate_adb_swipe(v[0], v[1], v[2], v[3])
                image = automation.get_screenshots()
                time_res = ocr_reg(ocr_default(np.array(image.crop(zhengbing_time_area))))
                times = calculate_max_timestamp(time_res)
                change_config_storage_by_key(taskid, 'times', times)
                # 如果是满兵，则不需要征兵
                if times == 0:
                    handle_out_map()
                    return None

                x, y = computedexecuteClickArea(zhengbing_page_swipe_verify)
                operate_adb_tap(x, y)
                continue
            # 点击确定
            if appear_then_click(image.crop(queding_area), queding_area, queding):
                handle_out_map()
                return None
        except Exception as e:
            print('征兵模块 发生了错误', e)
            return None


def appear_then_click(img_source, click_area, check_txt, clicked=True):
    res = ocr_default(np.array(img_source))
    if not bool(res[0]):
        return False

    result = ''
    for sublist in res:
        for item in sublist:
            result += item[1][0]
    if not (result in check_txt):
        return False

    if clicked:
        x, y = computedexecuteClickArea(click_area)
        operate_adb_tap(x, y)
    return True


# 队伍出发
def handle_in_lists_action(taskid):
    l = get_config_storage_by_key_value(taskid, 'lists')
    txt = get_config_storage_by_key_value(taskid, 'txt')
    offset_y = get_config_storage_by_key_value(taskid, 'offset')
    update_config_storage(taskid, {
        'type': 2,
    })
    time_sleep = customConfig.getTimesleep()
    while 1:
        try:
            image = automation.get_screenshots()

            # 识别扫荡并点击
            result = ocr_default(np.array(image.crop(address_execute_order_area)))
            if bool(result[0]):
                status = False
                for idx in range(len(result)):
                    res = result[idx]
                    for line in res:
                        if line[1][0] == txt:
                            first_list = line[0]
                            center_point = [sum(coord) / len(coord) for coord in zip(*first_list)]
                            operate_adb_tap(820 + center_point[0], 200 + center_point[1])
                            status = True
                            break
                    break
                if status:
                    continue

            # 扫荡时间跟点击出征
            if appear_then_click(image.crop(address_going_require), address_going_require, [txt], False):
                time_res = ocr_reg(ocr_default(np.array(image.crop(computed_going_time_area))))
                times = calculate_max_timestamp(time_res)
                x, y = computedexecuteClickArea(address_going_require)
                operate_adb_tap(x, y)
                change_config_storage_by_key(taskid, 'times', times)
                return None
            # 选择部队页面
            if appear_then_click(image.crop(computed_going_list_area), computed_going_list_area, [going_list_txt],
                                 False):
                result = ocr_reg(ocr_default(np.array(image.crop(bianduilists))))
                if len(result) > 0:
                    try:
                        current_max = int(result[0][2]) - 1
                    except Exception as e:
                        continue
                    residue_tili = ocr_reg(ocr_default(np.array(image.crop(
                        (tili_area[current_max][l - 1])
                    ))
                    ))
                    # 此处需要计算没有体力的情况下，直接返回结果，但是结果要更改任务顺序
                    if len(residue_tili) > 0 and residue_tili[0] is not None:
                        change_config_storage_by_key(taskid, 'result', calculate_max_timestamp(residue_tili))
                        return None
                    x, y = address_execute_list[current_max][l - 1]
                    operate_adb_tap(x, y)
                continue

            # 点击标记并点击下方土地
            if appear_then_click(image.crop(address_sign_verify), address_sign_verify, [biaoji]):
                time.sleep(time_sleep)
                x, y = computedexecuteClickArea(address_sign_land_area)
                operate_adb_tap(x, y + offset_y)
                continue
            # 如果没有点击标记，则点击一次
            if not appear_then_click(image.crop(address_sign_verify), address_sign_verify, [biaoji], False):
                operate_adb_tap(address_area_start[0], address_area_start[1])
                continue
        except Exception as e:
            print('扫荡/出征发生了错误', e)
            return None


# 战报结果
def handle_in_battle_result(taskid):
    current_time = get_config_storage_by_key_value(taskid, 'times')
    battle_result = {}
    start_time = time.time()
    time_sleep = customConfig.getTimesleep()
    while 1:
        try:
            image = automation.get_screenshots()

            if appear_then_click(image.crop(zhaomu_area), shili_area, ['招募'], False):
                operate_adb_tap(click_draw_area[0], click_draw_area[1])
                continue
            if appear_then_click(image.crop(person_battle_area), person_battle_area, [person_battle], False):
                time.sleep(time_sleep)
                operate_adb_tap(click_draw_detail_area[0], click_draw_detail_area[1])
                continue
            if appear_then_click(image.crop(person_detail_battle_area), person_detail_battle_area, [battle_details],
                                 False):
                image = automation.get_screenshots()
                status = ''
                person_number = ''
                enemy_number = ''
                while not bool(status) and not bool(person_number) and not bool(enemy_number):
                    status = ocr_reg(ocr_default(np.array(image.crop(status_area))))[0]
                    person_number = ocr_reg(ocr_default(np.array(image.crop(person_status_number_area))))[0]
                    enemy_number = ocr_reg(ocr_default(np.array(image.crop(enemy_status_number_area))))[0]

                battle_result['status'] = status
                battle_result['person'] = person_number
                battle_result['enemy'] = enemy_number
                handle_out_map()
                battle_result['time_sleep'] = current_time - (int(time.time()) - int(start_time))
                update_config_storage(taskid, {
                    'type': 3,
                    'battle_result': battle_result
                })
                return None

        except Exception as e:
            print('执行战报发生了错误', e)
            return None


# 战斗平局
def handle_battle_draw_result(taskid):
    update_config_storage(taskid, {
        'type': 4,
        'status': 0
    })
    time_sleep = customConfig.getTimesleep()
    while 1:
        try:
            image = automation.get_screenshots()

            if appear_then_click(image.crop(retreat_area), retreat_click_area, [retreat_name]):
                time.sleep(time_sleep)
                continue
            if appear_then_click(image.crop(retreat_append_click), retreat_append_click, [retreat_name]):
                return None
            if appear_then_click(image.crop(zhaomu_area), shili_area, [zhaomu], False):
                operate_adb_tap(click_draw_area[0], click_draw_area[1])
                continue
            if appear_then_click(image.crop(person_battle_area), person_battle_area, [person_battle], False):
                time.sleep(time_sleep)
                operate_adb_tap(click_draw_detail_area[0], click_draw_detail_area[1])
                continue
            if appear_then_click(image.crop(battle_site), battle_site, [battle_site_name]):
                continue
            if appear_then_click(image.crop(retreat_discern_require_area), retreat_discern_require_area, [queding]):
                time.sleep(time_sleep)
                x, y = retreat_require_click
                operate_adb_tap(x, y)
                time.sleep(time_sleep)
                continue
        except Exception as e:
            print('战报平局模块发生了错误', e)
            return None


# 基于标记出征土地
def handle_sign_action(taskid):
    count = 0
    update_config_storage(taskid, {
        'type': 5,
        'offset': 0
    })
    time_sleep = customConfig.getTimesleep()
    while count < 60:
        image = automation.get_screenshots()

        # 点击标记并点击下方土地
        if appear_then_click(image.crop(address_sign_verify), address_sign_verify, [biaoji]):
            time.sleep(time_sleep)
            result = ocr_reg(ocr_default(np.array(image.crop(sigin_action_area))))
            count += 1
            if len(result) >= 2:
                change_config_storage_by_key(taskid, 'offset', 45)
                return None

        # 如果没有点击标记，则点击一次
        if not appear_then_click(image.crop(address_sign_verify), address_sign_verify, [biaoji], False):
            operate_adb_tap(address_area_start[0], address_area_start[1])
            count += 1
            continue
    return None


# 取消标记
def handle_unmark(taskid):
    update_config_storage(taskid, {
        'type': 6
    })
    time_sleep = customConfig.getTimesleep()
    while 1:
        image = automation.get_screenshots()
        if appear_then_click(image.crop(address_sign_verify), address_sign_verify, [biaoji]):
            time.sleep(time_sleep)
            x, y = cancel_sign
            operate_adb_tap(x, y)
            result = ocr_reg(ocr_default(np.array(image.crop(sigin_action_area))))
            if len(result) >= 2:
                change_config_storage_by_key(taskid, 'offset', 45)
            else:
                change_config_storage_by_key(taskid, 'offset', 0)
            return None
            # 如果没有点击标记，则点击一次
        if not appear_then_click(image.crop(address_sign_verify), address_sign_verify, [biaoji], False):
            operate_adb_tap(address_area_start[0], address_area_start[1])
            time.sleep(time_sleep)
            continue


def ocr_reg(res):
    if bool(res[0]):
        return [item[1][0] for sublist in res for item in sublist]
    else:
        return []
