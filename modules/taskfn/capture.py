from modules.devices.main import DeviceOperator, DeviceManager
from modules.static.config_keys import PracticeLandKeys
from modules.taskfn.basic import Basic
from modules.taskfn.steps import EntryListPage, SearchMap, OperationGoMap, ListActionResult, SelectListAction
from modules.taskfn.tasks_utils import add_seconds_to_time


class Capture(Basic):
    def __init__(self, operator, config):
        super().__init__(operator, config)
        self.draft = EntryListPage(operator, config)
        self.search_map = SearchMap(operator, config)
        self.go_map = OperationGoMap(operator, config)
        self.list_action = SelectListAction(operator, config)
        self.action_result = ListActionResult(operator, config)
    def run(self):
        if self.config[PracticeLandKeys.STAGE] == 0:
            if self.config[PracticeLandKeys.DRAFT]:
                draft_result = self.draft.run()
                if draft_result['time_consuming'] != 0:
                    self.result[PracticeLandKeys.NEXTTIME] = add_seconds_to_time(
                        self.config[PracticeLandKeys.NEXTTIME],
                        draft_result['time_consuming']
                    )
                    return self.result

            # 共用逻辑（DRAFT.time_consuming=0 或 无 DRAFT）
            self.search_map.run()
            self.go_map.run()
            action_result = self.list_action()
            self.result.update(action_result)
            self.result[PracticeLandKeys.STAGE] = 1
            self.result[PracticeLandKeys.NEXTTIME] = add_seconds_to_time(
                self.config[PracticeLandKeys.NEXTTIME],
                action_result['time_consuming']
            )
            return self.result
        elif self.config[PracticeLandKeys.STAGE] == 1:
            return self.action_result
        return None








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