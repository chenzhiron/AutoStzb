from threading import Thread
import time
from pywebio.output import put_text
from pywebio.session import SessionNotFoundException
from logdb import LogDb


class LogThread:
    def __init__(self):
        self.log_thread = Thread(target=self.render_log, daemon=True)
        self.active = True

    def render_log(self):
        logdb = LogDb("log.db")
        logdb.init_conn()
        currentIndex = 0
        while self.active:
            try:
                rows = logdb.select(1)
                if len(rows) != 0:
                    r = rows[-1]
                    if currentIndex == r[0]:
                        continue
                    else:
                        currentIndex = r[0]
                    for v in rows:
                        leave = "info"
                        if v[2] == 1:
                            leave = "warning"
                        put_text(r[1] + " : " + leave + " : " + r[3], scope="log")
            except SessionNotFoundException:
                self.stop()
            time.sleep(0.5)

    def start(self):
        self.log_thread.start()

    def stop(self):
        self.active = False
