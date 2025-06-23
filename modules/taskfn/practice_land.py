import time
from datetime import datetime
from pprint import pprint

from modules.devices.main import DeviceOperator, DeviceManager
from modules.taskfn.capture import Capture
from modules.taskfn.steps import OperationGoMap


class PracticeLand(Capture):
    def __init__(self, operator, config):
        super().__init__(operator, config)
        # 需要重写 扫荡
        self.go_map = OperationGoMap(operator, config)


if __name__ == '__main__':
    list_config = {
        "state": True,
        "address": "",
        "stage": 0,
        "draft": False,
        "nexttime": "2025/05/22 00:00:00",
        "x": 642,
        "y": 969,
        "num": 5,
        "action_list": 5,
        "max_distance": 300,
        "time_consuming": 0,
        "my_remaining": 30000,
        "enemy_remaining": 30000,
    }
    device = DeviceOperator(DeviceManager('127.0.0.1:16384'))
    while list_config['state']:
        if datetime.now() > datetime.strptime(list_config['nexttime'], "%Y/%m/%d %H:%M:%S"):
            result = capture = Capture(operator=device, config=list_config).run()
            list_config.update(result)
            pprint(result)
            pprint(list_config)
        time.sleep(1)
    # capture.return_main()
