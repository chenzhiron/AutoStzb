from modules.taskConfigStorage.main import ConfigStorage


class Task:
    def __init__(self, storage, steps):
        self.status = True
        self.storage = storage
        self.steps = steps


if __name__ == '__main__':
    task1 = ConfigStorage()
    task = Task(task1, [1, 2, 3, 4])
    print(task.steps)
    task.storage.change_config_storage_by_key('type', 1)
    print(task.storage.type)