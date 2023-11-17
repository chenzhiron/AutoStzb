customConfig = {
    'TIMESLEEP': 1
}


def getTimeSleep():
    return customConfig['TIMESLEEP']


def setTimeSleep(v):
    if float(v) < 0:
        v = 1
    customConfig['TIMESLEEP'] = float(v)
    return customConfig


def getCustomConfig():
    return customConfig
