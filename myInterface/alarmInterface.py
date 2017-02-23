from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic, QtCore, QtGui, QtWidgets
import sys
import myAlarm

#Load UI FIles
Ui_Form_alarmScreen, QtBaseClass = uic.loadUiType("alarmScreen.ui")

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
    def updateAlarmScreen(self, myAlarmHandler()):
        pass  # Deve ter toda logica de atualizacao da tabela
    
# My Thread Alarm Handler Class
class ThreadAlarmPoll(QtCore.QThread):
    # Create signals
    sig = QtCore.pyqtSignal(list)
    
    def __init__(self, parent = None):
        super(ThreadAlarmPoll, self).__init__(parent)

    def run(self):
        myAlarm.alarmPoll()

        #Emit the signal
        self.sig.emit(myAlarm.alarmHandler())

# Init Interface
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AlarmSCreen()
    window.show()
    sys.exit(app_exec_())
