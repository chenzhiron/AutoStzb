from multiprocessing import Manager
from .static.propname import *


def stPropManger():
    data = Manager().dict(
        {
            simulator_address: "127.0.0.1:16384",
            besiegemain_state: False,
            besiegemain_endtime: "2024/12/16 12:00:00",
            basiegedestory_state: False,
            basiegedestory_endtime: "2024/12/16 12:00:00",
            exploit_state: False,
            enemymain_state: False,
            enemymain_next_time: "2024/12/16 12:00:00",
            enemymain_endtime: "2024/12/16 12:00:00",
            battledestory_state: False,
            battledestory_next_time: "2024/12/16 12:00:00",
            battledestory_endtime: "2024/12/16 12:00:00",
            battledestory_looptime: 60,
            myfight_state: False,
            myfight_next_time: "2024/12/16 12:00:00",
            myfight_endtime: "2024/12/16 12:00:00",
            ranking_state: False,
        }
    )
    return data


def updatecheckbox(obj, k, v):
    if len(v) == 0:
        result = False
    else:
        result = True

    obj[k] = result


def update(obj, k, v):
    obj[k] = v
    print('k-v:', obj[k])

allprops = stPropManger()
