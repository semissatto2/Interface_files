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
Ui_Form_TempScreen, QtBaseClass = uic.loadUiType("TempScreen.ui")

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

       # Set things to my Window
        self.labelAI1.setText(myEpics.pv1.pvname)
        self.labelAI2.setText(myEpics.pv2.pvname)
        self.labelAI3.setText(myEpics.pv3.pvname)
        self.labelAI4.setText(myEpics.pv4.pvname)
        self.labelAI5.setText(myEpics.pv5.pvname)
        self.labelAI6.setText(myEpics.pv6.pvname)
        self.labelAI7.setText(myEpics.pv7.pvname)
        self.labelAI8.setText(myEpics.pv8.pvname)
        self.labelAI9.setText(myEpics.pv9.pvname)
        self.labelAI10.setText(myEpics.pv10.pvname)
        self.labelAI11.setText(myEpics.pv11.pvname)
        self.labelAI12.setText(myEpics.pv12.pvname)
        self.labelAI13.setText(myEpics.pv13.pvname)
        self.labelAI14.setText(myEpics.pv14.pvname)
        self.labelAI15.setText(myEpics.pv15.pvname)
        self.labelAI16.setText(myEpics.pv16.pvname)
        self.labelAI17.setText(myEpics.pv17.pvname)
        self.labelAI18.setText(myEpics.pv18.pvname)
        self.labelAI19.setText(myEpics.pv19.pvname)
        self.labelAI20.setText(myEpics.pv20.pvname)
        self.labelAI21.setText(myEpics.pv21.pvname)
        self.labelAI22.setText(myEpics.pv22.pvname)
        self.labelAI23.setText(myEpics.pv23.pvname)
        self.labelAI24.setText(myEpics.pv24.pvname)
        self.labelAI25.setText(myEpics.pv25.pvname)
        self.labelAI26.setText(myEpics.pv26.pvname)
        self.labelAI27.setText(myEpics.pv27.pvname)
        self.labelAI28.setText(myEpics.pv28.pvname)
        self.labelAI29.setText(myEpics.pv29.pvname)
        self.labelAI30.setText(myEpics.pv30.pvname)
        self.labelAI31.setText(myEpics.pv31.pvname)
        self.labelAI32.setText(myEpics.pv32.pvname)
        
       # Bind signal to method
        self.threadclass.sig.connect(self.updateAI)
        self.LinkButtonBackEPS.clicked.connect(self.onClickBack)
    
    def onClickBack(self):
        self.close()
        self.window = TelaInicial()
        self.window.show()

    def updateAI(self, AI1, AI2, AI3, AI4,AI5, AI6, AI7, AI8,AI9, AI10, AI11, AI12,AI13, AI14, AI15, AI16,AI17, AI18, AI19, AI20,AI21, AI22, AI23, AI24,AI25, AI26, AI27, AI28,AI29, AI30, AI31, AI32):
        self.lineEditAI1.setText(str(AI1))
        self.lineEditAI2.setText(str(AI2))
        self.lineEditAI3.setText(str(AI3))
        self.lineEditAI4.setText(str(AI4))
        self.lineEditAI5.setText(str(AI5))
        self.lineEditAI6.setText(str(AI6))
        self.lineEditAI7.setText(str(AI7))
        self.lineEditAI8.setText(str(AI8))
        self.lineEditAI9.setText(str(AI9))
        self.lineEditAI10.setText(str(AI10))
        self.lineEditAI11.setText(str(AI11))
        self.lineEditAI12.setText(str(AI12))
        self.lineEditAI13.setText(str(AI13))
        self.lineEditAI14.setText(str(AI14))
        self.lineEditAI15.setText(str(AI15))
        self.lineEditAI16.setText(str(AI16))
        self.lineEditAI17.setText(str(AI17))
        self.lineEditAI18.setText(str(AI18))
        self.lineEditAI19.setText(str(AI19))
        self.lineEditAI20.setText(str(AI20))
        self.lineEditAI21.setText(str(AI21))
        self.lineEditAI22.setText(str(AI22))
        self.lineEditAI23.setText(str(AI23))
        self.lineEditAI24.setText(str(AI24))
        self.lineEditAI25.setText(str(AI25))
        self.lineEditAI26.setText(str(AI26))
        self.lineEditAI27.setText(str(AI27))
        self.lineEditAI28.setText(str(AI28))
        self.lineEditAI29.setText(str(AI29))
        self.lineEditAI30.setText(str(AI30))
        self.lineEditAI31.setText(str(AI31))
        self.lineEditAI32.setText(str(AI32))

