from pywebio.output import put_row,put_column,put_text

def def_lable_checkbox(component):
    for v in component.spec['input']['options']:
        v['label'] = ''
    return component

def explain_componet(texts, component):
    text_components = []
    for k, v in enumerate(texts):
        if k > 0:
            text_components.append(put_text(v).style('font-size:14px'))
        else:
            text_components.append(put_text(v))
         
    return put_row([
        put_column(text_components).style('display:block;'),
        component,
      ]).style('margin-bottom:15px;')
