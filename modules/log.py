from loguru import logger
import json

def set_handle(fn):
    def render_message(message):
        v = json.loads(message)
        fn(v['text'])
    logger.add(render_message, serialize=True)
