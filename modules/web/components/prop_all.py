class OptionExplain:
    def __init__(self, name, display_name, value, option_type, options=None):
        self.name = name
        self.display_name = display_name
        self.value = value
        self.option_type = option_type
        self.options = options
    def on_change_event(self, new_value, origin, origin_controller):
        origin_controller[self] = new_value
        origin[self.name] = new_value
        print('origin', origin_controller, origin)

        
team = OptionExplain(
    'team',
    '部队',
    1,
    'options',
    options=[1,2,3,4,5])

skip_await = OptionExplain(
    'skip_await',
    '跳过等待',
    False,
    'bool'
)

state = OptionExplain(
    'state',
    '状态',
    False,
    'bool'
)

explain = OptionExplain(
    'explain',
    '主城第二队队伍大营名字',
    '',
    'str'
)

await_time = OptionExplain(
    'await_time',
    '征兵等待时间',
    0,
    'int'
)

next_run_time = OptionExplain(
    'next_run_time',
    '下一次运行时间',
    '2024-01-01 00:00:00',
    'str'
)

x = OptionExplain(
    'x',
    'x坐标',
    0,
    'int'
)

y = OptionExplain(
    'y',
    'y坐标',
    0,
    'int'
)

recruit_person = OptionExplain(
    'recruit_person',
    '征兵',
    True,
    'bool'
)

going = OptionExplain(
    'going',
    '出征',
    False,
    'bool'
)
mopping_up = OptionExplain(
    'mopping_up',
    '扫荡',
    False,
    'bool'
)

delay = OptionExplain(
    'delay',
    '延迟',
    0,
    'int'
)

draw_txt = OptionExplain(
    'draw_txt',
    '平局',
    '',
    'str'
)

residue_troops_person = OptionExplain(
    'residue_troops_person',
    '部队剩余比例',
    0.5,
    'int'
)

residue_troops_enemy = OptionExplain(
    'residue_troops_enemy',
    '守军剩余比例',
    0.5,
    'int'
)

propall = {
    'team': team,
    'skip_await': skip_await,
    'state': state,
    'explain': explain,
    'await_time': await_time,
    'next_run_time': next_run_time,
    'x': x,
    'y': y,
    'recruit_person': recruit_person,
    'going': going,
    'mopping_up': mopping_up,
    'delay': delay,
    'draw_txt': draw_txt,
    'residue_troops_person': residue_troops_person,
    'residue_troops_enemy': residue_troops_enemy
}
