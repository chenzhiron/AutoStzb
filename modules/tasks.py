from dispatcher.Dispatcher import task_dispatcher


# from modules.taskGroup.taskGroup import handle_in_map_conscription, handle_in_lists_action, handle_in_battle_result, \
#     handle_in_unmark

def a(self):
    print(self, 'a')
    return self


def b(self):
    print(self, 'b')
    return self


def c(self):
    print(self, 'c')
    return self


def d(self):
    print(self, 'd')
    return self


class Task:
    dispatcher = task_dispatcher

    def zhengBing(self):
        # return handle_in_map_conscription
        return a

    def listsActive(self):
        # return handle_in_lists_action
        return b

    def battleResult(self):
        # return handle_in_battle_result
        return c

    def unmark(self):
        # return handle_in_unmark
        return d

    def __init__(self, taskid, t, circulation):
        if t == 1:
            self.task_group = [self.zhengBing()]
        elif t == 2:
            self.task_group = [self.listsActive(), self.battleResult(), self.zhengBing()]
        else:
            self.task_group = []
        self.circulation = circulation
        self.taskid = taskid
        self.setup = 0
        self.delay_time = 1
        self.type = None
        self.status = None
        self.result = None
        self.times = None
        self.lists = None
        self.txt = None
        self.offset = None
        self.battle_result = None
        self.checkbox_enhance = None

    def change_config_storage_by_key(self, key, value):
        setattr(self, key, value)
        return getattr(self, key)

    def next_start(self):
        if self.circulation > 0:
            self.change_config_storage_by_key('setup', 0)
            print('setup', self.setup)
            self.dispatcher.sc_cron_add_jobs(self.task_group[self.setup], [self], self.taskid, self.delay_time)
            self.change_config_storage_by_key('setup', 1)

    def next_task(self):
        if len(self.task_group) > self.setup:
            print('setup', self.setup)
            self.dispatcher.sc_cron_add_jobs(self.task_group[self.setup], [self], self.taskid, self.delay_time)
            self.change_config_storage_by_key('setup', self.setup + 1)
        else:
            self.change_config_storage_by_key('circulation', self.circulation - 1)
            self.next_start()


if __name__ == '__main__':
    task1 = Task('abd', 2, 2)
    task1.next_start()
    while 1:
        pass
