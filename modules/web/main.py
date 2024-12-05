from pywebio.platform.tornado import start_server
from pywebio.output import put_scope, use_scope
from pywebio.session import set_env
from pywebio import config

from .function import private, team, OverViewView
from .process_mange import ProcessManage
from .setting import ShareData

def server():
  ShareData.init()
    
  config(css_file='./static/style.css')
  start_server(app, port=10965, auto_open_webbrowser=True, static_dir='./modules/web/static')

def app():
  set_env(output_max_width='100%')
  put_scope('main', [
     put_scope('memu').style('width:100px;'),
      put_scope('function').style('width:200px;'),
      put_scope('function_area').style('flex:1;')
    ]).style('display:flex')
 
  with use_scope('function',clear=True):
    OverViewView(ProcessManage.get_manager('st')).render()
    private.render()
    team.render()
