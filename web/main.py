from pywebio.output import put_text
from pywebio.input import select
from tasks.zhengbing import zhengbing

def bmi():
    options = ['队伍一', '队伍二', '队伍三']
    selected_option = select('请选择一个选项', options, onchange=handle_option_change)


def handle_option_change(selected):
    put_text(selected)
    if selected == '队伍一':
        zhengbing(1)
