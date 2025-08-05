from multiprocessing import Process

from modules.logger import logger, set_func_logger


class ProcessManager:
    _instance = None  # 单例实例
    _process = None  # 进程实例

    def __init__(self):
        self._log_thread = None  # 日志处理线程

    def start(self) -> None:
        """启动进程"""
        if not self.alive:
            self._process = Process(
                target=ProcessManager._run_process
            )
            self._process.start()

    def stop(self) -> None:
        """停止进程"""
        if self.alive:
            self._process.terminate()

    @property
    def alive(self) -> bool:
        """检查进程是否运行中"""
        return self._process is not None and self._process.is_alive()

    @property
    def state(self) -> int:
        """获取进程状态"""
        if not self.renderables:
            return 0  # 未启动

        if self.alive:
            return 1  # 运行中

        # 检查最后一条日志判断退出原因
        last_log = str(self.renderables[-1])
        if "Manual stop" in last_log:
            return 2  # 手动停止
        elif "Finish" in last_log:
            return 3  # 正常完成
        else:
            return 4  # 异常退出

    @staticmethod
    def _run_process() -> None:
        try:
            from st import St
            St().loop()
            logger.info("Process exited. Reason: Finish")
        except Exception as e:
            logger.exception(e)
            logger.error("Process exited. Reason: Error")

    @classmethod
    def get_instance(cls) -> "ProcessManager":
        """获取单例实例"""
        if cls._instance is None:
            cls._instance = ProcessManager()
        return cls._instance
