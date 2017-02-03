import sys
from epics import PV

def getPvValue(pvName):
    pv = PV(pvName)
    if pv.connected:
        return pv.value
    else:
        return -1
