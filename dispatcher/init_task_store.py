from collections.abc import MutableSequence

from dispatcher.watch_task import execute_task_list


class ObservableList(MutableSequence):
    def __init__(self, *args):
        self._list = list(args)
        self._observers = []

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = value
        self._notify_observers()

    def __delitem__(self, index):
        del self._list[index]
        self._notify_observers()

    def __len__(self):
        return len(self._list)

    def insert(self, index, value):
        self._list.insert(index, value)
        self._notify_observers()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self._list)


class ArrayObserver:
    def update(self, array):
        print('array'+str(array))
        if len(array) == 0:
            return
        execute_task_list(array)


observable_list = ObservableList()


def init_task_store():
    # 示例用法
    observer = ArrayObserver()
    observable_list.add_observer(observer)


def return_task_store():
    return observable_list


def append_task_store(task_config):
    observable_list.append(task_config)


def remove_task_store(i):
    observable_list.remove(i)


def clear_task_store():
    observable_list.clear()


init_task_store()
