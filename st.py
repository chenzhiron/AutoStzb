import time

from modules.log import info
from modules.static.propname import *


class St:
    def __init__(self, teamprop):
        self.teamdata = teamprop
        self.handlesMap = {
            besiegemain_state: self.siegebattles,
            basiegedestory_state: self.siegebattles,
            exploit_state: self.exploit,
            # enemymain_state: self.en,
            battledestory_state: self.fliplists,
            ranking_state: self.ranking,
            # myfight_state: self.
        }

    def devices(self, config):
        from modules.devices.main import Devices

        d = Devices(config).d
        return d

    def exploit(self, d, config):
        from modules.taskfn.exploit import Exploit

        Exploit(d).execute()
        config[exploit_state] = False

    def fliplists(self, d, config):
        from modules.taskfn.flip_lists import FlipLists
        end_time = config[battledestory_endtime]
        FlipLists(d, end_time).execute()
        config[battledestory_state] = False

    def ranking(self, d, config):
        from modules.taskfn.ranking import Ranking
        Ranking(d).execute()
        config[ranking_state] = False

    def rolelists(self, d, config):
        from modules.taskfn.role_lists import role_lists

        pass

    def siegebattles(self, d, config):
        from modules.taskfn.siege_battles import SiegeBattles
        end_time = config[battledestory_endtime]
        SiegeBattles(d, end_time).execute()
        config[besiegemain_state] = False

    def loop(self):
        while True:
            for key, func in self.handlesMap.items():
                if self.teamdata[key]:
                    d = self.devices(self.teamdata[simulator_address])
                    func(d, self.teamdata)
                    self.teamdata[key] = False
            time.sleep(1)
