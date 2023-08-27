from modules.module_address.module_address import (module_address_start, module_address_going,
                                                   module_address_list_going)


def saodang( going_list=0, auto_txt='扫荡'):
    module_address_start()
    module_address_going(auto_txt)
    module_address_list_going(going_list)
