import time

from dispatcher.Dispatcher import task_dispatcher


# from modules.taskGroup.taskGroup import handle_in_map_conscription, handle_in_lists_action, handle_in_battle_result, \
#     handle_in_unmark

def a(self):
    print('a', self.__dict__, '\n')
    return self


def b(self):
    print('b', '\n')
    return self


def c(self):
    print('c', '\n')
    return self


def d(self):
    print('d', '\n')
    return self


class Task:
    dispatcher = task_dispatcher

    def __init__(self, t, circulation):
        if t == 1:
            self.task_group = [a]
        elif t == 2:
            self.task_group = [b, c, a]
        else:
            self.task_group = []
        self.circulation = circulation
        self.setup = 0
        self.delay_time = 1
        self.offset = 0
        self.status = True
        self.result = None
        self.times = None
        self.lists = None
        self.txt = None
        self.battle_result = None

    def change_config_storage_by_key(self, key, value):
        setattr(self, key, value)
        return getattr(self, key)

    def next_start(self):
        if self.circulation > 0 and self.status:
            self.dispatcher.sc_cron_add_jobs(self.task_group[self.setup], [self], self.delay_time)
            self.change_config_storage_by_key('setup', self.setup + 1)
            self.change_config_storage_by_key('circulation', self.circulation - 1)

    def next_task(self):
        if len(self.task_group) > self.setup and self.status:
            self.dispatcher.sc_cron_add_jobs(self.task_group[self.setup], [self], self.delay_time)
            self.change_config_storage_by_key('setup', self.setup + 1)
        else:
            self.change_config_storage_by_key('setup', 0)
            self.next_start()


if __name__ == '__main__':
    task1 = Task(2, 2)
    task1.next_start()

    task2 = Task(1, 1)
    task2.next_start()
    while 1:
        pass
