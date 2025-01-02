from loguru import logger
import json


def set_handle(fn):
    def render_message(message):
        v = json.loads(message)
        fn(v["text"])

    logger.add(render_message, serialize=True)


def info(message):
    logger.info(message)


def debug(message):
    logger.debug(message)


def warning(message):
    logger.warning(message)


def error(message):
    logger.error(message)
