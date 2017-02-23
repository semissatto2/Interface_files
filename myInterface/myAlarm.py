from epics import Alarm, poll
import datetime
import myExcel

alarm_count = 0
lista_alarms = [0]*len(myExcel.lista_alarmName)
pv_alarm_names = [0]*len(myExcel.lista_alarmName)
retorno = [0]*6

# Obtem os nome das PVs a partir dos nomes dos alarmes.
for i in range(len(myExcel.lista_alarmName)):
    pv_alarm_names[i] =  "IVUFE:EPS:" + myExcel.lista_alarmName[i]

'''
Trata o alarme. Retorna uma lista com :
 [      alarme disparado,   texto de alarme,    classe do alarme,   data,   hora,   contador de alarmes     ]
 '''
def alarmHandler(pvname=None, **kw):
    global alarm_count
    alarm_count += 1
    horario = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    campos = horario.split(' ')
    data = campos[0]
    hora = campos [1]
    pvname = pvname[10:]
    retorno = [pvname, myExcel.alarmText(pvname), myExcel.alarmClass(pvname), data, hora, alarm_count]
    print (alarm_count)
    #print ("%s  \nAlarm time: %s  \nIndex: %d \n" % (myExcel.alarmText(pvname), horario, alarm_count)) # Debbug    
    return retorno

'''
Cria um objeto Alarm.alarm do EPICS para cada nome de alarme lido da planilha do Excel.
'''
def createAlarms():
     print ("Creating alarms objects...")
     for i in range(len(myExcel.lista_alarmName)):
         lista_alarms[i] = Alarm(pvname= pv_alarm_names[i], comparison = 'eq', callback = alarmHandler, trip_point = 0, alert_delay = 1)
     print ("Alarms objects has been created.\n")

'''def alarmPoll():
    while True:
        poll()'''
