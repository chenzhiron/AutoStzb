from pywebio.output import use_scope, put_loading, put_text


def render_status(t):
    with use_scope('status', clear=True):
        # 出错
        if t == 2:
            put_loading(shape='grow', color='warning').style('height: 50px'), put_text('调度器出错了')
            # 正常
        if t == 1:
            put_loading(shape='border', color='primary').style('height: 50px'), put_text('调度器运行中')
            # 未启动
        if t == 0:
            put_text('调度器未启动')


def task_start_saodang(v, instance):
    if len(v) > 0:
        instance.change_config_storage_by_key('txt', '扫荡')
        instance.change_config_storage_by_key('status', True)
        instance.next_start()
    else:
        instance.change_config_storage_by_key('status', False)


def task_start_chuzheng(v, instance):
    if len(v) > 0:
        instance.change_config_storage_by_key('txt', '出证')
        instance.change_config_storage_by_key('status', True)
        instance.change_config_storage_by_key('offset', 205)
        instance.next_start()
    else:
        instance.change_config_storage_by_key('status', False)


def change_lists(v, instance):
    instance.change_config_storage_by_key('lists', int(v))


def change_delay_time(v, instance):
    instance.change_config_storage_by_key('delay_time', int(v) if int(v) > 0 else 0)


def change_circulation(v, instance):
    instance.change_config_storage_by_key('circulation', int(v) if int(v) > 0 else 0)


def change_skip_conscription(v, instance):
    if len(v) > 0:
        instance.change_config_storage_by_key('skip_conscription', True)
    else:
        instance.change_config_storage_by_key('skip_conscription', False)


def change_residue_person_ratio(v, instance):
    if float(v) < 0 or float(v) > 1:
        v = 0
    instance.change_config_storage_by_key('residue_person_ratio', float(v))


def change_residue_enemy_ratio(v, instance):
    if float(v) < 0 or float(v) > 1:
        v = 1
    instance.change_config_storage_by_key('residue_enemy_ratio', float(v))


def task_start_scheduler(v, instance):
    if len(v) > 0:
        instance.start()
        render_status(1)
    else:
        render_status(0)
        instance.stop()


def change_time_sleep(v, instance):
    instance.changeTimesleep(v)


def task_start_chengpi(v, instance):
    if len(v) > 0:
        instance.change_config_storage_by_key('txt', '出证')
        instance.change_config_storage_by_key('status', True)
        instance.change_config_storage_by_key('offset', 60)
        instance.next_start()
    else:
        instance.change_config_storage_by_key('status', False)


def task_start_wotu(v, instance):
    if len(v) > 0:
        instance.change_config_storage_by_key('txt', '出证')
        instance.change_config_storage_by_key('status', True)
        instance.change_config_storage_by_key('offset', 120)
        instance.next_start()
    else:
        instance.change_config_storage_by_key('status', False)
