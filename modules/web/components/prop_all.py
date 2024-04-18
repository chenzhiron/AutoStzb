class OptionExplain:
    def __init__(self, name, display_name, value, option_type, options=None):
        self.name = name
        self.display_name = display_name
        self.value = value
        self.option_type = option_type
        self.options = options
    def on_change_event(self, new_value, origin, origin_controller):
        if type(new_value) is list:
            if len(new_value) == 1:
                new_value = True
            else:
                new_value = False
        origin_controller[self] = new_value
        origin[self.name] = new_value

        
team = OptionExplain(
    'team',
    '部队',
    1,
    'options',
    options=[1,2,3,4,5])

state = OptionExplain(
    'state',
    '状态',
    [],
    'bool'
)


await_time = OptionExplain(
    'await_time',
    '下一次行动延迟时间',
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
    [],
    'bool'
)

going = OptionExplain(
    'going',
    '出征',
    [],
    'bool'
)
mopping_up = OptionExplain(
    'mopping_up',
    '扫荡',
    [],
    'bool'
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

simulator = OptionExplain(
    'simulator',
    '模拟器配置',
    '',
    'str'
)

propall = {
    'team': team,
    'state': state,
    'await_time': await_time,
    'next_run_time': next_run_time,
    'x': x,
    'y': y,
    'recruit_person': recruit_person,
    'going': going,
    'mopping_up': mopping_up,
    'residue_troops_person': residue_troops_person,
    'residue_troops_enemy': residue_troops_enemy,
    'simulator': simulator
}
