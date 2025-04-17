import cv2
import numpy as np
from modules.ocr.main import ocr_format_val
from modules.utils import formatDate
import threading
import queue
import time
from typing import Callable, Any, Optional

def battle_time(img, v):
    # 战报时间
    times = formatDate(
        ocr_format_val(np.array(img.crop([665, v + 240, 900, v + 240 + 40])))
    ) or formatDate(
        ocr_format_val(np.array(img.crop([665, v + 230, 900, v + 230 + 50])))
    )
    if type(times) is str or times is None:
        times = formatDate(
            ocr_format_val(
                np.array(img.crop([665, v + 230 + 80, 900, v + 230 + 80 + 60]))
            )
        )
    print("times", times)
    return times


class BaseTypeImg:
    def __init__(self):
        self.attack_template_img = cv2.imread(
            "./modules/imgs/attack_template.png", cv2.IMREAD_COLOR
        )
        self.defense_template_img = cv2.imread(
            "./modules/imgs/defense_template.png", cv2.IMREAD_COLOR
        )
        self.exploit_template_img = cv2.imread(
            "./modules/imgs/condinate.png", cv2.IMREAD_COLOR
        )





class AsyncTaskProcessor:
    def __init__(self, task_func: Callable[[], Any], max_queue_size: int = 10):
        """
        异步任务处理器

        :param task_func: 要异步执行的任务函数
        :param max_queue_size: 结果队列的最大长度
        """
        self.task_func = task_func
        self.result_queue = queue.Queue(maxsize=max_queue_size)
        self._stop_event = threading.Event()
        self._pause_event = threading.Event()  # 新增：用于暂停工作线程
        self._thread = threading.Thread(target=self._worker, daemon=True)
        self._lock = threading.Lock()
        self._active = False

    def _worker(self):
        """工作线程的主函数"""
        while not self._stop_event.is_set():
            try:
                # 检查是否需要暂停
                if self.result_queue.full():
                    self._pause_event.set()
                    time.sleep(0.1)  # 避免忙等待
                    continue

                self._pause_event.clear()
                result = self.task_func()
                self.result_queue.put(result, block=True, timeout=0.5)
            except queue.Full:
                # 队列已满，下一轮循环会触发暂停
                continue
            except Exception as e:
                print(f"Task execution failed: {e}")
                continue

    def start(self):
        """启动工作线程"""
        with self._lock:
            if not self._active:
                self._active = True
                self._stop_event.clear()
                self._pause_event.clear()
                self._thread.start()

    def stop(self):
        """停止工作线程"""
        with self._lock:
            if self._active:
                self._stop_event.set()
                self._thread.join(timeout=1)
                self._active = False

    def get_result(self, timeout: Optional[float] = None) -> Any:
        """
        从队列中获取一个结果

        :param timeout: 超时时间(秒)，None表示无限等待
        :return: 任务函数的返回结果
        :raises queue.Empty: 如果超时且队列为空
        """
        try:
            result = self.result_queue.get(timeout=timeout)
            # 取出结果后，如果有线程在等待，就唤醒
            if self._pause_event.is_set() and not self.result_queue.full():
                self._pause_event.clear()
            return result
        except queue.Empty:
            raise

    def has_result(self) -> bool:
        """检查队列中是否有可用结果"""
        return not self.result_queue.empty()

    def clear_results(self):
        """清空结果队列"""
        while not self.result_queue.empty():
            try:
                self.result_queue.get_nowait()
            except queue.Empty:
                break
        # 清空后唤醒可能暂停的线程
        self._pause_event.clear()

    def is_running(self) -> bool:
        """检查工作线程是否在运行"""
        with self._lock:
            return self._active

    def is_paused(self) -> bool:
        """检查工作线程是否因队列满而暂停"""
        return self._pause_event.is_set()