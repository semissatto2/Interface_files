# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaInicial.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 243)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/logoSirius.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(26, 26))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.LinkButtonEPICS = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.LinkButtonEPICS.setAutoFillBackground(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/logo_659x595.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LinkButtonEPICS.setIcon(icon1)
        #self.LinkButtonEPICS.setIconSize(QtCore.QSize(30, 30))
        self.LinkButtonEPICS.setAutoExclusive(False)
        self.LinkButtonEPICS.setAutoDefault(False)
        self.LinkButtonEPICS.setDefault(True)
        self.LinkButtonEPICS.setObjectName("LinkButtonEPICS")
        self.verticalLayout.addWidget(self.LinkButtonEPICS)
        self.LinkButtonEPS = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.LinkButtonEPS.setObjectName("LinkButtonEPS")
        self.verticalLayout.addWidget(self.LinkButtonEPS)
        self.LinkButtonPPS = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.LinkButtonPPS.setObjectName("LinkButtonPPS")
        self.verticalLayout.addWidget(self.LinkButtonPPS)
        self.LinkButtonHVAC = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.LinkButtonHVAC.setObjectName("LinkButtonHVAC")
        self.verticalLayout.addWidget(self.LinkButtonHVAC)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 474, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela Inicial"))
        self.LinkButtonEPICS.setText(_translate("MainWindow", "EPICS Read interface"))
        self.LinkButtonEPS.setText(_translate("MainWindow", "EPS Interface"))
        self.LinkButtonPPS.setText(_translate("MainWindow", "PPS Interface"))
        self.LinkButtonHVAC.setText(_translate("MainWindow", "HVAC Interface"))

import resources_rc
