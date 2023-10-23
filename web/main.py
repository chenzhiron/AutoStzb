from functools import partial

import pywebio.pin as pin
from pywebio import start_server
from pywebio.output import put_row, put_column, put_code, put_collapse, put_button, put_text, put_scope, set_scope, \
    clear, use_scope

#
# def bmi():
#     put_row([
#         put_column([
#             put_code('A'),
#             put_code('C'),
#             put_code('C'),
#         ]), None,
#         put_code('D'), None,
#         put_table([
#             ['征兵第二编队',  pin.put_checkbox('demo1', options=['True']),]
#         ]),
#     ])
#
#
# def start_web(port=12395):
#     # start_scheduler()
#     start_server(bmi, port)
#
#
# if __name__ == '__main__':
#     start_web()


# from modules.utils.main import get_current_date
# from dispatcher.execute_job import sc_cron_add_jobs, start_scheduler
# from modules.tasks.zhengbing import zhengbing

# checkbox_name = ('zhengbing1', 'zhengbing2', 'zhengbing3', 'zhengbing4', 'zhengbing5',
#                  'saodang1', 'saodang2', 'saodang3', 'saodang4', 'saodang5')

# def handle_option_change(selected, idx):
#     if len(selected) > 0:
#         current_date = get_current_date()
#         if 0 <= idx <= 4:
#             idx += 1
#             sc_cron_add_jobs(zhengbing, idx, current_date['year'], current_date['month'], current_date['day'],
#                              current_date['hour'], current_date['minute'], current_date['second'] + 1)
#         elif 5 <= idx <= 9:
#             idx -= 5


# pin.put_checkbox(checkbox_name[0], label='征兵第一编队', options=['True'])
#    pin.put_checkbox(checkbox_name[1], label='征兵第二编队', options=['True'])
#    pin.put_checkbox(checkbox_name[2], label='征兵第三编队', options=['True'])
#    pin.put_checkbox(checkbox_name[3], label='征兵第四编队', options=['True'])
#    pin.put_checkbox(checkbox_name[4], label='征兵第五编队', options=['True'])
#    pin.put_checkbox(checkbox_name[5], label='扫荡第一编队', options=['True'])
#    pin.put_checkbox(checkbox_name[6], label='扫荡第二编队', options=['True'])
#    pin.put_checkbox(checkbox_name[7], label='扫荡第三编队', options=['True'])
#    pin.put_checkbox(checkbox_name[8], label='扫荡第四编队', options=['True'])
#    pin.put_checkbox(checkbox_name[9], label='扫荡第五编队', options=['True'])
#    pin.pin_on_change(checkbox_name[0], lambda select: handle_option_change(select, 0))
#    pin.pin_on_change(checkbox_name[1], lambda select: handle_option_change(select, 1))
#    pin.pin_on_change(checkbox_name[2], lambda select: handle_option_change(select, 2))
#    pin.pin_on_change(checkbox_name[3], lambda select: handle_option_change(select, 3))
#    pin.pin_on_change(checkbox_name[4], lambda select: handle_option_change(select, 4))
#    pin.pin_on_change(checkbox_name[5], lambda select: handle_option_change(select, 5))
#    pin.pin_on_change(checkbox_name[6], lambda select: handle_option_change(select, 6))
#    pin.pin_on_change(checkbox_name[7], lambda select: handle_option_change(select, 7))
#    pin.pin_on_change(checkbox_name[8], lambda select: handle_option_change(select, 8))
#    pin.pin_on_change(checkbox_name[9], lambda select: handle_option_change(select, 9))

current_status = False

zhengbing_list = ['征兵第一编队', '征兵第二编队', '征兵第三编队']
saodang_list = ['扫荡第一编队', '扫荡第二编队', '扫荡第三编队', '扫荡第四编队', '扫荡第五编队']

current_options = ''
current_index = 0


def init():
    put_row([
        put_column([
            put_collapse('征兵', render_button(zhengbing_list, 2)),
            put_collapse('扫荡', render_button(saodang_list, 2)),
            None,
        ]),

        put_scope('center', put_column([
            None,
            None,
        ])),

        put_code('python\n' * 20).style('max-height:200px;'),
    ])


def bmi():
    content = put_text('111111111')
    return content


def bmi2():
    content = put_text('替换')
    return content


def render_button(lists, l):
    button_list = []
    for i, info in enumerate(lists):
        onclick = partial(add_zhengbing, info=info[:l], index=i + 1)
        button_list.append(put_button(info, onclick=onclick))
    return button_list


def add_zhengbing(info, index):
    global current_index,current_options
    current_options = info
    current_index = index
    with use_scope('center', clear=True, create_scope=True):
        if current_options == '征兵':
            bmi2()
        elif current_options == '扫荡':
            bmi()


def add_saodnag(i):
    pass


if __name__ == '__main__':
    start_server(init, 12395)
