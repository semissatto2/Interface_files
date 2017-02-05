# hello_app_from_ui_mult.py

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
import sys

Ui_Form_telaInicial, QtBaseClass = uic.loadUiType("telaInicial.ui")
Ui_Form_epicsInterface, QtBaseClass = uic.loadUiType("epicsInterface.ui")

class TelaInicial(QMainWindow, Ui_Form_telaInicial):
    def __init__(self, parent=None):
        super(TelaInicial, self).__init__(parent)
        super(Ui_Form_telaInicial, self).__init__()
        self.setupUi(self)

        # Add things to my TelaInicial

        # Bind signal to slot
        self.LinkButtonEPICS.clicked.connect(self.onClick)

    # My slot
    def onClick(self):
        self.epicsInterface = EpicsInterface()
        self.epicsInterface.show()

class EpicsInterface(QWidget, Ui_Form_epicsInterface):
    def __init__(self, parent=None):
        super(EpicsInterface, self).__init__(parent)
        super(Ui_Form_epicsInterface, self).__init__()
        self.setupUi(self)

        # Bind signal to slot
        self.LinkButtonBack.clicked.connect(self.onClickBack)

    def onClickBack(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TelaInicial()
    window.show()
    sys.exit(app.exec_())