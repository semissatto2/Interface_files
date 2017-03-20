#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import myEpics
import sys
import time

# Load UI Files
Ui_Form_siriusScreen, QtBaseClass = uic.loadUiType("SiriusScreen.ui")
Ui_Form_ppsScreen, QtBaseClass = uic.loadUiType("PPSScreen.ui")

# Window #1 SIRIUS OVERVIEW
class SiriusScreen(QWidget, Ui_Form_siriusScreen):
    def __init__(self, parent=None):
        super(SiriusScreen, self).__init__(parent)
        super(Ui_Form_siriusScreen, self).__init__()
        self.setupUi(self)

        # Add things to my Window
        self.threadclass = ThreadClass()
        self.threadclass.start()
        #self.setGeometry(54,-8,1538,878)
        
       # Set things to my Window
        
       # Bind signal to method
        self.pushButton.clicked.connect(self.onClick)
        self.threadclass.sig.connect(self.updateScreen)
    
    def onClick(self):
        #self.close()
        self.window = PPSScreen()
        self.window.show()

    def updateScreen(self, corrente, tempovida, temporeal):
        self.lineEditCurrent.setText(corrente+" mA")
        self.lineEditLifetime.setText(tempovida+" H")
        self.lineEditTime.setText(temporeal)
        

class ThreadClass(QtCore.QThread):
    # Create the signal
    sig = QtCore.pyqtSignal(str,str,str)
    
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)
        
    def run(self):
        corrente =  str(myEpics.pv[330].value)
        tempovida = myEpics.pv[331].value
        temporeal = myEpics.pv[332].value
        
        while 1:
            corrente =  str(myEpics.pv[330].value)
            tempovida = myEpics.pv[331].value
            temporeal = myEpics.pv[332].value
            #print ("Thread emits")
            #corrente =  '212'
            #tempovida = '18:15'
            #temporeal = '20:15:08'            
            time.sleep(0.2)
       
            # Emit the signal
            self.sig.emit(corrente, tempovida, temporeal)

# Window #1 SIRIUS OVERVIEW
class PPSScreen(QWidget, Ui_Form_ppsScreen):
    def __init__(self, parent=None):
        super(PPSScreen, self).__init__(parent)
        super(Ui_Form_ppsScreen, self).__init__()
        self.setupUi(self)

        # Add things to my Window
        #self.setGeometry(54,-8,1538,878)
        
       # Set things to my Window
        
       # Bind signal to method
        self.pushButtonBack.clicked.connect(self.onClick)
    
    def onClick(self):
        self.close()

# Init interface
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SiriusScreen()
    window.show()
    sys.exit(app.exec_())        
