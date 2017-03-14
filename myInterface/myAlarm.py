from epics import Alarm, poll
import datetime
import myExcel
import time

alarm_count = 0
flag_alarmes_criados = 0
lista_alarms = [0]*len(myExcel.lista_alarmName)
lista_alarms_positivos = [0]*len(myExcel.lista_alarmName)
pv_alarm_names = [0]*len(myExcel.lista_alarmName)
horario = []
pvname = []
#pv_names = []
data = list()
hora = list()
pv_names = list()
alarmText = list()
alarmClass = list()

# Obtem os nome das PVs a partir dos nomes dos alarmes.
for i in range(len(myExcel.lista_alarmName)):
    pv_alarm_names[i] =  "IVUFE:EPS:" + myExcel.lista_alarmName[i]

'''
Trata o alarme. Retorna uma lista com :
 [      alarme disparado,   texto de alarme,    classe do alarme,   data,   hora,   contador de alarmes     ]
 '''
def alarmHandler(pvname = None, **kw):
    global alarm_count, hora, data, pv_names, alarmText, alarmClass
    horario.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    campos = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").split(' ')
    data.append(campos[0])
    hora.append(campos [1])    
    pv_names.append(pvname[10:])    
    pvname= pvname[10:]
    alarmText.append(myExcel.alarmText(pvname))
    alarmClass.append(myExcel.alarmClass(pvname))
    alarm_count += 1

def alarmHandlerPositive(pvname = None, **kw):
    global alarm_count, hora, data, pv_names, alarmText, alarmClass
    horario.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    campos = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").split(' ')
    data.append(campos[0])
    hora.append(campos [1])    
    pv_names.append(pvname[10:])    
    pvname= pvname[10:]
    alarmText.append(myExcel.alarmText(pvname))
    alarmClass.append(myExcel.alarmClass(pvname)+' solved')
    alarm_count += 1    

'''
Cria um objeto Alarm.alarm do EPICS para cada nome de alarme lido da planilha do Excel.
'''
def createAlarms():
     print ("Creating alarms objects...")
     global flag_alarmes_criados
     flag_alarmes_criados = 0     
     for i in range(len(myExcel.lista_alarmName)):
         lista_alarms[i] = Alarm(pvname= pv_alarm_names[i], comparison = 'eq', callback = alarmHandler, trip_point = 0, alert_delay = 0.1)
         lista_alarms_positivos[i] =  Alarm(pvname= pv_alarm_names[i], comparison = 'eq', callback = alarmHandlerPositive, trip_point = 1, alert_delay = 0.1)
     flag_alarmes_criados = 1
     print ("Alarms objects has been created.\n")

'''
Alarm poll(). Não sei exatamente o uso disto. Ler doc. EPICS
'''
def alarmPoll():
    while True:
        poll()


