#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic, QtCore, QtGui, QtWidgets
import sys
import myAlarmHome
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
                if j == 4:
                    item.setText(str(data[i]))
                if j == 5:
                    item.setText(str(aux))
                    aux += 1                    
                self.tableWidget.setItem(aux,j, item)

    print ('Pass update AlarmScreen')


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
        i = 0
        while 1:
            myAlarmHome.alarmHandler(str(i))
            i += 1

            # Emit the signal

            counter = myAlarmHome.alarm_count
            data = myAlarmHome.data
            hora = myAlarmHome.hora
            texto = myAlarmHome.alarmText
            classe = myAlarmHome.alarmClass
            item_name = myAlarmHome.pvname
            self.sig.emit(
                counter,
                item_name,
                data,
                hora,
                classe,
                texto,
                )
            time.sleep(0.4)


# Init Interface

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AlarmScreen()
    window.show()
    sys.exit(app.exec_())

			
