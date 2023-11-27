from modules.tasks import Task

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
    print(instance, '11111-----', v)


def start2(v, instance):
    instance.change_config_storage_by_key('lists', int(v))
    print(' 222- --- instance', instance)


def start3(v, instance):
    instance.change_config_storage_by_key('delay_time', int(v) if int(v) > 0 else 0)
    print('3333----- instance', instance)


def start4(v, instance):
    print('4444-----', v)


def create_option(name, task_type):
    return {
        'name': name,
        'config': [
            {
                'value': False,
                'explain': '启动',
                'type': 'checkbox',
                'options': checkboxGroup,
                'fn': start,
                'name': 'status'
            },
            {
                'value': 1,
                'explain': '选择编队',
                'type': 'select',
                'options': listGroup,
                'fn': start2,
                'name': 'lists'
            },
            {
                'value': 2,
                'explain': '延迟时间',
                'type': 'input',
                'fn': start3,
                'name': 'delay_time'
            }
        ],
        'instance': Task(task_type),
    }


options_config = [
    {
        'groupName': '扫荡',
        'taskType': 2,
        'options': [create_option(f'编队{i + 1}', 2) for i in range(5)]
    }
]
