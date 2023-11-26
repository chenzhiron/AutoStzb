
listGroup = [
    {
        'label': 1,
        'value': 1,
        'selected': True
    },
    {
        'label': 2,
        'value': 2
    },
    {
        'label': 3,
        'value': 3
    },
    {
        'label': 4,
        'value': 4
    },
    {
        'label': 5,
        'value': 5
    }
]

explain = '编队'

def render_Options(o, e, instance):
    optionss = pin.put_select('optionss', options=o, label='')
    pin.pin_on_change('optionss', onchange=executeoptions)
    return optionss

