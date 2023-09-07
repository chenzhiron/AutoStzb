import datetime

from communication.task_store import change_store_data_value
from dispatcher.general import battle_dispose_result
from dispatcher.main import return_scheduler
from modules.module_address.module_address import (module_address_start, module_address_going,
                                                   module_address_list_going)

from modules.general.module_options_name import saodang as name_saodang
from modules.module_battle.module_draw import module_computed_draw


def saodang(going_list=0, name_id=0, auto_txt=name_saodang):
    scheduler = return_scheduler()
    module_address_start()
    module_address_going(auto_txt)
    times = module_address_list_going(going_list)
    # 目前只考虑平局一次的问题
    # scheduler.add_job(module_computed_draw, 'cron',
    #                   args=[datetime.datetime.now(), name_id],
    #                   next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=times))
    scheduler.add_job(module_computed_draw, 'date',
                      args=[datetime.datetime.now(), name_id, times],
                      next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=times),
                      id=str(name_id) + saodang.__name__ + str(going_list)
                      )
    change_store_data_value(name_id, 'next_execute', times)
