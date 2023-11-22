config_storage = {}

property_list = ['type', 'status', 'result', 'times', 'lists', 'txt', 'offset', 'battle_result', 'delay_time', 'checkbox_enhance']


def create_config_storage():
    storage = {}
    for i in property_list:
        if i == 'battle_result':
            storage[i] = {}
            continue
        elif i == 'result':
            storage[i] = None
            continue
        storage[i] = 0
    return storage


def change_config_storage_by_key(taskid, key, value):
    config_storage[taskid][key] = value
    return config_storage[taskid]


def update_config_storage(taskid, value):
    config_storage[taskid].update(value)
    return config_storage[taskid]


def get_config_storage():
    return config_storage


def get_config_storage_by_key(key):
    return config_storage[key]


def get_config_storage_by_key_value(taskid, key):
    return config_storage[taskid][key]


def init_config_storage_by_key(key):
    config_storage[key] = create_config_storage()
    return config_storage[key]


def clear_config_storage_by_key(key):
    config_storage[key] = {}


def clear_config_storage():
    global config_storage
    config_storage = {}
    return config_storage


class ConfigStorage:
    def __init__(self):
        self.type = None
        self.status = None
        self.result = None
        self.times = None
        self.lists = None
        self.txt = None
        self.offset = None
        self.battle_result = None
        self.delay_time = None
        self.checkbox_enhance = None

    def change_config_storage_by_key(self, key, value):
        setattr(self, key, value)
        return getattr(self, key)

    def get_config_storage_by_key(self, key):
        return getattr(self, key)
