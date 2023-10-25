import queue
import time
from functools import partial

import pywebio.pin as pin
from pywebio import start_server
from pywebio.output import put_row, put_column, put_code, put_collapse, put_button, put_text, put_scope, use_scope, \
    put_info

from dispatcher.main import sc_cron_add_jobs, start_scheduler
from dispatcher.status import set_status, get_status
from modules.utils.main import get_current_date


# from modules.tasks import saodang, zhengbing


def get_task():
    while True:
        print('等待task')
        task = task_queue.get()
        print('拿到task')
        if task['name'] in current_expire_queue:
            continue
        else:
            return task


zhengbing_list = ['征兵一', '征兵二', '征兵三']
saodang_list = ['扫荡一', '扫荡二', '扫荡三', '扫荡四', '扫荡五']

current_options = ''
current_index = 0

# 准备执行的队列
task_queue = queue.Queue()
# 预备执行的任务
task_list = []
# 已取消的任务
current_expire_queue = []


def demo1(*args):
    time.sleep(5)
    print(*args)
    time.sleep(5)


def demo2(*args):
    time.sleep(5)
    print(*args)
    time.sleep(5)


def add_scheduler_job(event):
    checkbox_inline = event
    if len(checkbox_inline) > 0:
        going_list = pin.pin['select_list']
        repetition_number = pin.pin['repetition_number']
        checkbox_enhance = pin.pin['checkbox_enhance'][0] if bool(pin.pin['checkbox_enhance']) else False

        task_fn = {
            'name': current_options + str(current_index),
            'fn': demo1 if current_options == '扫荡' else demo2,
            'args': [going_list, repetition_number, checkbox_enhance]
        }
        task_list.append(task_fn)
        task_queue.put(task_fn)

        for em in current_expire_queue:
            if em == current_options + str(current_index):
                current_expire_queue.remove(em)
                break
    else:
        for em in task_list:
            if em['name'] == (current_options + str(current_index)):
                task_list.remove(em)
                break
        current_expire_queue.append(current_options + str(current_index))


def start():
    start_scheduler()
    while True:
        task = get_task()
        date = get_current_date()
        sc_cron_add_jobs(task['fn'], task['args'], date['year'], date['month'], date['day'], date['hour'],
                         date['minute'], date['second'] + 1)
        set_status(False)
        while True:
            if get_status():
                break


def render_button(lists, l):
    button_list = []
    for i, info in enumerate(lists):
        onclick = partial(cut, info=info[:l], index=i + 1)
        button_list.append(put_button(info, onclick=onclick))
    return button_list


def init():
    put_info("请先配置选项，再点击启动"),
    put_row([
        put_column([
            put_button('启动', onclick=start),
            put_collapse('征兵', render_button(zhengbing_list, 2)),
            put_collapse('扫荡', render_button(saodang_list, 2)),
            None,
        ]).style('display: block;'),
        put_scope('center', put_column([
            None,
            None,
        ])),
        put_code('日志'),
    ], size='20% 50% 30%')


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


def apply(info):
    current_name = current_options + str(current_index)
    start_txt = '启动'
    going_list = '选择编队'
    going_list_number = '次数'
    checkbox_enhance = '扫荡后默认自动征兵' if info == '扫荡' else '当资源不够一次性征兵时，打开此选项'

    inline = False
    select_list = 1
    repetition_number = 1
    checkbox_enhance_inline = True if info == '扫荡' else False

    if len(task_list) > 0:
        for em in task_list:
            if em['name'] == current_name:
                inline = True
                select_list = em['args'][0]
                repetition_number = em['args'][1]
                checkbox_enhance_inline = em['args'][2]
                break

    put_row([
        put_column([
            put_text(start_txt),
            put_text(going_list),
            put_text(going_list_number) if info == '扫荡' else None,
            put_text(checkbox_enhance),
        ]),
        put_column([
            pin.put_checkbox('checkbox_inline', options=options, value=inline),
            pin.put_select('select_list', options=options_list, value=select_list),
            pin.put_input('repetition_number', value=repetition_number, type='number', ) if info == '扫荡' else None,
            pin.put_checkbox('checkbox_enhance', options=enhance, value=bool(checkbox_enhance_inline)),
        ])
    ])
    pin.pin_on_change('checkbox_inline', onchange=add_scheduler_job, clear=True)


def cut(info, index):
    global current_index, current_options
    current_options = info
    current_index = index
    with use_scope('center', clear=True, create_scope=True):
        apply(current_options)


if __name__ == '__main__':
    start_server(init, 12395)
