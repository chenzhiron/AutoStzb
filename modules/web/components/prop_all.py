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
    ['部队','选择出征的部队'],
    1,
    'options',
    options=[1,2,3,4,5])

state = OptionExplain(
    'state',
    ['状态', '启动前需要把配置全部配置好'],
    [],
    'bool'
)


await_time = OptionExplain(
    'await_time',
    ['下一次行动延迟时间','执行完 出征/扫荡 征兵？ 之后进行等待,之后再次执行。单位(秒)', 'tip:目前还没实装'],
    0,
    'int'
)

next_run_time = OptionExplain(
    'next_run_time',
    ['下一次运行时间', '自动计算的值，不需要更改'],
    '2024-01-01 00:00:00',
    'str'
)

x = OptionExplain(
    'x',
    ['x坐标', '如果选项为扫荡，只需要填入一个土地x坐标即可', '如果选项为出征,可以填入多个土地的y坐标，以 , 号分割；例如:315,648,1024'],
    0,
    'int'
)

y = OptionExplain(
    'y',
    ['y坐标', '如果选项为扫荡，只需要填入一个土地y坐标即可', '如果选项为出征,可以填入多个土地的y坐标，以 , 号分割；例如:513,846,4012'],
    0,
    'int'
)

recruit_person = OptionExplain(
    'recruit_person',
    ['征兵'],
    [],
    'bool'
)

going = OptionExplain(
    'going',
    ['出征'],
    [],
    'bool'
)
mopping_up = OptionExplain(
    'mopping_up',
    ['扫荡'],
    [],
    'bool'
)

residue_troops_person = OptionExplain(
    'residue_troops_person',
    ['部队剩余比例', '当我方兵力剩余兵力大于该比例时，会进行平局等待，同时，要求下方守军要求同样满足'],
    0.5,
    'int'
)

residue_troops_enemy = OptionExplain(
    'residue_troops_enemy',
    ['守军剩余比例','当守军兵力剩余兵力小于该比例时，会进行平局等待，同时，与上方部队要求同样满足'],
    0.5,
    'int'
)

simulator = OptionExplain(
    'simulator',
    ['模拟器配置', '选择要链接的模拟器，如果不确定自己要的是哪一个模拟器，可以进入 toolkit/adb 目录下，运行 cmd, 执行 adb devices,找到需要的模拟器，同时请注意，有一些模拟器并不支持或者等待适配中，目前推荐的是 夜神模拟器'],
    '',
    'str'
)

outset = OptionExplain(
    'outset',
    ['出发基点', '如果在野外要塞出发则填写野外要塞名字，主城不填'],
    '',
    'str'
)

standby_max = OptionExplain(
    'standby_max',
    ['部队总数','选择要出征的要塞/主城当前已放置的部队总数数量'],
    5,
    'options',
    [1,2,3,4,5]
)
screen_await = OptionExplain(
    'screen_await',
    ['截图间隔时间','截图间隔时间。单位(秒)'],
    0.3,
    'options',
    [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
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
    'simulator': simulator,
    "standby_max": standby_max,
    "outset": outset,
    "screen_await": screen_await
}
