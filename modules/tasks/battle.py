from modules.module_battle.module_draw import module_click_draw, module_draw_verify, \
    module_draw_info


def battle():
    module_click_draw()
    module_draw_verify()
    result = module_draw_info()
    return {
        'type': 3,
        'result': result
    }
