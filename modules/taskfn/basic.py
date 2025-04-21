from modules.devices.main import Devices


class Basic:
    def __init__(self, device: Devices, config=None, db=None):
        if config is None:
            config = {}
        self.device = device
        self.config = config
        self.result = {}
        self.db = db


class OperationAction(Basic):
    def execute(self):
        pass

class SearchMap(Basic):
    def execute(self):
        pass