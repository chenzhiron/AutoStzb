import time

from modules.devices.main import DeviceManager, DeviceOperator
from modules.static.config_keys import MartialArtsKeys
from modules.taskfn.basic import Basic
from modules.taskfn.steps_basic import StepsBasic
from modules.taskfn.tasks_utils import get_future_time
from modules.utils import truncated_normal


class MartialArts(Basic):
    def __init__(self, device, config):
        super().__init__(device,config)
        self.basic_step = StepsBasic(device)
        self.battling_num = 0
        self.battling_max_num = 8
    def entry_map(self):
        if self.basic_step.verify_entey_neizheng():
            self.device.click(truncated_normal(290,340), truncated_normal(735,850))
            return True
        return False

    def entry_martial_arts_map(self):
        if self.basic_step.verify_entry_martial_arts_map():
            self.device.click(truncated_normal(1225,1320), truncated_normal(470,540))
            return True
        return False

    def verify_remaining(self):
        if self.basic_step.verify_remaining_num() == '剩余挑战轮次1':
            self.device.click(truncated_normal(685,900), truncated_normal(822,860))
            return True
        elif self.basic_step.verify_remaining_num() == '剩余挑战轮次0':
            print(2222)
            return True
        return False

    def select_difficulty(self):
        if self.basic_step.verify_select_difficulty() == '确定挑战':
            select_difficulty = int(self.config[MartialArtsKeys.DIFFICULTY])
            offset_x = (select_difficulty - 1) * 50 + 220 * select_difficulty + 130
            self.device.click(truncated_normal(offset_x-200, offset_x), truncated_normal(300,550))
            return True
        return False

    def click_next_difficulty(self):
        self.device.click(truncated_normal(687,900), truncated_normal(682,725))
        return True

    def battling(self):
        time.sleep(2)
        axis = self.basic_step.select_maps_battling_bit()
        if axis is None:
            return False
        (x, y),v = axis
        self.device.click(x+360, y+76+60+40)
        return True

    def battling_end(self):
        bat_res = self.basic_step.verify_batting_end_result()
        if bat_res is not None and "战斗" in bat_res:
            self.device.click(truncated_normal(690,910), truncated_normal(715,750))
            self.battling_num += 1
            return True
        return False

    def group_battling(self):
        i = 0
        max_retry = int(self.config['retry'])
        while i < max_retry:
            if self.battling_num == self.battling_max_num:
                self.device.click(truncated_normal(360,1260), truncated_normal(76,730))
                return True
            max_num = self.basic_step.verify_batting_max_num()
            if max_num is None:
                time.sleep(0.5)
                continue
            max_num = max_num.replace('次','')
            if int(max_num) < max_retry:
                steps = [self.battling, self.battling_end]
                if self.execute_sequence(steps):
                    i += 1
        return False

    def receive(self):
        self.device.click(1436,825)
        time.sleep(1)
        self.device.click(truncated_normal(0,1600), truncated_normal(800,900))
        return True

    def run(self):
        self.return_main()
        steps = [
            self.entry_map,
            self.entry_martial_arts_map,
            self.verify_remaining,
            self.select_difficulty,
            self.click_next_difficulty,
            self.group_battling,
            self.receive,
        ]
        if self.execute_sequence(steps):
            self.return_main()
            self.result[MartialArtsKeys.NEXTTIME] = get_future_time(60*60*24)
            return self.result
        return False

if __name__=='__main__':
    d = DeviceOperator(DeviceManager('127.0.0.1:16416'))
    mart = MartialArts(d,{"difficulty":2, 'retry': 20})
    res = mart.run()
    print(res)
