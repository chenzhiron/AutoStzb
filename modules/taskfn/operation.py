from modules.devices.main import Devices
from modules.taskfn.tasks_utils import BaseReturnMain


class Operation(BaseReturnMain):
    def __init__(self, device: Devices, config={}, db=None):
        super().__init__(device)
        self.config = config

    def execute(self):
        pass


if __name__=='__main__':
    d = Devices('127.0.0.1:16384')
    operation = Operation(d)
    operation.execute()