# Window #4 Class
class TempScreen(QWidget, Ui_Form_TempScreen):
    def __init__(self, parent=None):
        super(TempScreen, self).__init__(parent)
        super(Ui_Form_EPSInterface, self).__init__()
        self.setupUi(self)

        # Add things to my Window
        self.threadclass = ThreadClass()
        self.threadclass.start()

       # Set things to my Window
        self.labelAI1.setText(myEpics.pv1.pvname)

        
       # Bind signal to method
        self.threadclass.sig.connect(self.updateAI)
    
    def onClickBack(self):
        self.close()
        self.window = TelaInicial()
        self.window.show()

    def updateAI(self, AI1, AI2, AI3, AI4,AI5, AI6, AI7, AI8,AI9, AI10, AI11, AI12,AI13, AI14, AI15, AI16,AI17, AI18, AI19, AI20,AI21, AI22, AI23, AI24,AI25, AI26, AI27, AI28,AI29, AI30, AI31, AI32):
        self.lineEditAI1.setText(str(AI1))
        self.lineEditAI2.setText(str(AI2))
        self.lineEditAI3.setText(str(AI3))
        self.lineEditAI4.setText(str(AI4))
        self.lineEditAI5.setText(str(AI5))
        self.lineEditAI6.setText(str(AI6))
        self.lineEditAI7.setText(str(AI7))
        self.lineEditAI8.setText(str(AI8))
        self.lineEditAI9.setText(str(AI9))
        self.lineEditAI10.setText(str(AI10))
        self.lineEditAI11.setText(str(AI11))
        self.lineEditAI12.setText(str(AI12))
        self.lineEditAI13.setText(str(AI13))
        self.lineEditAI14.setText(str(AI14))
        self.lineEditAI15.setText(str(AI15))
        self.lineEditAI16.setText(str(AI16))
        self.lineEditAI17.setText(str(AI17))
        self.lineEditAI18.setText(str(AI18))
        self.lineEditAI19.setText(str(AI19))
        self.lineEditAI20.setText(str(AI20))
        self.lineEditAI21.setText(str(AI21))
        self.lineEditAI22.setText(str(AI22))
        self.lineEditAI23.setText(str(AI23))
        self.lineEditAI24.setText(str(AI24))
        self.lineEditAI25.setText(str(AI25))
        self.lineEditAI26.setText(str(AI26))
        self.lineEditAI27.setText(str(AI27))
        self.lineEditAI28.setText(str(AI28))
        self.lineEditAI29.setText(str(AI29))
        self.lineEditAI30.setText(str(AI30))
        self.lineEditAI31.setText(str(AI31))
        self.lineEditAI32.setText(str(AI32))
        
class ThreadClass(QtCore.QThread):
    # Create the signal
    sig = QtCore.pyqtSignal(float, float, float, float,float, float, float, float,float, float, float, float,float, float, float, float,float, float, float, float,float, float, float, float,float, float, float, float,float, float, float, float)
    
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)
        
    def run(self):
        while 1:
            AI1 = myEpics.readAIValues()[0]
            AI2 = myEpics.readAIValues()[1]
            AI3 = myEpics.readAIValues()[2]
            AI4 = myEpics.readAIValues()[3]
            AI5 = myEpics.readAIValues()[4]
            AI6 = myEpics.readAIValues()[5]
            AI7 = myEpics.readAIValues()[6]
            AI8 = myEpics.readAIValues()[7]
            AI9 = myEpics.readAIValues()[8]
            AI10 = myEpics.readAIValues()[9]
            AI11 = myEpics.readAIValues()[10]
            AI12= myEpics.readAIValues()[11]
            AI13 = myEpics.readAIValues()[12]
            AI14 = myEpics.readAIValues()[13]
            AI15 = myEpics.readAIValues()[14]
            AI16 = myEpics.readAIValues()[15]
            AI17 = myEpics.readAIValues()[16]
            AI18 = myEpics.readAIValues()[17]
            AI19 = myEpics.readAIValues()[18]
            AI20 = myEpics.readAIValues()[19]
            AI21 = myEpics.readAIValues()[20]
            AI22 = myEpics.readAIValues()[21]
            AI23 = myEpics.readAIValues()[22]
            AI24 = myEpics.readAIValues()[23]
            AI25 = myEpics.readAIValues()[24]
            AI26 = myEpics.readAIValues()[25]
            AI27 = myEpics.readAIValues()[26]
            AI28= myEpics.readAIValues()[27]
            AI29 = myEpics.readAIValues()[28]
            AI30 = myEpics.readAIValues()[29]
            AI31 = myEpics.readAIValues()[30]
            AI32 = myEpics.readAIValues()[31]
            time.sleep(0.4)


            
            # Emit the signal
            self.sig.emit(AI1, AI2, AI3, AI4,AI5, AI6, AI7, AI8,AI9, AI10, AI11, AI12,AI13, AI14, AI15, AI16,AI17, AI18, AI19, AI20,AI21, AI22, AI23, AI24,AI25, AI26, AI27, AI28,AI29, AI30, AI31, AI32)

# Init interface
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TelaInicial()
    window.show()
    sys.exit(app.exec_())
