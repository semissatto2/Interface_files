# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Hello(object):
    def setupUi(self, Hello):
        Hello.setObjectName("Hello")
        Hello.resize(480, 215)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Hello)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 481, 216))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 0, 1, 1)
        self.pushButton_action = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_action.setFont(font)
        self.pushButton_action.setObjectName("pushButton_action")
        self.gridLayout_2.addWidget(self.pushButton_action, 4, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout_2.addWidget(self.pushButton_clear, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_2.addWidget(self.pushButton_close, 6, 0, 1, 1)

        self.retranslateUi(Hello)
        self.pushButton_clear.clicked.connect(self.lineEdit.clear)
        self.pushButton_close.clicked.connect(Hello.close)
        QtCore.QMetaObject.connectSlotsByName(Hello)

    def retranslateUi(self, Hello):
        _translate = QtCore.QCoreApplication.translate
        Hello.setWindowTitle(_translate("Hello", "Hello.ui @LNLS @GAE"))
        self.pushButton_action.setText(_translate("Hello", "Ler PV"))
        self.lineEdit.setText(_translate("Hello", "dasf"))
        self.pushButton_clear.setText(_translate("Hello", "Clear"))
        self.label_2.setText(_translate("Hello", "Valor da PV:"))
        self.label.setText(_translate("Hello", "Nome da PV:"))
        self.pushButton_close.setText(_translate("Hello", "Close"))

