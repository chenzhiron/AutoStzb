class TaskManager:
    def __init__(self):
        self.padding = []

    def addTask(self, instance):
        if instance not in self.padding and instance.state:
            self.padding.append(instance)
        self.sortTask()

    def sortTask(self):
        print('sortTask ---TaskManager')
        self.padding.sort(key=lambda x: (not x.state, x.next_run_times))

    def get_tasks(self):
        print('get_tasks')
        if len(self.padding) > 0 and self.padding[0].state:
            return self.padding.pop(0)
        return None


taskManager = TaskManager()
