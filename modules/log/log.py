import logging

from config.task_or_web_common import update_queue


class MyLogger(logging.Logger):
    def __init__(self, name):
        super().__init__(name)


class StringHandler(logging.Handler):
    def __init__(self):
        super().__init__()

    def emit(self, record):
        # 获取日志消息的字符串
        log_string = self.format(record)
        # 将日志消息的字符串添加到列表中
        update_queue.put(['log', log_string])


logger = MyLogger('log')
handler = StringHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)
