from threading import Thread
import time
from pywebio.output import put_text
from pywebio.session import get_current_session

class LogThread:
    _thread = None

    def __init__(self):
        self.log_thread = Thread(None, target=self.render_log)
        self.log_thread.setDaemon(True)

    def initiate(self):
        self.log_thread.start()

    def active(self):
        if self.log_thread is None:
            return False
        return self.log_thread.is_alive()

    def render_log(self):
        v = get_current_session()
        print(v)
        while True:
            try:
                put_text(time.time(), scope="log")
            except Exception as e:
                print(e)
            time.sleep(0.5)

    @classmethod
    def get_logthread(cls):
        if LogThread._thread is None:
            LogThread._thread = LogThread()
        return LogThread._thread
