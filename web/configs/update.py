from pywebio.output import clear, use_scope
from web.configs.config import render_options_config
from web.configs.module import options_config


def update_web():
    clear(scope='config')
    with use_scope('config', clear=True):
        result = render_options_config(options_config)
        result.show()
# def update_web_info(value):
#     put_text(value)
