import time
from config.const import TIMESLEEP
from modules.module_battle.module_draw import module_click_draw, module_draw_verify, \
    module_draw_info


def battle():
    time.sleep(TIMESLEEP)
    module_click_draw()
    time.sleep(TIMESLEEP)
    module_draw_verify()
    time.sleep(TIMESLEEP)
    module_draw_info()

