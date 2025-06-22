from modules.static.config_keys import PracticeLandKeys
from modules.taskfn.basic import Basic
from modules.taskfn.capture import Capture
from modules.taskfn.steps import EntryListPage, SearchMap, OperationGoMap, ListActionResult, SelectListAction
from modules.taskfn.tasks_utils import get_future_time


class PracticeLand(Basic):
     def __init__(self, operator, config):
        super().__init__(operator, config)
        self.draft = EntryListPage(operator, config)
        self.search_map = SearchMap(operator, config)
        self.go_map = OperationGoMap(operator, config)
        self.list_action = SelectListAction(operator, config)
        self.action_res = ListActionResult(operator, config)

     def run(self):
        if self.config[PracticeLandKeys.STAGE] == 0:
            if self.config[PracticeLandKeys.DRAFT]:
                draft_result = self.draft.run()
                if draft_result['time_consuming'] != 0:
                    self.result[PracticeLandKeys.NEXTTIME] = get_future_time(draft_result['time_consuming'])
                    return self.result
            # 共用逻辑（DRAFT.time_consuming=0 或 无 DRAFT）
            self.search_map.run()
            self.go_map.run()
            list_res = self.list_action.run()
            self.result.update(list_res)
            self.result[PracticeLandKeys.STAGE] = 1
            self.result[PracticeLandKeys.NEXTTIME] = get_future_time(list_res['time_consuming'])

        elif self.config[PracticeLandKeys.STAGE] == 1:
            action_result = self.action_res.run()
            print('action_result:::', action_result)
            if action_result == 1:
                # 等待
                self.result[PracticeLandKeys.NEXTTIME] = get_future_time(300)
            else:
                self.result[PracticeLandKeys.NEXTTIME] = get_future_time(
                    self.config[PracticeLandKeys.TIME_CONSUMING]
                )
                self.result[PracticeLandKeys.STAGE] = 2

        elif self.config[PracticeLandKeys.STAGE] == 2:
            if self.config[PracticeLandKeys.DRAFT]:
                draft_result = self.draft.run()
                if draft_result['time_consuming'] != 0:
                    self.result[PracticeLandKeys.NEXTTIME] = get_future_time(draft_result['time_consuming'])
            self.result[PracticeLandKeys.STATE] = False

        return self.result
