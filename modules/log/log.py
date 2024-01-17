import logging

# 创建一个日志记录器，并设置级别
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# 创建一个处理器，用于将日志写入文件
file_handler = logging.FileHandler('my_log.log')
file_handler.setLevel(logging.DEBUG)

# 创建一个处理器，用于将日志输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 创建一个格式器，并将其添加到处理器中
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 将处理器添加到日志记录器中
logger.addHandler(file_handler)
logger.addHandler(console_handler)
if __name__ == '__main__':

    # 写日志
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')