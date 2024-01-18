import pywebio
from pywebio import start_server
from config.config import globalConfig
from pywebio.output import put_text, put_collapse, put_scope, put_scrollable

from modules.web.modules.renderTeam import renderTeam
from modules.web.modules.devices_web import change_config

from st import stzb

# pywebio.config(css_file='./modules/cover.css')

pywebio.config(css_style="""
    * {
        margin: 0 ;
        padding: 0 ;
    }
    .container {padding:0;
    margin:0;
    max-width: 100%;
    }
    .pywebio {
        padding:0;
    }
    .footer{
        display: none;
        }
""")


def init():
    put_scope('title', stzb.render()).style('height:44px')
    put_scope('details', [
        put_scope('aside',
                  [change_config.render(), put_collapse('主城', renderTeam())]
                  ).style('width:200px;margin-right:8px;'),
        put_scope('center', []).style('flex:1;'),
        put_scope('log', [put_text('日志'), put_scrollable(['123'], border=True)]).style('flex:1;marign-left:8px;')
    ]).style('display:flex;')


def start_web():
    start_server(init, port=globalConfig['Web']['port'], auto_open_webbrowser=True, cdn=False)


if __name__ == '__main__':
    start_web()
