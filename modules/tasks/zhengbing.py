from modules.module_zhengbing.module_zhengbing import module_zhengbing_list_click, module_swipe_zhengbing_page, \
    module_zhengbing_page_click, module_computed_time, module_require_zhengbing, module_require_next_click, \
    module_return_page, module_return_next_page
from modules.module_shili.module_shili import module_click_shili


# 处理 添加征兵队列1个|2个|3个的阻塞拦截
def zhengbing(i):
    module_click_shili()
    module_zhengbing_list_click(i)
    module_zhengbing_page_click()
    module_swipe_zhengbing_page()
    result = module_computed_time()
    module_require_zhengbing()
    module_require_next_click()
    module_return_page()
    module_return_next_page()
    return {
        'type': 1,
        'result': result
    }
# if __name__ == '__main__':
#     connect_device()
#     result = zhengbing(3)
#     print(result)
