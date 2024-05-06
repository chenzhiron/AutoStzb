import os

from pywebio_battery import logbox_append

from pywebio.session import ThreadBasedSession, eval_js
from functools import  wraps
from uuid import uuid4

from modules.manager.main import conf
class WebConfig:
    sessions = []
    def __init__(self):
        self.conf_data = conf
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

