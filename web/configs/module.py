from config.custom import customConfig
from dispatcher.Dispatcher import task_dispatcher
from modules.tasks import Task
from config.task_or_web_common import *
from web.configs.event import *

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


def create_instance(task_type):
    # 调度器
    if task_type == schedulerType:
        return task_dispatcher
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
        task.add_attribute('skip_conscription', False)
    return task


def create_zhengbing_options(name, task_type):
    configs = [
        create_config('status', '启动', 'checkbox', task_start_saodang, False, checkboxGroup),
        create_config('lists', '选择编队', 'select', change_lists, 1, listGroup),
    ]
    return create_option(name, task_type, configs)


def create_config(name, explain, ctype=None, fn=None, value=None, options=None):
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


def create_saodang_option(name, task_type):
    configs = [
        create_config('status', '启动', 'checkbox', task_start_saodang, False, checkboxGroup),
        create_config('lists', '选择编队', 'select', change_lists, 1, listGroup),
        create_config('circulation', '循环次数', 'input', change_circulation, 1),
        create_config('delay_time', '延迟时间', 'input', change_delay_time, 0),
        create_config('skip_conscription', '跳过征兵继续扫荡', 'checkbox', change_skip_conscription, False,
                      checkboxGroup),
        create_config('explain', '以下2个条件必须都符合才会进入平局等待，否则会执行撤退函数!!!'),
        create_config('explain', '当我方剩余兵力低于该比例时，会执行撤退函数，否则等待 5分钟后下一封战报'),
        create_config('residue_person_ratio', '我方剩余兵力比例, 范围填 0 - 1', 'input', change_residue_person_ratio,
                      0.8),
        create_config('explain', '当土地守军剩余兵力高于该比例时，会执行撤退函数，否则等待 5分钟后下一封战报'),
        create_config('residue_enemy_ratio', '敌人剩余兵力比例, 范围填 0 - 1', 'input', change_residue_enemy_ratio,
                      0.8),
    ]

    return create_option(name, task_type, configs)


def create_chuzheng_options(name, task_type):
    configs = [
        create_config('status', '启动---说明：从第四个标记，将所有需要出征的土地标记', 'checkbox', task_start_chuzheng,
                      False, checkboxGroup),
        create_config('lists', '选择编队', 'select', change_lists, 1, listGroup),
        create_config('delay_time', '延迟时间', 'input', change_delay_time, 2),
        create_config('explain', '以下2个条件必须都符合才会进入平局等待，否则会执行撤退函数!!!'),
        create_config('explain', '当我方剩余兵力低于该比例时，会执行撤退函数，否则等待 5分钟后下一封战报'),
        create_config('residue_person_ratio', '我方剩余兵力比例, 范围填 0 - 1', 'input', change_residue_person_ratio,
                      0.8),
        create_config('explain', '当土地守军剩余兵力高于该比例时，会执行撤退函数，否则等待 5分钟后下一封战报'),
        create_config('residue_enemy_ratio', '敌人剩余兵力比例, 范围填 0 - 1', 'input', change_residue_enemy_ratio,
                      0.8),
    ]

    return create_option(name, task_type, configs)


def create_wotu_options(name, task_type):
    configs = [
        create_config('status', '启动--------说明：标记为第三个标记', 'checkbox', task_start_wotu, False, checkboxGroup),
        create_config('lists', '选择编队', 'select', change_lists, 1, listGroup),
        create_config('delay_time', '延迟时间', 'input', change_delay_time, 2),
    ]

    return create_option(name, task_type, configs)


def create_chengpi_options(name, task_type):
    configs = [
        create_config('status', '启动--------说明：标记为第二个标记', 'checkbox', task_start_chengpi, False,
                      checkboxGroup),
        create_config('lists', '选择编队', 'select', change_lists, 1, listGroup),
        create_config('delay_time', '延迟时间', 'input', change_delay_time, 2),
        create_config('explain', '以下2个条件必须都符合才会进入平局等待，否则会执行撤退函数!!!'),
        create_config('explain', '当我方剩余兵力低于该比例时，会执行撤退函数，否则等待 5分钟后下一封战报'),
        create_config('residue_person_ratio', '我方剩余兵力比例, 范围填 0 - 1', 'input', change_residue_person_ratio,
                      0.8),
        create_config('explain', '当土地守军剩余兵力高于该比例时，会执行撤退函数，否则等待 5分钟后下一封战报'),
        create_config('residue_enemy_ratio', '敌人剩余兵力比例, 范围填 0 - 1', 'input', change_residue_enemy_ratio,
                      0.8),
    ]

    return create_option(name, task_type, configs)


def create_config_options(name, task_type):
    configs = [
        create_config('time_sleep', '截图延迟时间，单位 秒', 'input', change_time_sleep, 1),
    ]

    return create_option(name, task_type, configs)


def create_option(name, task_type, configs):
    return {
        'name': name,
        'config': [config for config in configs],
        'instance': create_instance(task_type)
    }


def create_scheduler_options(name, task_type):
    configs = [
        create_config('status', '状态', 'checkbox', task_start_scheduler, False, checkboxGroup),
    ]

    return create_option(name, task_type, configs)


options_config = [
    {
        'groupName': '调度器',
        'taskType': schedulerType,
        'options': [create_scheduler_options('调度器', schedulerType)]

    },
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
        'options': [create_chuzheng_options(f'编队{1}', chuzhengType),
                    create_chengpi_options('城皮', chengpiType),
                    create_wotu_options('沃土', wotuType)]
    }
]
