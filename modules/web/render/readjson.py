import json
from pywebio import start_server

from pywebio.output import put_button, use_scope, put_collapse, put_text, put_scope, clear
from pywebio.pin import put_input, put_checkbox, pin_on_change

filename = './config.json'
load_dict = None


def formatCom(data):
    aside = []
    for v in data:
        aside.append(componentsAside(v))
    put_scope('st', [
        put_scope('aside', []).style('width:100px'),
        put_scope('collapse', []).style('width:200px'),
        put_scope('center', []).style('flex:1'),
    ]).style('display:flex;')
    with use_scope('aside'):
        for v in aside:
            v.show()


def componentsAside(aside):
    return put_button(aside['name'], onclick=componentsCollapse(aside['children'], aside['name']))


# 下拉选项框， 对应的全部按钮 对应的 chileren
def componentsCollapse(collapse, title):
    def render():
        collapseGroup = []
        for v in collapse:
            clear(v['scope'])
            collapseGroup.append(cvcomponentsAside(v))
        for v in collapse:
            with use_scope(v['scope'], clear=True):
                put_collapse(title, collapseGroup)

    return render


def cvcomponentsAside(aside):
    return put_button(aside['name'], onclick=componentsCollapseButton(aside['children']))


def pin_change_bool(v):
    def render(i):
        if len(i) > 0:
            v['value'] = True
        else:
            v['value'] = False
        print(data)

    return render


def reg_str(item):
    def render(v):
        if v is None:
            return None
        item['value'] = v
        print(data)

    return render


def componentsCollapseButton(aside):
    def render():
        with use_scope('center', clear=True):
            for index, item in enumerate(aside):
                input_name = f'item_{index}'
                if item['value'] is not None:
                    if isinstance(item['value'], bool):
                        put_scope(input_name, [
                            put_text(item['explain']),
                            put_checkbox(input_name, [{'label': '', 'value': True}], value=[item['value']])
                        ]).style('display:grid;grid-template-columns:auto auto;')
                        pin_on_change(input_name, pin_change_bool(item), clear=True)
                    else:
                        put_scope(input_name, [
                            put_text(item['explain']),
                            put_input(input_name, value=str(item['value']))
                        ]).style('display:grid;grid-template-columns:auto auto;')
                        pin_on_change(input_name, reg_str(item), clear=True)
                else:
                    put_text(item['explain'])

    return render


def init():
    formatCom(data)


data = None
if __name__ == '__main__':
    with open(filename, 'r', encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
        data = load_dict['st']
        print(data)
        start_server(init, port=9091, auto_open_webbrowser=True, debug=True)
