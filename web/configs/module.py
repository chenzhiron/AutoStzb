from modules.tasks import Task
from web.configs.common import saodangType, chuzhengType

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


def start(v, instance):
    instance.change_config_storage_by_key('txt', '扫荡')
    instance.change_config_storage_by_key('status', True)
    instance.next_start()


def start2(v, instance):
    instance.change_config_storage_by_key('lists', int(v))
    print(' 222- --- instance', instance)


def start3(v, instance):
    instance.change_config_storage_by_key('delay_time', int(v) if int(v) > 0 else 0)
    print('3333----- instance', instance)


def change_circulation(v, instance):
    instance.change_config_storage_by_key('circulation', int(v) if int(v) > 0 else 0)


def start4(v, instance):
    print('4444-----', v)


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
    task = Task(task_type)
    print(task_type, 'task_type')
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
        create_config('status', '启动', 'checkbox', start, False, checkboxGroup),
        create_config('lists', '选择编队', 'select', start2, 1, listGroup),
        create_config('circulation', '循环次数', 'input', change_circulation, 1),
        create_config('delay_time', '延迟时间', 'input', start3, 0),
        create_config('skip_conscription', '跳过征兵继续扫荡', 'checkbox', start4, False, checkboxGroup),
    ]

    return create_option(name, task_type, configs)


def create_chuzheng_options(name, task_type):
    configs = [
        create_config('status', '启动', 'checkbox', start, False, checkboxGroup),
        create_config('lists', '选择编队', 'select', start2, 1, listGroup),
        create_config('delay_time', '延迟时间', 'input', start3, 2),
    ]

    return create_option(name, task_type, configs)


options_config = [
    {
        'groupName': '扫荡',
        'taskType': saodangType,
        'options': [create_saodang_option(f'编队{i + 1}', saodangType) for i in range(5)]
    },
    {
        'groupName': '出征',
        'taskType': chuzhengType,
        'options': [create_chuzheng_options(f'编队{1}', chuzhengType)]
    }
]
