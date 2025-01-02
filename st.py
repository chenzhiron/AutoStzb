import time
from modules.log import *


class St:
    def __init__(self):
        pass

    def get_next_task(self):
        from modules.web.taskState import TaskReadManager

        return TaskReadManager().get_next_task()

    def devices(self, config):
        from modules.devices.main import Devices

        d = Devices(config).d
        return d

    def exploit(self, d, config):
        from modules.taskfn.exploit import Exploit

        Exploit(d, config).execute()

    def fliplists(self, d, config):
        from modules.taskfn.flip_lists import FlipLists

        FlipLists(d, config).execute()

    def ranking(self, d, config):
        from modules.taskfn.ranking import Ranking

        Ranking(d, config).execute()

    def rolelists(self, d, config):
        from modules.taskfn.role_lists import role_lists

        pass

    def siegebattles(self, d, config):
        from modules.taskfn.siege_battles import SiegeBattles

        SiegeBattles(d, config).execute()

    def loop(self):
        while True:
            v = self.get_next_task()
            if v is None:
                continue

            info("Task: %s" % v)
            time.sleep(1)
