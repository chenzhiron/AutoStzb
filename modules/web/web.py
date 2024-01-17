from pywebio import start_server
from config.config import globalConfig
from pywebio.output import put_text, put_row, put_column, put_collapse, put_scope, put_scrollable

from modules.web.modules.renderTeam import renderTeam
from modules.web.modules.devices_web import change_config
from st import stzb

def init():
    put_column([
        put_row([stzb.render()]),
        put_row(
            [put_column([
                put_scope('config', change_config.render()),
                put_collapse('主城', renderTeam())
            ]).style('flex:1;'),
             put_scope('center', put_text('点击左侧选项'))
             .style('flex:1;'),
             put_scope('log', [put_text('日志'), put_scrollable(['123'], border=True, height=200)]).style('flex:1;')]
        ).style('display: flex;')
    ])


def start_web():
    start_server(init, port=globalConfig['Web']['port'], auto_open_webbrowser=True)


if __name__ == '__main__':
    start_web()
