from modules.taskfn.basic import Basic
from modules.taskfn.steps.draft import Draft
from modules.taskfn.steps.operator_action import OperationGoMap
from modules.taskfn.steps.search_map import SearchMap
from modules.taskfn.steps.select_list_action import OperationListAction


class Capture(Basic, Draft, SearchMap, OperationGoMap, OperationListAction):
    def __init__(self, operator, config):
        super().__init__(operator, config)
        self.steps_fn = [self.execute_draft, self.execute_search_map, self.execute_operation_go_map, self.execute_list_action]

    def execute(self):
        pass
