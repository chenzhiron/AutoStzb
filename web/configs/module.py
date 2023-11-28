from config.custom import customConfig
from modules.tasks import Task
from config.task_or_web_common import configType, saodangType, chuzhengType, zhengbingType, chengpiType, wotuType

listGroup = [
    {
        'label': 1,
        'value': 1
    },
    {
        'label': 2,
        'value': 2
    },
    {
        'label': 3,
        'value': 3
    },
    {
        'label': 4,
        'value': 4
    },
    {
        'label': 5,
        'value': 5
    }
]
checkboxGroup = [{
    'label': '',
    'value': True
}]


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
        instance.change_config_storage_by_key('offset', 180)
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


def change_time_sleep(v, instance):
    instance.changeTimesleep(v)


def create_config(name, explain, ctype, fn, value, options=None):
    config = {
        'name': name,
        'explain': explain,
        'type': ctype,
        'fn': fn,
        'value': value,
    }
    if options is not None:
        config['options'] = options

    return config


def create_instance(task_type):
    # 截图配置时间延迟
    if task_type == configType:
        return customConfig

        # 正常任务
    task = Task(task_type)

    # 出征城皮
    if task_type == chengpiType:
        task.change_config_storage_by_key('change_delay_time', 900)
    if task_type == wotuType:
        task.change_config_storage_by_key('change_delay_time', 3600)

    if task_type == saodangType:
        task.change_config_storage_by_key('skip_conscription', False)
    return task


def create_option(name, task_type, configs):
    return {
        'name': name,
        'config': [config for config in configs],
        'instance': create_instance(task_type)
    }


def create_saodang_option(name, task_type):
    configs = [
        create_config('status', '启动', 'checkbox', task_start_saodang, False, checkboxGroup),
        create_config('lists', '选择编队', 'select', change_lists, 1, listGroup),
        create_config('circulation', '循环次数', 'input', change_circulation, 1),
        create_config('delay_time', '延迟时间', 'input', change_delay_time, 0),
        create_config('skip_conscription', '跳过征兵继续扫荡', 'checkbox', change_skip_conscription, False, checkboxGroup),
    ]

    return create_option(name, task_type, configs)


def create_chuzheng_options(name, task_type):
    configs = [
        create_config('status', '启动', 'checkbox', task_start_chuzheng, False, checkboxGroup),
        create_config('lists', '选择编队', 'select', change_lists, 1, listGroup),
        create_config('delay_time', '延迟时间', 'input', change_delay_time, 2),
    ]

    return create_option(name, task_type, configs)


def create_config_options(name, task_type):
    configs = [
        create_config('time_sleep', '截图延迟时间，单位 秒', 'input', change_time_sleep, 1),
    ]

    return create_option(name, task_type, configs)


def create_zhengbing_options(name, task_type):
    configs = [
        create_config('status', '启动', 'checkbox', task_start_saodang, False, checkboxGroup),
        create_config('lists', '选择编队', 'select', change_lists, 1, listGroup),
    ]
    return create_option(name, task_type, configs)


options_config = [
    {
        'groupName': '配置',
        'taskType': configType,
        'options': [create_config_options('延迟', configType)]
    },
    {
        'groupName': '征兵',
        'taskType': zhengbingType,
        'options': [create_zhengbing_options(f'编队{i + 1}', zhengbingType) for i in range(3)]
    },
    {
        'groupName': '扫荡',
        'taskType': saodangType,
        'options': [create_saodang_option(f'编队{i + 1}', saodangType) for i in range(5)]
    },
    {
        'groupName': '出征',
        'taskType': chuzhengType,
        'options': [create_chuzheng_options(f'编队{1}', chengpiType),
                    create_chuzheng_options('城皮', chengpiType),
                    create_chuzheng_options('沃土', wotuType)]
    }
]
