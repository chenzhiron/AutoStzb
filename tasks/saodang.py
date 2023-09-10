from modules.general.module_options_name import saodang as name_saodang
from modules.module_address.module_address import (module_address_start, module_address_going,
                                                   module_address_list_going)


def saodang(going_list=0, auto_txt=name_saodang):
    module_address_start()
    module_address_going(auto_txt)
    times = module_address_list_going(going_list)
    return {
        'lists': going_list,
        'times': times,
    }
