from pywebio.output import put_text
from pywebio.input import select
from modules.tasks.zhengbing import zhengbing

from dispatcher.execute_job import sc_cron_add_jobs


def bmi():
    options = ['队伍一', '队伍二', '队伍三']
    selected_option = select('请选择一个选项', options, onchange=handle_option_change)


def handle_option_change(selected):
    print(selected)
    if selected:
        sc_cron_add_jobs()
