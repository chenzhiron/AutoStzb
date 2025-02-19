version = '1.0.0'
tasks_config = {
    "simulator": {"address": "127.0.0.1:7885"},
    "besiege": {"state": False, "nexttime": "2019/06/01 00:00:00"},
    "exploit": {"state": False, "nexttime": "2019/06/01 00:00:00"},
    "enemy": {
        "state": False,
        "nexttime": "2019/06/01 00:00:00",
        "endtime": "2019/06/01 00:00:00",
        "looptime": 60,
    },
    "myfight": {
        "state": True,
        "nexttime": "2019/06/01 00:00:00",
        "endtime": "2019/06/01 00:00:00",
        "looptime": 0,
    },
    "ranking": {"state": False, "nexttime": "2019/06/01 00:00:00"},
    "battledestory": {
        "state": True,
        "nexttime": "2019/06/01 00:00:00",
        "endtime": "2019/06/01 00:00:00",
        "looptime": 60,
    },
}
