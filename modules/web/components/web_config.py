import os 
import json
import os

from pywebio_battery import logbox_append

from pywebio.session import ThreadBasedSession, eval_js
from functools import  wraps
from uuid import uuid4

current_file_path = os.path.abspath(__file__)

# 获取当前文件所在的目录
current_dir_path = os.path.dirname(current_file_path)

# 拼接config.yaml的路径
config_file_path = os.path.join(current_dir_path, 'config.json')


class WebConfig:
    sessions = []
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
    

    # https://github.com/pywebio/PyWebIO/issues/565
    def for_all_sessions(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            for session in self.sessions:
                func_id = str(uuid4())
                def session_callback(_):
                    func(self, *args, **kwargs)

                session.callbacks[func_id] = (session_callback, False)
                session.callback_mq.put({"task_id": func_id, "data": None})
        return wrapper
    def register_session(self):
        self.sessions.append(ThreadBasedSession.get_current_session())


    @for_all_sessions
    def send_message(self, msg):
        res = eval_js("""
                    document.getElementById('pywebio-scope-log_bar')
                    """)
        self.add_log(msg)
        if res:
            logbox_append('log', self.get_log()[-1])

