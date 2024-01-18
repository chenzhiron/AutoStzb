from pywebio.output import use_scope,  put_text, toast, put_scope
from pywebio.pin import put_checkbox, pin_on_change, put_input
from modules.task.tasks import taskManager
from datetime import datetime


def changeInit(instance, key):
    def changeArrType(arr, instance=instance, key=key):
        if len(arr) > 0:
            instance.changeConfig(key, True)
        else:
            instance.changeConfig(key, False)

    return changeArrType


def checkInit(min, max):
    def checkNum(x, min=min, max=max):
        if not isinstance(x, (int, float, str)):
            return False
        if min < float(x) < max:
            return True
        else:
            return False

    return checkNum


def changeNum(instance, key, min, max):
    def changeNumType(x, instance=instance, key=key, min=min, max=max):
        if not checkInit(min, max)(x):
            toast('请输入{}到{}之间的数字'.format(min, max), position='right', duration=3)
            return None
        else:
            instance.changeConfig(key, x)

    return changeNumType


class TeamProp:
    def __init__(self, config=None):
        self.state = False
        self.execute_tasks = []
        self.next_run_times = datetime.now()
        self.x = 0
        self.y = 0
        self.count = 0
        self.going = False
        self.team = None
        self.delay_time = 0
        self.speed_time = 0
        self.elapsed_time = 0
        self.skip_conscription = False
        self.skip_battle = False
        self.battle_result = None
        self.battle_await_time = 0
        self.residue_person_ratio = 0.5
        self.residue_enemy_ratio = 0.5
        if config is not None:
            for key, value in config.items():
                setattr(self, key, value)

    def changeConfig(self, key, value):
        setattr(self, key, value)
        self.sortTask()

    def sortTask(self):
        print('sortTask')
        taskManager.addTask(self)
        execute_tasks = []
        if self.skip_conscription:
            execute_tasks.append('zhengbing')
        if self.going:
            execute_tasks.append('chuzheng')
        if self.count > 0:
            execute_tasks.append('saodang')
        self.execute_tasks = execute_tasks

    def render(self):
        with use_scope('center', clear=True):
            put_scope('state',
                      [put_text('状态:'),
                       put_checkbox('state', [{'label': '', 'value': True}], value=[self.state]
                                    )]
                      ).style('display:grid;grid-template-columns:auto auto;')
            put_scope('zhengbing', [
                put_text('征兵'),
                put_checkbox('skip_conscription', [{'label': '', 'value': True}],
                             value=[self.skip_conscription])
            ]).style('display:grid;grid-template-columns:auto auto;')
            put_scope('combat_config', [put_text('平局等待选项'),
                                        put_text('我方剩余兵力比例'),
                                        put_input('residue_person_ratio', value=str(self.residue_person_ratio),
                                                  ),
                                        put_text('敌方剩余兵力比例'),
                                        put_input('residue_enemy_ratio', value=str(self.residue_enemy_ratio),
                                                  )
                                        ])
            put_scope('chuzheng',
                      [put_text('出征'), put_checkbox('going', [{'label': '', 'value': True}], value=[self.going])]
                      ).style('display:grid;grid-template-columns:auto auto;')
            put_scope('saodang', [put_text('扫荡次数'),
                                  put_input('count', type='number', value=str(self.count))]
                      ).style('display:grid;grid-template-columns:auto auto;')

        pin_on_change('state', changeInit(self, 'state'), clear=True)
        pin_on_change('count', changeNum(self, 'count', 1, 100), clear=True)
        pin_on_change('going', changeInit(self, 'going'), clear=True)
        pin_on_change('skip_conscription', changeInit(self, 'skip_conscription'), clear=True)
        pin_on_change('residue_person_ratio', changeNum(self, 'residue_person_ratio', 0, 1), clear=True)
        pin_on_change('residue_enemy_ratio', changeNum(self, 'residue_enemy_ratio', 0, 1), clear=True)
