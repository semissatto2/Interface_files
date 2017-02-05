# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'epicsInterface.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EPICSWindow(object):
    def setupUi(self, EPICSWindow):
        EPICSWindow.setObjectName("EPICSWindow")
        EPICSWindow.resize(591, 403)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/logo_659x595.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EPICSWindow.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(EPICSWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LinkButtonBack = QtWidgets.QCommandLinkButton(EPICSWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/green-back-button-icon-65921.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LinkButtonBack.setIcon(icon1)
        self.LinkButtonBack.setIconSize(QtCore.QSize(30, 30))
        self.LinkButtonBack.setObjectName("LinkButtonBack")
        self.horizontalLayout_2.addWidget(self.LinkButtonBack)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.logoSirius = QtWidgets.QLabel(EPICSWindow)
        self.logoSirius.setText("")
        self.logoSirius.setPixmap(QtGui.QPixmap(":/images/logoSirius.png"))
        self.logoSirius.setScaledContents(True)
        self.logoSirius.setAlignment(QtCore.Qt.AlignCenter)
        self.logoSirius.setObjectName("logoSirius")
        self.verticalLayout.addWidget(self.logoSirius)
        self.lineEdit_readPv = QtWidgets.QLineEdit(EPICSWindow)
        self.lineEdit_readPv.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_readPv.setPlaceholderText("Type PV name here")
        self.lineEdit_readPv.setObjectName("lineEdit_readPv")
        self.verticalLayout.addWidget(self.lineEdit_readPv)
        self.pushButton_readPv = QtWidgets.QPushButton(EPICSWindow)
        self.pushButton_readPv.setObjectName("pushButton_readPv")
        self.verticalLayout.addWidget(self.pushButton_readPv)
        self.lineEdit_PvValue = QtWidgets.QLineEdit(EPICSWindow)
        self.lineEdit_PvValue.setText("")
        self.lineEdit_PvValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_PvValue.setObjectName("lineEdit_PvValue")
        self.verticalLayout.addWidget(self.lineEdit_PvValue)
        self.pushButton_clear = QtWidgets.QPushButton(EPICSWindow)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.verticalLayout.addWidget(self.pushButton_clear)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(EPICSWindow)
        self.pushButton_clear.clicked.connect(self.lineEdit_readPv.clear)
        self.pushButton_clear.clicked.connect(self.lineEdit_PvValue.clear)
        QtCore.QMetaObject.connectSlotsByName(EPICSWindow)

    def retranslateUi(self, EPICSWindow):
        _translate = QtCore.QCoreApplication.translate
        EPICSWindow.setWindowTitle(_translate("EPICSWindow", "EPICS Interface"))
        self.LinkButtonBack.setText(_translate("EPICSWindow", "Back"))
        self.pushButton_readPv.setText(_translate("EPICSWindow", "Read PV Value"))
        self.lineEdit_PvValue.setPlaceholderText(_translate("EPICSWindow", "PV value"))
        self.pushButton_clear.setText(_translate("EPICSWindow", "Clear"))

import resources_rc
