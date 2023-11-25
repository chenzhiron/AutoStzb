from functools import partial
import copy
import pywebio.pin as pin
from config.custom import customConfig
from modules.taskConfigStorage.main import init_config_storage_by_key, change_config_storage_by_key
from pywebio import start_server
from pywebio.output import put_row, put_column, put_code, put_collapse, put_button, put_text, put_scope, use_scope
from pywebio import session

from config.const import web_port
from dispatcher.main import sc_cron_add_jobs, start_scheduler

zhengbing_list = ['征兵一', '征兵二', '征兵三']
saodang_list = ['扫荡一', '扫荡二', '扫荡三', '扫荡四', '扫荡五']
chuzheng_list = ['出征']

options = [
    {
        "label": "",
        "value": True
    },
]
options_list = [
    {
        'label': 1,
        'value': 1,
    },
    {
        'label': 2,
        'value': 2,
    },
    {
        'label': 3,
        'value': 3
    },
    {
        'label': 4,
        'value': 4
    },
    {
        'label': 5,
        'value': 5
    },
]
enhance = [
    {
        "label": "",
        "value": True,
    },
]

current_options = ''
current_index = 0

# 预备执行的任务
task_list = []


# 队列
def get_task():
    while True:
        if len(task_list) > 0:
            return task_list.pop(0)


# 调度器添加任务
def add_scheduler_job(event):
    # 这是个 [True] 或者 []
    checkbox_inline = event
    if len(checkbox_inline) > 0:
        going_list = pin.pin['select_list']
        repetition_number = pin.pin['repetition_number']
        checkbox_enhance = pin.pin['checkbox_enhance'][0] if bool(pin.pin['checkbox_enhance']) else False
        delay_time = pin.pin['delay_time']
        checkbox_enhance_city_inline = pin.pin['checkbox_enhance_city_inline'][0] if bool(
            pin.pin['checkbox_enhance_city_inline']) else False

        executefn = None
        if current_options == '扫荡':
            if bool(checkbox_enhance):
                executefn = copy.deepcopy(mopping_up) * repetition_number
            else:
                executefn = copy.deepcopy(mopping_up_fast) * repetition_number
        elif current_options == '征兵':
            executefn = copy.deepcopy(conscription)
        elif current_options == '出征':
            executefn = copy.deepcopy(conquer) * 2
        try:
            if float(delay_time) < 0:
                delay_time = 0
        except:
            delay_time = 0
        task_fn = {'name': current_options + str(current_index),
                   'args': [going_list, checkbox_enhance, float(delay_time), checkbox_enhance_city_inline],
                   'fn': executefn
                   }
        task_list.append(task_fn)


# 调度器启动
def start():
    start_scheduler()
    while True:
        task = get_task()
        task_name = task['name']
        task_fn = task['fn'].pop(0)
        # 初始化存储
        init_config_storage_by_key(task_name)
        if '扫荡' in task_name:
            change_config_storage_by_key(task_name, 'txt', '扫荡')
        elif '出征' in task_name:
            change_config_storage_by_key(task_name, 'txt', '出证')
        # 初始化 队伍
        change_config_storage_by_key(task_name, 'lists', task['args'][0])
        change_config_storage_by_key(task_name, 'checkbox_enhance', task['args'][1])
        change_config_storage_by_key(task_name, 'delay_time', task['args'][2])
        if task['args'][3]:
            change_config_storage_by_key(task_name, 'txt', '出证')
        # 设置队列任务
        set_task_all(task_name, task['fn'])
        # 添加执行任务
        sc_cron_add_jobs(task_fn, [task_name], task_name, 1)


# 不同页面展示不同选项
def apply(info):
    current_name = current_options + str(current_index)
    start_txt = '启动'
    going_list = '选择编队'
    going_list_number = '次数'
    checkbox_enhance = '扫荡后默认自动征兵' if info == '扫荡' else '当资源不够一次性征兵时，打开此选项'
    delay_time_txt = '队伍延迟出发时间,单位 秒, 基于城皮/沃土扫荡时注意耐久度'
    checkbox_enhance_city = '沃土/城皮 模式' if info == '扫荡' else ''
    inline = False
    select_list = 1
    repetition_number = 1
    checkbox_enhance_inline = True if info == '扫荡' else False
    checkbox_enhance_city_inline = False
    delay_time = 0

    if len(task_list) > 0:
        for em in task_list:
            if em['name'] == current_name:
                inline = True
                select_list = em['args'][0]
                repetition_number = em['args'][1]
                checkbox_enhance_inline = em['args'][2]
                delay_time = em['args'][3]
                break

    put_row([
        put_column([
            put_text(start_txt),
            put_text(going_list),
            put_text(going_list_number) if info == '扫荡' else None,
            put_text(checkbox_enhance),
            put_text(delay_time_txt),
            put_text(checkbox_enhance_city)
        ]),
        put_column([
            pin.put_checkbox('checkbox_inline', options=options, value=inline),
            pin.put_select('select_list', options=options_list, value=select_list),
            pin.put_input('repetition_number', value=repetition_number, type='number', ) if info == '扫荡' else None,
            pin.put_checkbox('checkbox_enhance', options=enhance, value=bool(checkbox_enhance_inline)),
            pin.put_input('delay_time', value=delay_time, type='number'),
            pin.put_checkbox('checkbox_enhance_city_inline', options=enhance,
                             value=bool(checkbox_enhance_city_inline)) if info == '扫荡' else None
        ])
    ])
    pin.pin_on_change('checkbox_inline', onchange=add_scheduler_job, clear=True)


# 切换页面
def cut(info, index):
    global current_index, current_options
    current_options = info
    current_index = index
    with use_scope('center', clear=True, create_scope=True):
        apply(current_options)


def render_sleep():
    start_txt = '操作统计延迟'
    change_sleep_time = customConfig.getTimesleep()()
    put_row([
        put_column([
            put_text(start_txt),
            put_text('请注意，延迟不能小于等于0, 单位 秒')
        ]),
        put_column([
            pin.put_input('change_sleep_time', value=change_sleep_time, type='number')
        ])
    ])
    pin.pin_on_change('change_sleep_time', onchange=customConfig.changeTimesleep, clear=True)


change_list = ['操作延迟']


def change_sleep(info, index):
    global current_index, current_options
    current_options = info
    current_index = index
    with use_scope('center', clear=True, create_scope=True):
        render_sleep()


# 渲染函数
def render_button(lists, l, cutfn):
    button_list = []
    for i, info in enumerate(lists):
        onclick = partial(cutfn, info=info[:l], index=i + 1)
        button_list.append(put_button(info, onclick=onclick))
    return button_list


# 初始化函数
def init():
    js_code = """
    document.querySelector('footer').style.display = 'none';
    document.body.style.overflow = 'hidden';
    """
    session.run_js(js_code)
    put_row([
        put_column([
            put_button('启动', onclick=start),
            put_collapse('配置', render_button(change_list, 2, change_sleep)),
            put_collapse('征兵', render_button(zhengbing_list, 2, cut)),
            put_collapse('扫荡', render_button(saodang_list, 2, cut)),
            put_collapse('出征', render_button(chuzheng_list, 2, cut)),
            None,
        ]).style('display: block;'),
        put_scope('center', put_column([
            None,
            None,
        ])),
        put_code('日志'),
    ], size='20% 50% 30%')


# 启动web
def start_web(web_port=web_port):
    start_server(init, port=web_port)


# if __name__ == '__main__':
#     start_web(18878)
