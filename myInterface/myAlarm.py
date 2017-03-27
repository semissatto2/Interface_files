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
IOC_recem_criada = False
data = list()
hora = list()
pv_names = list()
alarmText = list()
alarmClass = list()
tempo_total_list = list()

# Obtem os nome das PVs a partir dos nomes dos alarmes.
for i in range(len(myExcel.lista_alarmName)):
    pv_alarm_names[i] =  "IVUFE:EPS:" + myExcel.lista_alarmName[i]

'''
Trata os alarmes de estado de falha. Retorna lista incremental com informacoes do alarme de cada hora :
 '''
def alarmHandler(pvname = None, **kw):
    global alarm_count, hora, data, pv_names, alarmText, alarmClass, tempo_total_list

    horario.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    campos = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").split(' ')
    data.append(campos[0])
    hora.append(campos [1])    
    pv_names.append(pvname[10:])    
    pvname= pvname[10:]
    alarmText.append(myExcel.alarmText(pvname))
    alarmClass.append(myExcel.alarmClass(pvname))


    Y = int(datetime.datetime.now().strftime("%Y"))
    month = int(datetime.datetime.now().strftime("%m"))
    d = int(datetime.datetime.now().strftime("%d"))
    H = int(datetime.datetime.now().strftime("%H"))
    minute = int(datetime.datetime.now().strftime("%M"))
    S = int(datetime.datetime.now().strftime("%S"))
    tempo_total = (Y-2000)*365*24 + d*24 + month*30*24 + H + minute/60 + S/3600
    tempo_total_list.append(tempo_total)
    
    alarm_count += 1
    print ("alarm_count = ", alarm_count)
    
'''
Trata os alarmes de estado de recuperacao de falha. Retorna lista incremental com informacoes do alarme de cada hora :
 '''
def alarmHandlerPositive(pvname = None, **kw):
    print ("IOC_recem_criada = ", IOC_recem_criada)
    if IOC_recem_criada == False:
        global alarm_count, hora, data, pv_names, alarmText, alarmClass, tempo_total_list
        
        horario.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        campos = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").split(' ')
        data.append(campos[0])
        hora.append(campos [1])    
        pv_names.append(pvname[10:])    
        pvname= pvname[10:]
        alarmText.append(myExcel.alarmText(pvname))
        alarmClass.append(myExcel.alarmClass(pvname)+' solved')

        Y = int(datetime.datetime.now().strftime("%Y"))
        month = int(datetime.datetime.now().strftime("%m"))
        d = int(datetime.datetime.now().strftime("%d"))
        H = int(datetime.datetime.now().strftime("%H"))
        minute = int(datetime.datetime.now().strftime("%M"))
        S = int(datetime.datetime.now().strftime("%S"))
        tempo_total = (Y-2000)*365*24 + d*24 + month*30*24 + H + minute/60 + S/3600
        tempo_total_list.append(tempo_total)
    
        alarm_count += 1
        print ("alarm_count = ", alarm_count)
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

def recebeInt( Int ):
    global IOC_recem_criada
    IOC_recem_criada = Int
    

