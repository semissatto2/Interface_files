import datetime

alarm_count = 0
hora = list()
data = list()
pvname = list()
alarmText = list()
alarmClass = list()


'''
Trata o alarme. Retorna uma lista com :
 [      alarme disparado,   texto de alarme,    classe do alarme,   data,   hora,   contador de alarmes     ]
 '''
def alarmHandler(parameter = None):
    global alarm_count, hora, data, pvname, alarmText, alarmClass
    horario = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    campos = horario.split(' ')
    data.append(campos[0])
    hora.append(campos[1])
    pvname.append(parameter)
    alarmText.append(parameter)
    alarmClass.append(parameter)
    alarm_count += 1


