from multiprocessing import Process
import queue
import threading
from typing import List
from rich.console import ConsoleRenderable

from modules.logger import logger, set_file_logger, set_func_logger


class ProcessManager:
    _instance = None  # 单例实例
    _process = None  # 进程实例

    def __init__(self):
        self._renderable_queue = queue.Queue()  # 日志渲染队列
        self.renderables: List[ConsoleRenderable] = []  # 存储的日志
        self.renderables_max_length = 400  # 日志最大存储量
        self.renderables_reduce_length = 80  # 日志裁剪量
        self._log_thread = None  # 日志处理线程
        self._process_lock = threading.Lock()  # 进程操作锁

    def start(self) -> None:
        """启动进程"""
        with self._process_lock:
            if not self.alive:
                self._process = Process(
                    target=ProcessManager._run_process,
                    args=(self._renderable_queue,)
                )
                self._process.start()
                self._start_log_thread()

    def stop(self) -> None:
        """停止进程"""
        with self._process_lock:
            if self.alive:
                self._process.terminate()
                self._add_log_message("Process exited. Reason: Manual stop")

            if self._log_thread is not None:
                self._log_thread.join(timeout=1)
                if self._log_thread.is_alive():
                    logger.warning("Log thread did not stop within 1 second")
                self._log_thread = None

    def _start_log_thread(self) -> None:
        """启动日志处理线程"""
        if self._log_thread and self._log_thread.is_alive():
            return

        self._log_thread = threading.Thread(
            target=self._handle_log_queue,
            daemon=True
        )
        self._log_thread.start()

    def _handle_log_queue(self) -> None:
        """处理日志队列"""
        while self.alive:
            try:
                log = self._renderable_queue.get(timeout=1)
                self._add_log_message(log)
            except queue.Empty:
                continue
        logger.info("Log thread stopped")

    def _add_log_message(self, message: ConsoleRenderable) -> None:
        """添加日志消息并控制存储量"""
        self.renderables.append(message)
        if len(self.renderables) > self.renderables_max_length:
            self.renderables = self.renderables[self.renderables_reduce_length:]

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
    def _run_process(queue: queue.Queue) -> None:
        """进程入口函数"""
        # 设置日志
        set_file_logger()
        set_func_logger(func=queue.put)

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