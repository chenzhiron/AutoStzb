customConfig = {
    'TIMESLEEP': 1.0
}


def getTimeSleep():
    return customConfig['TIMESLEEP']


def setTimeSleep(v):
    try:
        if float(v) <= 0:
            v = 1
        customConfig['TIMESLEEP'] = float(v)
    except:
        customConfig['TIMESLEEP'] = 1.0
    return customConfig


def getCustomConfig():
    return customConfig
