import queue
import re
import threading
import time
from datetime import datetime, timedelta
from typing import Callable, Any, Optional

import numpy as np

from modules.ocr.main import ocr_format_val
from modules.utils import convert_to_timestamp


def battle_time(img, v):
    # 战报时间
    times = convert_to_timestamp(
        ocr_format_val(img.crop([665, v + 240, 900, v + 240 + 40]))
    ) or convert_to_timestamp(
        ocr_format_val(img.crop([665, v + 230, 900, v + 230 + 50]))
    )
    if type(times) is str or times is None:
        times = convert_to_timestamp(
            ocr_format_val(
                img.crop([665, v + 230 + 80, 900, v + 230 + 80 + 60])
            )
        )
    print("times", times)
    return times


def time_str_to_seconds(time_str):
    try:
        time_obj = datetime.strptime(time_str, '%H:%M:%S')
        total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
        return total_seconds
    except (ValueError, AttributeError, TypeError):
        return 0


def time_consuming(data):
    if data[0] is None:
        return 0
    result = []
    for v in data[0]:
        custom_times = v[1][0]
        result.append(time_str_to_seconds(custom_times))
    return max(result)


def extract_numbers_from_brackets(text):
    try:
        # 使用正则表达式查找括号内的内容，包括中文和英文括号，并处理可能缺失的右括号
        match = re.search(r'[（(]([^）)\n]+)', text)
        if not match:
            return None

        # 获取括号内的内容
        content = match.group(1)

        # 移除可能存在的右括号（如果有）
        content = content.split(')')[0] if ')' in content else content
        content = content.split('）')[0] if '）' in content else content

        # 使用非数字分割字符串
        numbers = re.split(r'[^\d]+', content)

        # 过滤掉空字符串并转换为整数
        numbers = [int(num) for num in numbers if num]

        # 如果找到至少两个数字，返回前两个
        if len(numbers) >= 2:
            return numbers[0], numbers[1]
        else:
            return None
    except (TypeError, ValueError):
        return None


def get_future_time(seconds):
    # 获取当前本地时间
    current_time = datetime.now()

    # 加上指定的秒数
    future_time = current_time + timedelta(seconds=seconds)

    # 格式化为目标字符串
    future_time_str = future_time.strftime("%Y/%m/%d %H:%M:%S")

    return future_time_str


def process_list(input_list):
    result = []
    for item in input_list:
        if len(item) != 2:  # 确保每个子列表有2个元素
            continue

        first_element = item[0]
        second_element = item[1]

        # 尝试将第二个元素转换为数字
        try:
            num = float(second_element)  # 先尝试转换为float
            if num.is_integer():  # 如果是整数，转换为int
                num = int(num)
            result.append([first_element, num])
        except ValueError:
            # 转换失败，使用正则剔除非数字字符
            cleaned = re.sub(r'[^0-9]', '', second_element)
            if len(cleaned) > 0:
                # 尝试将清理后的字符串转换为数字
                try:
                    num = int(cleaned)
                    result.append([first_element, num])
                except ValueError:
                    # 如果清理后还是不能转换为数字，跳过
                    continue
            else:
                # 清理后长度为0，跳过
                continue
    return result


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
