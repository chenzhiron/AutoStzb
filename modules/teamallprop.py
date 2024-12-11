from multiprocessing import Manager

#打城主力
besiegemain_state = 'besiegemain_state_state'
#打城拆迁
basiegedestory_state = 'basiegedestory_state'
#武勋
exploit_state = 'exploit_state'
#敌军主力
enemymain_state = 'enemymain_state'
#战场翻地/拆除
battledestory_state = 'battledestory_state'
#我方出战/防守
myfight_state = 'myfight_state'

def stTeamPropManger():
    data = Manager().dict({
        besiegemain_state: False,
        basiegedestory_state: False,
        exploit_state: False,
        enemymain_state: False,
        battledestory_state: False,
        myfight_state: False,  
    })
    return data

def updatecheckbox(obj, k, v):
    if len(v) == 0:
      result = False
    else:
      result = True
    
    obj[k] = result

def update(obj, k, v):
    obj[k] = v

stteamprop = stTeamPropManger()
