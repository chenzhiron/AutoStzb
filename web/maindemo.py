import pywebio.pin as pin
from pywebio import start_server
from pywebio.output import put_row, put_column, put_code, put_collapse, put_button, put_text, put_scope, use_scope, \
    put_grid
from pywebio import session

from web.config import listGroup


@use_scope('center', clear=True)
def clickend():
    put_grid([
        [put_code('1'), put_code('2')],
        [put_code('3'), put_code('4')],
        [put_code('5'), put_code('6')],
        [put_code('7'), put_code('8')],
    ])


@use_scope('center', clear=True)
def clickend2():
    put_row([put_code('C'), put_code('D')], size='2fr 1fr')


@use_scope('center', clear=True)
def clickend3():
    put_row([put_code('E'), put_code('F')], size='2fr 1fr')


@use_scope('center', clear=True)
def clickend4():
    put_row([put_code('G'), put_code('H')], size='2fr 1fr')


def render_list_group():
    render = []
    for v in range(5):
        render.append(put_button('编队' + str(v + 1), onclick=clickend))
    return render


def render_active_group():
    render = []
    for v in range(3):
        render.append(put_button('编队' + str(v + 1), onclick=clickend2))
    return render


def render_config_group():
    render = []
    for v in range(3):
        render.append(put_button('配置' + str(v + 1), onclick=clickend3))
    return render


def render_going():
    return put_button('出征', onclick=clickend4)


# 初始化函数
def init():
    js_code = """
    document.querySelector('footer').style.display = 'none';
    document.body.style.overflow = 'hidden';
    """
    session.run_js(js_code)
    put_row([
        put_column([
            put_collapse('配置', render_config_group()),
            put_collapse('扫荡', render_list_group()),
            put_collapse('征兵', render_active_group()),
            put_collapse('出征', render_going())
        ]).style('display: block;'),
        put_scope('center'),
        render_options(),
    ], size='20% 50% 30%')


def executeoptions(*args):
    print(args)


def render_options():
    optionss = pin.put_select('optionss', options=listGroup, label='')
    pin.pin_on_change('optionss', onchange=executeoptions)
    return optionss


# 启动web
def start_web(web_port):
    start_server(init, port=web_port)


if __name__ == '__main__':
    start_web(18878)
