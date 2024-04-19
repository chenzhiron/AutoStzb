import logging
import traceback

class CustomHandler(logging.Handler):
    def __init__(self):
        from modules.web.web import send_message
        self.send_message = send_message
        logging.Handler.__init__(self)
    def emit(self, record):
        if record.levelno < logging.ERROR:  # 将条件改回原来的逻辑
            # Use a simpler format for messages below ERROR level
            simple_format = '%(asctime)s - %(levelname)s - %(message)s'
            formatter = logging.Formatter(simple_format)
            self.setFormatter(formatter)
            message = self.format(record)
        else:
            # Use a more detailed format for ERROR level messages
            custom_format = '%(asctime)s - %(levelname)s - %(message)s'
            formatter = logging.Formatter(custom_format)
            self.setFormatter(formatter)

            extra_info = "\n\tPathname: {}\n\tFilename: {}\n\tFunction Name: {}\n\tLine No: {}\n\tTime: {}\n\tThread ID: {}\n\tThread Name: {}\n\tProcess ID: {}\n\tMessage: {}\n".format(
                record.pathname, record.filename, record.funcName, record.lineno, record.created, record.thread, record.threadName, record.process, record.msg)

            if record.exc_info:
                trace = traceback.format_exc()
                extra_info += "\n\tTraceback:\n{}".format(trace)

            message = self.format(record=record) + extra_info
        self.send_message(message + '\r\n')

def setup_custom_logger(name):
    handler = CustomHandler()
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger

st_logger = setup_custom_logger('stzb')
