from multiprocessing import Process, Manager
from queue import Empty
from modules.log import set_handle

# from .setting import ShareData
from threading import Thread


class ProcessManage:
    _processes = None

    def __init__(self):
        self.st_thread = None
        self.st_log_queue = Manager().Queue()
        self.log = []
        self.log_thread = None
        self.log_thread_stop_flag = False

    def log_thread_fn(self):
        while not self.log_thread_stop_flag:
            try:
                v = self.st_log_queue.get(timeout=1)
            except Empty:
                continue

            self.log.append(v)

    def stop(self):
        if self.state:
            self.st_thread.kill()
            self.st_thread = None
            if self.log_thread and self.log_thread.is_alive():
                self.log_thread_stop_flag = True  # 设置退出标志
                self.log_thread.join(1)
            print("process exit")
            print("log_thread states:", self.log_thread.is_alive())

    def start(self, teamprop):
        print(type(teamprop))
        self.st_thread = Process(
            None, target=ProcessManage.run_st, args=(self.st_log_queue, teamprop)
        )
        print("st_thread:", self.st_thread)
        self.st_thread.start()

        self.log_thread_stop_flag = False
        self.log_thread = Thread(None, target=self.log_thread_fn)
        self.log_thread.start()

    @property
    def state(self) -> bool:
        return self.alive

    def run_st(q, teamprop):
        from st import St

        set_handle(q.put)
        St(teamprop).loop()

    @property
    def alive(self) -> bool:
        if self.st_thread is not None:
            return self.st_thread.is_alive()
        else:
            return False

    @classmethod
    def get_manager(cls) -> "ProcessManage":
        if ProcessManage._processes is None:
            ProcessManage._process = ProcessManage()

        return ProcessManage._process
