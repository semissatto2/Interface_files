# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableWidget.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(613, 349)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 491, 192))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Item"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Alarm Hour"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Alarm Text"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Alarm Class"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Alarm Date"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Index"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("Form", "TESTE0"))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("Form", "TESTE1"))
        item = self.tableWidget.item(6, 2)
        item.setText(_translate("Form", "TESTE2"))
        item = self.tableWidget.item(6, 3)
        item.setText(_translate("Form", "TESTE3"))
        item = self.tableWidget.item(6, 4)
        item.setText(_translate("Form", "TESTE4"))
        item = self.tableWidget.item(6, 5)
        item.setText(_translate("Form", "TESTE5"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

