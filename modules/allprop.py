from multiprocessing import Manager
from .static.propname import *

def stPropManger():
    data = Manager().dict({
        simulator_address: '127.0.0.1:16384',
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

allprops = stPropManger()
