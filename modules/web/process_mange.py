from multiprocessing import Process

class ProcessManage:
    _process = None

    def __init__(self):
        self.st_thread = None

    def stop(self):
        if self.state:
            self.st_thread.kill()
            self.st_thread = None

    def start(self):
        self.st_thread = Process(None, target=ProcessManage.run_st)
        self.st_thread.start()

    @property
    def state(self) -> bool:
        return self.alive

    def run_st():
        from st import St

        St().loop()

    @property
    def alive(self) -> bool:
        if self.st_thread is not None:
            return self.st_thread.is_alive()
        else:
            return False

    @classmethod
    def get_manager(cls) -> "ProcessManage":
        if ProcessManage._process is None:
            ProcessManage._process = ProcessManage()

        return ProcessManage._process
