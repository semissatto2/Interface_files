# hello_app_from_ui_mult.py

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic, QtCore
import sys
from epics import caget, PV
import myEpics
import time

# Load UI Files
Ui_Form_telaInicial, QtBaseClass = uic.loadUiType("telaInicial.ui")
Ui_Form_epicsInterface, QtBaseClass = uic.loadUiType("epicsInterface.ui")
Ui_Form_EPSInterface, QtBaseClass = uic.loadUiType("EPSInterface.ui")

# Window #1 Class
class TelaInicial(QMainWindow, Ui_Form_telaInicial):
    def __init__(self, parent=None):
        super(TelaInicial, self).__init__(parent)
        super(Ui_Form_telaInicial, self).__init__()
        self.setupUi(self)

        # Add things to my TelaInicial

        # Bind signal to slot
        self.LinkButtonEPICS.clicked.connect(self.openEPICS)
        self.LinkButtonEPS.clicked.connect(self.openEPS)



    # My slot's
    def openEPICS(self):
        self.epicsInterface = EpicsInterface()
        self.epicsInterface.show()
        self.close()

    def openEPS(self):
        self.EPSInterface = EPSInterface()
        self.EPSInterface.show()
        self.close()

# Window #2 Class
class EpicsInterface(QWidget, Ui_Form_epicsInterface):
    def __init__(self, parent=None):
        super(EpicsInterface, self).__init__(parent)
        super(Ui_Form_epicsInterface, self).__init__()
        self.setupUi(self)

        # Bind signal to slot
        self.LinkButtonBack.clicked.connect(self.onClickBack)
        self.pushButton_readPv.clicked.connect(self.readPv)
        
    # My slot's
    def onClickBack(self):
        self.close()
        self.window = TelaInicial()
        self.window.show()
        
    def readPv(self):
         nome_da_pv = self.lineEdit_readPv.text()
         if nome_da_pv != '':
             pv = PV(nome_da_pv)
             if pv.connected:
                      pv_value = str(float(pv.value/10))
                      self.lineEdit_PvValue.setText(pv_value)
             else:
                      self.lineEdit_PvValue.setText('PV not connected')
        
# Window #3 Class
class EPSInterface(QWidget, Ui_Form_EPSInterface):
    def __init__(self, parent=None):
        super(EPSInterface, self).__init__(parent)
        super(Ui_Form_EPSInterface, self).__init__()
        self.setupUi(self)

        # Add things to my Window
        self.threadclass = ThreadClass()
        self.threadclass.start()

	# Bind signal to method
        self.threadclass.sig.connect(self.updateAI)
        self.LinkButtonBackEPS.clicked.connect(self.onClickBack)
	
    def onClickBack(self):
		self.close()
		self.window = TelaInicial()
		self.window.show()
		
    def updateAI(self, AI1, AI2, AI3, AI4):
        self.lineEditAI1.setText(str(AI1))
        self.lineEditAI2.setText(str(AI2))
        self.lineEditAI3.setText(str(AI3))
        self.lineEditAI4.setText(str(AI4))

class ThreadClass(QtCore.QThread):
    # Create the signal
    sig = QtCore.pyqtSignal(float, float, float, float)
    
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)
        
    def run(self):
        while 1:
            AI1 = myEpics.readAIValues()[0]
            AI2 = myEpics.readAIValues()[1]
            AI3 = myEpics.readAIValues()[2]
            AI4 = myEpics.readAIValues()[3]
            time.sleep(0.4)


            
            # Emit the signal
            self.sig.emit(AI1, AI2, AI3, AI4)

# Init interface
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TelaInicial()
    window.show()
    sys.exit(app.exec_())
