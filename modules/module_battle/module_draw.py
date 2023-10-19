from device.main import adb_tap
from modules.general.generalExecuteFn import executeFn, reg_ocr_verify

from modules.general.module_options_name import person_battle, battle_details, shili
from modules.module_battle.module_draw_area import person_battle_area, person_status_number_area, \
    enemy_status_number_area, \
    status_area, click_draw_area, person_detail_battle_area, click_draw_detail_area

from modules.module_shili.address_area import shili_area


# 点击战报
def module_click_draw():
    result = executeFn(
        reg_ocr_verify(shili_area, 2),
        shili
    )
    if result:
        adb_tap(click_draw_area[0], click_draw_area[1])
    print('end')


#     验证是否进入页面
def module_draw_verify():
    result = executeFn(
        reg_ocr_verify(person_battle_area, 2),
        person_battle
    )
    if result:
        adb_tap(click_draw_detail_area[0], click_draw_detail_area[1])


def module_draw_info():
    result = executeFn(
        reg_ocr_verify(person_detail_battle_area, 4),
        battle_details
    )
    if result:
        # 胜利/失败/平局
        status = reg_ocr_verify(status_area, 2)
        print(status)
        # 我方兵力
        person_number = reg_ocr_verify(person_status_number_area, 999)
        print(person_number)
        # 敌方兵力
        enemy_number = reg_ocr_verify(enemy_status_number_area)
        print(enemy_number)
