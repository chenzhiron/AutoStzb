from pywebio.output import put_scope, put_text, use_scope
from web.configs.config import render_options_config
from web.configs.module import options_config


def update_web():
    put_scope('center', render_options_config(options_config))


@use_scope('info')
def update_web_info(value):
    put_text(value)
