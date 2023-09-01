import logging
import datetime

from dispatcher.main import return_scheduler
from modules.module_address.module_address import (module_address_start, module_address_going,
                                                   module_address_list_going)


def saodang(going_list=0, max_num=1, auto_txt='扫荡'):
    module_address_start()
    module_address_going(auto_txt)
    times = module_address_list_going(going_list)
    scheduler = return_scheduler()

    if max_num - 1 > 0:
        # scheduler.remove_job(saodang.__name__)
        scheduler.add_job(saodang, 'date', args=[going_list, max_num - 1],
                          next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=(times * 2) + 10),
                        )

    logging.info(times)


