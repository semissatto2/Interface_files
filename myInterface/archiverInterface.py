# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'archiverInterface.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(756, 525)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonBack = QtWidgets.QPushButton(Form)
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.gridLayout.addWidget(self.pushButtonBack, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(284, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(284, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 20))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonBackURL = QtWidgets.QPushButton(self.widget)
        self.pushButtonBackURL.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButtonBackURL.setObjectName("pushButtonBackURL")
        self.horizontalLayout.addWidget(self.pushButtonBackURL)
        self.pushButtonForwardURL = QtWidgets.QPushButton(self.widget)
        self.pushButtonForwardURL.setMaximumSize(QtCore.QSize(16777215, 18))
        self.pushButtonForwardURL.setObjectName("pushButtonForwardURL")
        self.horizontalLayout.addWidget(self.pushButtonForwardURL)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 2)
        self.webView = QtWebKitWidgets.QWebView(Form)
        self.webView.setProperty("url", QtCore.QUrl("http://10.2.105.191"))
        self.webView.setObjectName("webView")
        self.gridLayout.addWidget(self.webView, 2, 0, 1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButtonBack.setText(_translate("Form", "BACK"))
        self.label.setText(_translate("Form", "Archiver"))
        self.pushButtonBackURL.setText(_translate("Form", "BACK"))
        self.pushButtonForwardURL.setText(_translate("Form", "FORWARD"))

from PyQt5 import QtWebKitWidgets
