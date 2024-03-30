import json
import os
import copy
import functools

from pywebio.output import put_row, put_scope, use_scope, put_collapse,put_button, put_column, put_text
from pywebio import start_server
from pywebio.session import set_env

from components.Option import OptionPage
from components.prop_all import *


current_file_path = os.path.abspath(__file__)

# 获取当前文件所在的目录
current_dir_path = os.path.dirname(current_file_path)

# 拼接config.yaml的路径
config_file_path = os.path.join(current_dir_path, 'config.json')

print(config_file_path)

class WebConfig:
    def __init__(self):
        self.data = None
        self.config_file = config_file_path
        with open(self.config_file, 'r', encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
            self.data = load_dict

class Web(WebConfig):

    def __init__(self):
        super().__init__()

    # def get_main_data(self):
    #     return copy.deepcopy(self.data)

    # def update_main_data(self, data):
    #     self.data = data

    @use_scope('menu_bar', clear=True)
    def render_memu_bar(self, updata):
          OptionPage([updata, {
                    team: updata['team'],
                    skip_await: updata['skip_await'],
                    state: updata['state'],
                    explain: updata['explain'],
                    await_time: updata['await_time'],
                    next_run_time: updata['next_run_time'],
                    mopping_up: updata['mopping_up'],
                    delay: updata['delay'],
                    draw_txt: updata['draw_txt'],
                    residue_troops_person: updata['residue_troops_person'],
                    residue_troops_enemy: updata['residue_troops_enemy']
                }]).dispatch()
          
    @use_scope('navigation_bar', clear=True)
    def render_navigation_bar(self):
        tasks_render = []
        for v in self.data['task']:
            tasks_render.append(put_button('队伍', onclick= functools.partial(self.render_memu_bar, updata = v)))
        put_collapse('任务', tasks_render)
    
    def change_state(self, state):
        self.data['state'] = state
        self.render_state()

    @use_scope('state', clear=True)
    def render_state(self):
        put_text('调度器').style('display:inline-block')
        if self.data['state'] == 0:
            put_button('启动', onclick= functools.partial(self.change_state, state = 1)).style('display:inline-block')
        if self.data['state'] == 1:
            put_button('停止', onclick= functools.partial(self.change_state, state = 0)).style('display:inline-block')

    @use_scope('title', clear=True)
    def render_title(self, title):
        put_text(title).style('display:inline-block')

    def render(self):
        set_env(title="AutoStzb", output_max_width='100%')
        put_scope('topp', [put_scope('state', []), put_scope('title', [])]).style('display:flex')
        self.render_state()
        self.render_title('主页')
        put_row([
            put_scope('navigation_bar', []),
            put_scope('function_bar', []),
            put_scope('menu_bar', []),
            put_scope('log_bar', [])
        ]).style('display:flex')
        self.render_navigation_bar()
         

if __name__ == '__main__':
    ui = Web()
    start_server(ui.render, port=9091, debug=True)
