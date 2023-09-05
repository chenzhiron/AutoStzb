import datetime
import logging

from dispatcher.main import return_scheduler
from modules.module_address.module_address import (module_address_start, module_address_going,
                                                   module_address_list_going)

from modules.general.module_options_name import saodang as name_saodang


def saodang(going_list=0, max_num=1, name_id=0, auto_txt=name_saodang):
    scheduler = return_scheduler()
    logging.error(name_id +'\n\r' )
    logging.error(str(scheduler.get_jobs()) +'\n\r')
    module_address_start()
    module_address_going(auto_txt)
    times = module_address_list_going(going_list)

    if max_num - 1 > 0:
        scheduler.modify_job(name_id,
                             next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=(times * 2) + 5),
                             args=[going_list, max_num - 1, name_id])
    else:
        scheduler.remove_job(name_id)
