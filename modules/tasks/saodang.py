from modules.general.module_options_name import saodang as name_saodang
from modules.module_address.module_address import (module_address_start,
                                                   executed_going_list,
                                                   module_computed_going_time,
                                                   module_execute_list_click,
                                                   module_sign_Execute_order,
                                                   module_sign_land_area_click,
                                                   module_sign_area_area_click)


def saodang(going_list=1, auto_txt=name_saodang):
    module_address_start()
    module_sign_area_area_click()
    module_sign_land_area_click()
    module_sign_Execute_order(auto_txt)
    module_execute_list_click(going_list)
    times = module_computed_going_time()
    executed_going_list()
    return {
        'type':  2,
        'lists': going_list,
        'times': times,
    }