import pywebio.pin as pin
from pywebio import start_server

from modules.utils.main import get_current_date

from dispatcher.execute_job import sc_cron_add_jobs, start_scheduler
from modules.tasks.zhengbing import zhengbing

checkbox_name = ('zhengbing1', 'zhengbing2', 'zhengbing3', 'zhengbing4', 'zhengbing5',
                 'saodang1', 'saodang2', 'saodang3', 'saodang4', 'saodang5')


def bmi():
    pin.put_checkbox(checkbox_name[0], label='征兵第一编队', options=['True'])
    pin.put_checkbox(checkbox_name[1], label='征兵第二编队', options=['True'])
    pin.put_checkbox(checkbox_name[2], label='征兵第三编队', options=['True'])
    pin.put_checkbox(checkbox_name[3], label='征兵第四编队', options=['True'])
    pin.put_checkbox(checkbox_name[4], label='征兵第五编队', options=['True'])
    pin.put_checkbox(checkbox_name[5], label='扫荡第一编队', options=['True'])
    pin.put_checkbox(checkbox_name[6], label='扫荡第二编队', options=['True'])
    pin.put_checkbox(checkbox_name[7], label='扫荡第三编队', options=['True'])
    pin.put_checkbox(checkbox_name[8], label='扫荡第四编队', options=['True'])
    pin.put_checkbox(checkbox_name[9], label='扫荡第五编队', options=['True'])
    pin.pin_on_change(checkbox_name[0], lambda select: handle_option_change(select, 0))
    pin.pin_on_change(checkbox_name[1], lambda select: handle_option_change(select, 1))
    pin.pin_on_change(checkbox_name[2], lambda select: handle_option_change(select, 2))
    pin.pin_on_change(checkbox_name[3], lambda select: handle_option_change(select, 3))
    pin.pin_on_change(checkbox_name[4], lambda select: handle_option_change(select, 4))
    pin.pin_on_change(checkbox_name[5], lambda select: handle_option_change(select, 5))
    pin.pin_on_change(checkbox_name[6], lambda select: handle_option_change(select, 6))
    pin.pin_on_change(checkbox_name[7], lambda select: handle_option_change(select, 7))
    pin.pin_on_change(checkbox_name[8], lambda select: handle_option_change(select, 8))
    pin.pin_on_change(checkbox_name[9], lambda select: handle_option_change(select, 9))


def demo(a):
    print('demo1', a)


def demo2(b):
    print('demo2', b)


def handle_option_change(selected, idx):
    if len(selected) > 0:
        current_date = get_current_date()
        if 0 <= idx <= 4:
            idx += 1
            sc_cron_add_jobs(zhengbing, idx, current_date['year'], current_date['month'], current_date['day'],
                             current_date['hour'], current_date['minute'], current_date['second'] + 1)
        elif 5 <= idx <= 9:
            idx -= 5


def start_web(port=12395):
    start_scheduler()
    start_server(bmi, port)
