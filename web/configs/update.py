from pywebio.output import clear, use_scope, put_text
from web.configs.config import render_options_config
from web.configs.module import options_config


def update_web():
    clear(scope='config')
    with use_scope('config', clear=True):
        result = render_options_config(options_config)
        for v in result:
            v.show()


# def update_web_info(value):
#     put_text(value)
def update_log(value):
    with use_scope('info'):
        put_text(value)
