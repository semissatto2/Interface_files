#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic, QtCore, QtGui, QtWidgets
import sys
import myAlarm
import time

# Load UI FIles

(Ui_Form_alarmScreen, QtBaseClass) = uic.loadUiType('alarmScreen.ui')


# Window #1 Class

class AlarmScreen(QWidget, Ui_Form_alarmScreen):

    def __init__(self, parent=None):
        super(AlarmScreen, self).__init__(parent)
        super(Ui_Form_alarmScreen, self).__init__()
        self.setupUi(self)

        # Add things to my WIndow

        self.threadclass = ThreadAlarmPoll()
        self.threadclass.start()

        # Binds signals  - slots

        self.threadclass.sig.connect(self.updateAlarmScreen)

    # My slots

    def updateAlarmScreen(
        self,
        counter,
        item_name,
        data,
        hora,
        classe,
        texto,
        ):
        
        aux = 0
        self.tableWidget.setRowCount(counter)
        for i in reversed(range(counter)):
            for j in range(6):
                item = QtWidgets.QTableWidgetItem()
                if j == 0:
                    item.setText(str(item_name[i]))
                if j == 1:
                    item.setText(str(hora[i]))
                if j == 2:
                    item.setText(str(texto[i]))
                if j == 3:
                    item.setText(str(classe[i]))
                    if classe[i] == 'Defeito':
                        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                        brush.setStyle(QtCore.Qt.SolidPattern)
                        item.setBackground(brush)
                    if classe[i] == 'Falha':
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                        brush.setStyle(QtCore.Qt.SolidPattern)
                        item.setBackground(brush)
                if j == 4:
                    item.setText(str(data[i]))
                if j == 5:
                    item.setText(str(aux))
                    aux += 1
                                       
                self.tableWidget.setItem(aux,j, item)



# My Thread Alarm Handler Class

class ThreadAlarmPoll(QtCore.QThread):

    # Create signals

    sig = QtCore.pyqtSignal(
        int,
        list,
        list,
        list,
        list,
        list,
        )

    def __init__(self, parent=None):
        super(ThreadAlarmPoll, self).__init__(parent)

    def run(self):
        myAlarm.createAlarms()
        while 1:
            
            #pass
            # Emit the signal if alarms was created with sucess
            if myAlarm.flag_alarmes_criados:
                counter = myAlarm.alarm_count
                data = myAlarm.data
                hora = myAlarm.hora
                texto = myAlarm.alarmText
                classe = myAlarm.alarmClass
                item_name = myAlarm.pv_names
                self.sig.emit(counter,item_name,data, hora,classe,texto)
                #print (counter)
            time.sleep(10)


# Init Interface

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AlarmScreen()
    window.show()
    sys.exit(app.exec_())

			
