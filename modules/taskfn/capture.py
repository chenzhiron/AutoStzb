import logging
import time

from modules.devices.main import DeviceOperator, DeviceManager
from modules.taskfn.basic import Basic
from modules.taskfn.state_enum import State
from modules.taskfn.steps import EntryListPage, SearchMap, OperationGoMap, ListActionResult, SelectListAction
from modules.taskfn.steps_basic import StepsBasic



class Capture(Basic):
    def __init__(self, operator, config):
        super().__init__(operator, config)
        self.steps_basic = StepsBasic(operator)
        self.map_x = 0
        self.map_y = 0
        self.time_sleep = 0

        self.current_state = State.INIT
        self.state_handlers = {
            State.DRAFT: EntryListPage(operator, config),
            State.SEARCH_MAP: SearchMap(operator, config),
            State.GO_MAP: OperationGoMap(operator, config),
            State.LIST_ACTION: SelectListAction(operator, config),
            State.RESULT: ListActionResult(operator, config),
        }
    def init_state(self):
        # 校验当前状态。


        if self.config['draft']:
            self.current_state = State.DRAFT

    def run(self):
        self.init_state()
        while State(self.current_state) == State.END:
            handle = self.state_handlers.get(self.current_state)
            res = handle.run()
            if State(res) == State.END:
                 # 征兵结束
                pass


if __name__ == '__main__':
    capture = Capture(operator=DeviceOperator(DeviceManager('127.0.0.1:16384')),
                      config={"address": "",
                              "x": 646,
                              "y": 966,
                              "num": 3,
                              "action_list": 3,
                              "max_distance": 300,
                              "time_consuming": 0,
                              "my_remaining": 30000,
                              "enemy_remaining": 30000,
                              })
    # capture.execute()
    capture.return_main()