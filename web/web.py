from pywebio import start_server
from pywebio.output import put_row, put_column, put_scope, put_button, clear, use_scope
from pywebio import session

from web.configs.config import render_options_config
from web.configs.module import options_config

# 初始化函数
def init():
    js_code = """
    document.querySelector('footer').style.display = 'none';
    document.body.style.overflow = 'hidden';
    document.title = 'stzb';
    """
    session.run_js(js_code)
    put_row([
        put_column([
            put_scope('config', render_options_config(options_config))
        ]),
        put_column([
            put_scope('center')
        ]),
        put_column([
            put_scope('info')
        ])
    ], size='20% 50% 30%')


# 启动web
def start_web(web_port):
    start_server(init, port=web_port)

# if __name__ == '__main__':
#     start_web(18878)
