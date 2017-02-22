import pyexcel as pe

records = pe.iget_records(file_name="Tabela_AlarmeEPICS.xls")
lista_alarmName = []
lista_alarmText = []
lista_alarmClass = []

for record in records:
    lista_alarmName.append(record['Name'])
    lista_alarmText.append(record['Alarm text [en-US], Alarm text'])
    lista_alarmClass.append(record['Class'])

def getAlarmClass(name):
    return lista_alarmClass[lista_alarmName.index(name)]

def getAlarmText(name):
    return lista_alarmText[lista_alarmName.index(name)]
