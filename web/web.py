from config.task_or_web_common import update_queue
from modules.dispatcher.Dispatcher import task_dispatcher
from pywebio import start_server
from pywebio.output import put_row, put_column, put_scope
from pywebio import session
from web.configs.config import render_options_config
from web.configs.module import options_config, render_status
from web.configs.update import update_web, update_log


# 初始化函数
def init():
    js_code = """
    document.querySelector('footer').style.display = 'none';
    document.body.style.overflow = 'hidden';
    document.title = 'stzb';
    """
    session.run_js(js_code)
    # put_row(
    # [put_text('注意！所有功能的一切前提是以主城为中心出发，在野外要塞或其他不属于主城的地方出征/扫荡可能会出现错误')])

    put_row([put_scope('status', render_status(task_dispatcher.get_status()))])
    put_row([
        put_column([
            put_row([put_scope('config', render_options_config(options_config))])
        ]),
        put_column([
            put_scope('center')
        ]),
        put_column([
            put_scope('info').style('height: 400px;overflow:auto;')
        ])
    ], size='20% 40% 40%')
    while True:
        msg = update_queue.get()  # 阻塞直到队列中有消息
        if msg[0] == 'update':
            update_web()
        elif msg[0] == 'log':
            update_log(msg[1])


# 启动web
def start_web(web_port):
    start_server(init, port=web_port, auto_open_webbrowser=True)

# if __name__ == '__main__':
#     start_web(18878)
