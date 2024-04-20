import json
import os
import copy
import functools
import threading
import time

from flask import session
from pywebio.output import put_scope, use_scope, put_collapse,put_button, put_text, clear, put_image
from pywebio_battery import put_logbox, logbox_append
from pywebio import start_server, config
from pywebio.session import set_env, ThreadBasedSession, eval_js

from functools import wraps
from typing import Callable
from uuid import uuid4
import logging

from modules.web.components.Option import *
from modules.web.components.prop_all import *
from modules.web.styles import style

current_file_path = os.path.abspath(__file__)

# 获取当前文件所在的目录
current_dir_path = os.path.dirname(current_file_path)

# 拼接config.yaml的路径
config_file_path = os.path.join(current_dir_path, 'config.json')


class WebConfig:
    def __init__(self):
        self.data = None
        self.config_file = config_file_path
        with open(self.config_file, 'r', encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
            self.data = load_dict
        self.logs = []
    def add_log(self, msg):
        if len(self.logs) > 500:
            self.logs = self.logs[300:]
        self.logs.append(msg)
    def get_log(self):
        return self.logs
    
sessions = []

def for_all_sessions(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        for session in sessions:
            func_id = str(uuid4())
            def inner(_):
                func(*args, **kwargs)

            session.callbacks[func_id] = (inner, False)
            session.callback_mq.put({"task_id": func_id, "data": None})

    return wrapper


def register_session():
    sessions.append(ThreadBasedSession.get_current_session())

@for_all_sessions
def send_message(msg):
    res = eval_js("""
                document.getElementById('pywebio-scope-log_bar')
                  """)
    ui.add_log(msg)
    if res:
        logbox_append('log', ui.get_log()[-1])


class Web(WebConfig):

    def __init__(self):
        super().__init__()

    def get_data(self, key=None):
        if key is None:
            return copy.deepcopy(self.data)
        return copy.deepcopy(self.data[key])
    def set_data(self, key, value, keyid = None):
        if key == 'task':
            for v in self.data['task']:
                if v['id'] == keyid:
                    v.update(value)
        else:
            self.data[key] = value

    def clear_area(self, area_lists=['navigation_bar', 'content']):
        for v in area_lists:
            clear(v)

    @use_scope('navigation_bar', clear=True)
    def render_navigation_bar(self):
        self.clear_area()
        tasks_render = []
        for v in self.data['task']:
            tasks_render.append(put_button('主城部队', onclick= functools.partial(self.render_memu_bar, updata = v)))
        put_collapse('队伍', tasks_render)

    def change_state(self, state):
        self.data['state'] = state
        self.render_state()

    @use_scope('state', clear=True)
    def render_state(self):
        put_text('调度器')
        if self.data['state'] == 0:
            put_button('启动', onclick= functools.partial(self.change_state, state = 1))
        if self.data['state'] == 1:
            put_button('停止', onclick= functools.partial(self.change_state, state = 0))

    @use_scope('content', clear=True)
    def render_log(self):
        self.clear_area()
        put_scope('log_bar', [put_logbox('log', height=700)])
        for v in self.get_log():
            logbox_append('log', v)


    @use_scope('content', clear=True)
    def render_memu_bar(self, updata):
          with use_scope('menu_bar', clear=True):
            OptionPage([updata, {
                        state: updata['state'],
                        team: updata['team'],
                        next_run_time: updata['next_run_time'],
                        recruit_person:updata['recruit_person'],
                        going: updata['going'],
                        mopping_up: updata['mopping_up'],
                        x: updata['x'],
                        y: updata['y'],
                        await_time: updata['await_time'],
                        residue_troops_person: updata['residue_troops_person'],
                        residue_troops_enemy: updata['residue_troops_enemy']
                    }]).dispatch()
            
          with use_scope('img_show', clear=True):
              put_text('战报记录')
              if len(updata['battle_info']) > 0:
                  updata['battle_info'].reverse()
                  for v in updata['battle_info']:
                    put_image(v)

    config(css_style=style)
    def render(self):
        register_session()

        set_env(title="AutoStzb", output_max_width='100%')
        put_scope('top', [
                            put_scope('state', [])
                            ])
        self.render_state()
        put_scope('main', [
                    put_scope('module_bar', []),
                    put_scope('navigation_bar', []),
                    put_scope('content', []),
        ])
        self.render_module_bar()
    
    @use_scope('navigation_bar', clear=True)
    def manager(self):
        self.clear_area()
        put_button('模拟器配置', onclick=self.render_manager_simulator)

    @use_scope('content', clear=True)
    def render_manager_simulator(self):
        with use_scope('menu_bar', clear=True):
            key = propall['simulator']
            Option(key.display_name, Component(key.name, self.data[key.name],
                                                key.option_type, functools.partial(
                                                    key.on_change_event,
                                                        origin=self.data,
                                                        origin_controller={key:self.data[key.name]}
                                                        ))
                ).options


    def render_module_bar(self):
        with use_scope('module_bar', clear=True):
            put_button('日志', onclick=self.render_log)
            put_button('管理', onclick=self.manager)
            put_button('功能', onclick=self.render_navigation_bar)


ui = Web()

def start_web(): 
    start_server(ui.render, port=9091, debug=True)

if __name__ == '__main__':
    start_web()
