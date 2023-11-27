from pywebio.pin import put_input, put_select, put_checkbox, pin_on_change
from pywebio.output import put_collapse, put_button, use_scope, put_row, put_text


def make_execute_handler(fn, instance):
    def handler(value):
        fn(value, instance)

    return handler


@use_scope('center', clear=True)
def render_config(config, instance):
    render = []
    for item in config:
        if item['type'] == 'input':
            value = getattr(instance, item['name'])
            render.append(
                put_row([put_text(item['explain']),
                         put_input(name=item['name'], value=item['value'] if item['value'] == value else value)])
            )
            pin_on_change(item['name'], onchange=make_execute_handler(item['fn'], instance), clear=True)
        elif item['type'] == 'select':
            value = getattr(instance, item['name'])
            render.append(
                put_row([put_text(item['explain']),
                         put_select(name=item['name'], options=item['options'],
                                    value=item['value'] if item['value'] == value else value)])
            )
            pin_on_change(item['name'], onchange=make_execute_handler(item['fn'], instance), clear=True)
        elif item['type'] == 'checkbox':
            value = getattr(instance, item['name'])
            render.append(
                put_row([put_text(item['explain']),
                         put_checkbox(name=item['name'],options=item['options'],
                                      value=item['value'] if item['value'] == value else value)])
            )
            pin_on_change(item['name'], onchange=make_execute_handler(item['fn'], instance), clear=True)

    render.reverse()
    return render


def make_handler(config, instance):
    def handler():
        render_config(config, instance)

    return handler


def render_options_config(options_all):
    render = []
    for group in options_all:
        buttons = []
        for option in group['options']:
            handler = make_handler(option['config'], option['instance'])
            button = put_button(option['name'], onclick=handler)
            buttons.append(button)
        render.append(put_collapse(group['groupName'], buttons))
    return render
