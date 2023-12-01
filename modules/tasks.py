from dispatcher.Dispatcher import task_dispatcher
from modules.taskGroup import handle_in_map_conscription, handle_in_lists_action, handle_in_battle_result, \
    handle_in_unmark, handle_in_draw_battle
from config.task_or_web_common import saodangType, chuzhengType, zhengbingType, wotuType, chengpiType


# def a(instance):
#     print(instance.setup)
#     print('征兵')
#     return instance
#
#
# def b(instance):
#     print(instance.setup)
#     print('扫荡')
#     return instance
#
#
# def c(instance):
#     print(instance.setup)
#     print('出征')
#     return instance


# def e(instance):
#     print(instance.setup)
#     person_num = instance.battle_result['person_number'].split('/')
#     enemy_num = instance.battle_result['enemy_number'].split('/')
#     person_result = int(person_num[0]) > int(person_num[1]) * instance.residue_person_ratio
#     enemy_result = int(enemy_num[0]) < int(enemy_num[1]) * instance.residue_enemy_ratio
#     print(person_result, 'person_result')
#     print(enemy_result, 'enemy_result')
#     if person_result and enemy_result:
#         instance.setup = instance.setup - 1
#         instance.battle_time = 15
#         print('等待')
#     else:
#         print('不变化')
#     print('统计')
#     return instance


# def f(instance):
#     print(instance.setup)
#     print('撤退')
#     return instance
#
#
# def g(instance):
#     print(instance.setup)
#     print('取消标记')
#     return instance


class Task:
    dispatcher = task_dispatcher

    @classmethod
    def set_task_group(cls, t):
        if t == zhengbingType:
            return [handle_in_map_conscription]
        elif t == saodangType:
            return [handle_in_lists_action, handle_in_battle_result, handle_in_draw_battle,
                    handle_in_map_conscription]
        elif t == chuzhengType:
            return [handle_in_lists_action, handle_in_battle_result, handle_in_draw_battle,
                    handle_in_map_conscription, handle_in_unmark]
        elif t == wotuType or t == chengpiType:
            return [handle_in_lists_action, handle_in_battle_result, handle_in_draw_battle,
                    handle_in_map_conscription]
        else:
            return []
        #
        # if t == zhengbingType:
        #     return [a]
        # elif t == saodangType:
        #     return [b, e, f]
        # elif t == chuzhengType:
        #     return [c, e, f, g]
        # elif t == wotuType or t == chengpiType:
        #     return [c, e, f]
        # else:
        #     return []

    def __init__(self, t, circulation=1):
        self.task_group = self.set_task_group(t)
        self.type = t
        self.circulation = circulation
        self.setup = 0
        self.delay_time = 0
        self.offset = 0
        self.speed_time = 0
        self.next_times = 0
        self.status = False
        self.lists = 1
        self.txt = None
        # self.battle_result = {
        #     'status': '平局',
        #     'person_number': '4001/8000',
        #     'enemy_number': '3999/8000',
        # }
        self.battle_result = {}
        self.residue_person_ratio = 0.5
        self.residue_enemy_ratio = 0.5
        self.battle_time = 0

    def add_attribute(self, key, value):
        setattr(self, key, value)

    def change_config_storage_by_key(self, key, value):
        setattr(self, key, value)
        return getattr(self, key)

    def next_start(self):
        if self.circulation > 0 and self.status:
            self.change_config_storage_by_key('setup', 0)
            next_time = max(self.delay_time, self.next_times)

            self.dispatcher.sc_cron_add_jobs(self.task_group[self.setup], [self], next_time)
            self.change_config_storage_by_key('setup', self.setup + 1)
            self.change_config_storage_by_key('circulation', self.circulation - 1)
        elif self.circulation == 0:
            self.status = False
        return None

    def next_task(self):
        if len(self.task_group) > self.setup and self.status:
            next_time = self.next_times
            # 平局倒计时 5分钟
            if self.battle_time != 0:
                next_time = self.battle_time
            self.dispatcher.sc_cron_add_jobs(self.task_group[self.setup], [self], next_time)
            self.change_config_storage_by_key('setup', self.setup + 1)
        else:
            self.next_start()
#
# if __name__ == '__main__':
#     task1 = Task(2, 2)
#     task1.next_start()
#
#     task2 = Task(1, 1)
#     task2.next_start()
#     while 1:
#         pass
