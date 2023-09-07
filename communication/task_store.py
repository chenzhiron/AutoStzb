store = {}


def add_store_data(task_id, value):
    store[task_id] = value


def get_store_data(task_id):
    return store[task_id]


def change_store_data_value(task_id, key, value):
    store[task_id][key] = value


def get_store_data_value(task_id, key):
    return store[task_id][key]


def del_store_data(task_id):
    del store[task_id]
