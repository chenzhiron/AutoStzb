from modules.task.Class.OperatorSteps import SwipeOperatorSteps
from modules.general.module_options_name import require_zhengbing
from modules.general.option_verify_area import zhengbing_page_swipe_verify, zhengbing_page_swipe

swipe_zhengbing = SwipeOperatorSteps(zhengbing_page_swipe_verify, [require_zhengbing],
                                     zhengbing_page_swipe)
