# hello_app_from_ui_mult.py

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLabel
from PyQt5 import uic, QtGui, QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal
import sys
import myEpics
from epics import caget, PV


Ui_Form, QtBaseClass = uic.loadUiType("hello.ui")

class MainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.threadclass = ThreadClass()
        self.threadclass.start()

        # Add interface objects
        
        # Bind signal to method
        self.pushButton_action.clicked.connect(self.myAction)
        self.pushButton_clear.clicked.connect(self.lineEdit_2.clear)
        self.threadclass.sig.connect(self.updateStatusLinha)

    @pyqtSlot(int, int, int)
    def updateStatusLinha(self, val_bool_0 , val_word_1, val_real_1):        
        if val_bool_0 > 0:
            self.status_linha_1.setPixmap(QtGui.QPixmap("led_green.png"))
        else:
            self.status_linha_1.setPixmap(QtGui.QPixmap("led_red.png"))
        
        if val_word_1 > 0:
            self.status_linha_2.setPixmap(QtGui.QPixmap("led_green.png"))
        else:
            self.status_linha_2.setPixmap(QtGui.QPixmap("led_red.png"))
            
        if val_real_1 > 0:
            self.status_linha_3.setPixmap(QtGui.QPixmap("led_green.png"))
        else:
            self.status_linha_3.setPixmap(QtGui.QPixmap("led_red.png"))

    def myAction(self):
         nome_da_pv = self.lineEdit.text()
         if nome_da_pv != '':
             pv = PV(nome_da_pv)
             if pv.connected:
                      pv_value = str(float(pv.value/10))
                      self.lineEdit_2.setText(pv_value)
             else:
                      self.lineEdit_2.setText('PV not connected')

class ThreadClass(QtCore.QThread):
    # Create the signal
    sig = QtCore.pyqtSignal(int, int, int)
    
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)
        
    def run(self):
        while 1:
            val_bool_0 = myEpics.getPvValue('IVUFE:EPS:bool_0')
            val_word_1= myEpics.getPvValue('IVUFE:EPS:word1')
            val_real_1= myEpics.getPvValue('IVUFE:EPS:real1')
            
            # Emit the signal
            self.sig.emit(val_bool_0, val_word_1, val_real_1)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
