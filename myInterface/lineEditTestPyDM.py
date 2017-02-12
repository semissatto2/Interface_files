# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lineEditTestPyDM.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(560, 379)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 11, 423, 351))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setStyleSheet("color: rgb(30, 30, 30);\n"
"font: 75 25pt \"Utopia\";\n"
"background-color: transparent;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.PyDMLineEdit = PyDMLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Utopia")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.PyDMLineEdit.setFont(font)
        self.PyDMLineEdit.setToolTip("")
        self.PyDMLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.PyDMLineEdit.setReadOnly(True)
        self.PyDMLineEdit.setObjectName("PyDMLineEdit")
        self.horizontalLayout.addWidget(self.PyDMLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.PyDMTimePlot = PyDMTimePlot(self.widget)
        self.PyDMTimePlot.setToolTip("")
        self.PyDMTimePlot.setWhatsThis("")
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.PyDMTimePlot.setBackgroundBrush(brush)
        self.PyDMTimePlot.setCurveColor(QtGui.QColor(0, 0, 0))
        self.PyDMTimePlot.setAxisColor(QtGui.QColor(0, 0, 0))
        self.PyDMTimePlot.setUpdatesAsynchronously(True)
        self.PyDMTimePlot.setTimeSpan(50.0)
        self.PyDMTimePlot.setObjectName("PyDMTimePlot")
        self.verticalLayout.addWidget(self.PyDMTimePlot)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_11.setText(_translate("Form", "WRT-FIT"))
        self.PyDMLineEdit.setWhatsThis(_translate("Form", "\n"
"    Writeable text field to send and display channel values\n"
"    "))
        self.PyDMLineEdit.setProperty("channel", _translate("Form", "ca://IVUFE:EPS:AS_UTL-WRT-FIT "))
        self.PyDMTimePlot.setProperty("title", _translate("Form", "IVUFE:EPS:WPR-FIT"))
        self.PyDMTimePlot.setYChannel(_translate("Form", "ca://IVUFE:EPS:AS_UTL-WRT-FIT "))

from pydm.widgets.line_edit import PyDMLineEdit
from pydm.widgets.timeplot import PyDMTimePlot
