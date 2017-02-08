import sys
from epics import PV
import random
import time

def getPvValue(pvName):
    pv = PV(pvName)
    if pv.connected:
        return pv.value
    else:
        return -1

def getRandom():
    return random.uniform(0,100)
    #time.sleep(1)
