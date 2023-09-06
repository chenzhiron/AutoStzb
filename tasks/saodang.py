import datetime
import logging

from dispatcher.main import return_scheduler
from modules.module_address.module_address import (module_address_start, module_address_going,
                                                   module_address_list_going)

from modules.general.module_options_name import saodang as name_saodang
from modules.module_battle.module_draw import module_computed_draw
from tasks.zhengbing import zhengbing


def saodang(going_list=0, max_num=1, name_id=0, auto_txt=name_saodang):
    scheduler = return_scheduler()
    logging.error(name_id +'\n\r' )
    logging.error(str(scheduler.get_jobs()) +'\n\r')
    module_address_start()
    module_address_going(auto_txt)
    times = module_address_list_going(going_list)

    battle_result = scheduler.add_job(module_computed_draw, 'cron',
                                      args=[datetime.datetime.now()],
                                      next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=times))
    if battle_result['result'] == 'success' or battle_result['result'] == 'lose':
        scheduler.pause_job(name_id)
        len_time = scheduler.add_job(zhengbing, 'date', args=[going_list], next_run_time=datetime.datetime.now())
    else:
        if max_num - 1 > 0:
            scheduler.modify_job(name_id,
                                 next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=times + 5),
                                 args=[going_list, max_num - 1, name_id])
        else:
            scheduler.remove_job(name_id)

