# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EPSInterface.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EPSInterface(object):
    def setupUi(self, EPSInterface):
        EPSInterface.setObjectName("EPSInterface")
        EPSInterface.resize(882, 677)
        EPSInterface.setAutoFillBackground(False)
        EPSInterface.setStyleSheet("background-image: url(:/images/fundoEscuro.png);")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(EPSInterface)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LinkButtonBackEPS = QtWidgets.QCommandLinkButton(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LinkButtonBackEPS.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/green-back-button-icon-65921.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LinkButtonBackEPS.setIcon(icon)
        self.LinkButtonBackEPS.setIconSize(QtCore.QSize(30, 30))
        self.LinkButtonBackEPS.setObjectName("LinkButtonBackEPS")
        self.horizontalLayout.addWidget(self.LinkButtonBackEPS)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.labelAI1 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI1.setFont(font)
        self.labelAI1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI1.setObjectName("labelAI1")
        self.verticalLayout_9.addWidget(self.labelAI1)
        self.lineEditAI1 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI1.setFont(font)
        self.lineEditAI1.setAutoFillBackground(False)
        self.lineEditAI1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI1.setReadOnly(True)
        self.lineEditAI1.setObjectName("lineEditAI1")
        self.verticalLayout_9.addWidget(self.lineEditAI1)
        self.labelAI2 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI2.setFont(font)
        self.labelAI2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI2.setObjectName("labelAI2")
        self.verticalLayout_9.addWidget(self.labelAI2)
        self.lineEditAI2 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI2.setFont(font)
        self.lineEditAI2.setAutoFillBackground(False)
        self.lineEditAI2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI2.setReadOnly(True)
        self.lineEditAI2.setObjectName("lineEditAI2")
        self.verticalLayout_9.addWidget(self.lineEditAI2)
        self.labelAI3 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI3.setFont(font)
        self.labelAI3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI3.setObjectName("labelAI3")
        self.verticalLayout_9.addWidget(self.labelAI3)
        self.lineEditAI3 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI3.setFont(font)
        self.lineEditAI3.setAutoFillBackground(False)
        self.lineEditAI3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI3.setReadOnly(True)
        self.lineEditAI3.setObjectName("lineEditAI3")
        self.verticalLayout_9.addWidget(self.lineEditAI3)
        self.labelAI4 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI4.setFont(font)
        self.labelAI4.setMouseTracking(False)
        self.labelAI4.setAcceptDrops(True)
        self.labelAI4.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI4.setObjectName("labelAI4")
        self.verticalLayout_9.addWidget(self.labelAI4)
        self.lineEditAI4 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI4.setFont(font)
        self.lineEditAI4.setAutoFillBackground(False)
        self.lineEditAI4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI4.setReadOnly(True)
        self.lineEditAI4.setObjectName("lineEditAI4")
        self.verticalLayout_9.addWidget(self.lineEditAI4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.labelAI5 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI5.setFont(font)
        self.labelAI5.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI5.setObjectName("labelAI5")
        self.verticalLayout_8.addWidget(self.labelAI5)
        self.lineEditAI5 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI5.setFont(font)
        self.lineEditAI5.setAutoFillBackground(False)
        self.lineEditAI5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI5.setReadOnly(True)
        self.lineEditAI5.setObjectName("lineEditAI5")
        self.verticalLayout_8.addWidget(self.lineEditAI5)
        self.labelAI6 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI6.setFont(font)
        self.labelAI6.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI6.setObjectName("labelAI6")
        self.verticalLayout_8.addWidget(self.labelAI6)
        self.lineEditAI6 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI6.setFont(font)
        self.lineEditAI6.setAutoFillBackground(False)
        self.lineEditAI6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI6.setReadOnly(True)
        self.lineEditAI6.setObjectName("lineEditAI6")
        self.verticalLayout_8.addWidget(self.lineEditAI6)
        self.labelAI7 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI7.setFont(font)
        self.labelAI7.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI7.setObjectName("labelAI7")
        self.verticalLayout_8.addWidget(self.labelAI7)
        self.lineEditAI7 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI7.setFont(font)
        self.lineEditAI7.setAutoFillBackground(False)
        self.lineEditAI7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI7.setReadOnly(True)
        self.lineEditAI7.setObjectName("lineEditAI7")
        self.verticalLayout_8.addWidget(self.lineEditAI7)
        self.labelAI8 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI8.setFont(font)
        self.labelAI8.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI8.setObjectName("labelAI8")
        self.verticalLayout_8.addWidget(self.labelAI8)
        self.lineEditAI8 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI8.setFont(font)
        self.lineEditAI8.setAutoFillBackground(False)
        self.lineEditAI8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI8.setReadOnly(True)
        self.lineEditAI8.setObjectName("lineEditAI8")
        self.verticalLayout_8.addWidget(self.lineEditAI8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelAI9 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI9.setFont(font)
        self.labelAI9.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI9.setObjectName("labelAI9")
        self.verticalLayout_7.addWidget(self.labelAI9)
        self.lineEditAI9 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI9.setFont(font)
        self.lineEditAI9.setAutoFillBackground(False)
        self.lineEditAI9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI9.setReadOnly(True)
        self.lineEditAI9.setObjectName("lineEditAI9")
        self.verticalLayout_7.addWidget(self.lineEditAI9)
        self.labelAI10 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI10.setFont(font)
        self.labelAI10.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI10.setObjectName("labelAI10")
        self.verticalLayout_7.addWidget(self.labelAI10)
        self.lineEditAI10 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI10.setFont(font)
        self.lineEditAI10.setAutoFillBackground(False)
        self.lineEditAI10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI10.setReadOnly(True)
        self.lineEditAI10.setObjectName("lineEditAI10")
        self.verticalLayout_7.addWidget(self.lineEditAI10)
        self.labelAI11 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI11.setFont(font)
        self.labelAI11.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI11.setObjectName("labelAI11")
        self.verticalLayout_7.addWidget(self.labelAI11)
        self.lineEditAI11 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI11.setFont(font)
        self.lineEditAI11.setAutoFillBackground(False)
        self.lineEditAI11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI11.setReadOnly(True)
        self.lineEditAI11.setObjectName("lineEditAI11")
        self.verticalLayout_7.addWidget(self.lineEditAI11)
        self.labelAI12 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI12.setFont(font)
        self.labelAI12.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI12.setObjectName("labelAI12")
        self.verticalLayout_7.addWidget(self.labelAI12)
        self.lineEditAI12 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI12.setFont(font)
        self.lineEditAI12.setAutoFillBackground(False)
        self.lineEditAI12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI12.setReadOnly(True)
        self.lineEditAI12.setObjectName("lineEditAI12")
        self.verticalLayout_7.addWidget(self.lineEditAI12)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelAI13 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI13.setFont(font)
        self.labelAI13.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI13.setObjectName("labelAI13")
        self.verticalLayout_6.addWidget(self.labelAI13)
        self.lineEditAI13 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI13.setFont(font)
        self.lineEditAI13.setAutoFillBackground(False)
        self.lineEditAI13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI13.setReadOnly(True)
        self.lineEditAI13.setObjectName("lineEditAI13")
        self.verticalLayout_6.addWidget(self.lineEditAI13)
        self.labelAI14 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI14.setFont(font)
        self.labelAI14.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI14.setObjectName("labelAI14")
        self.verticalLayout_6.addWidget(self.labelAI14)
        self.lineEditAI14 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI14.setFont(font)
        self.lineEditAI14.setAutoFillBackground(False)
        self.lineEditAI14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI14.setReadOnly(True)
        self.lineEditAI14.setObjectName("lineEditAI14")
        self.verticalLayout_6.addWidget(self.lineEditAI14)
        self.labelAI15 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI15.setFont(font)
        self.labelAI15.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI15.setObjectName("labelAI15")
        self.verticalLayout_6.addWidget(self.labelAI15)
        self.lineEditAI15 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI15.setFont(font)
        self.lineEditAI15.setAutoFillBackground(False)
        self.lineEditAI15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI15.setReadOnly(True)
        self.lineEditAI15.setObjectName("lineEditAI15")
        self.verticalLayout_6.addWidget(self.lineEditAI15)
        self.labelAI16 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI16.setFont(font)
        self.labelAI16.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI16.setObjectName("labelAI16")
        self.verticalLayout_6.addWidget(self.labelAI16)
        self.lineEditAI16 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI16.setFont(font)
        self.lineEditAI16.setAutoFillBackground(False)
        self.lineEditAI16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI16.setReadOnly(True)
        self.lineEditAI16.setObjectName("lineEditAI16")
        self.verticalLayout_6.addWidget(self.lineEditAI16)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelAI17 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI17.setFont(font)
        self.labelAI17.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI17.setObjectName("labelAI17")
        self.verticalLayout.addWidget(self.labelAI17)
        self.lineEditAI17 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI17.setFont(font)
        self.lineEditAI17.setAutoFillBackground(False)
        self.lineEditAI17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI17.setReadOnly(True)
        self.lineEditAI17.setObjectName("lineEditAI17")
        self.verticalLayout.addWidget(self.lineEditAI17)
        self.labelAI18 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI18.setFont(font)
        self.labelAI18.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI18.setObjectName("labelAI18")
        self.verticalLayout.addWidget(self.labelAI18)
        self.lineEditAI18 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI18.setFont(font)
        self.lineEditAI18.setAutoFillBackground(False)
        self.lineEditAI18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI18.setReadOnly(True)
        self.lineEditAI18.setObjectName("lineEditAI18")
        self.verticalLayout.addWidget(self.lineEditAI18)
        self.labelAI19 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI19.setFont(font)
        self.labelAI19.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI19.setObjectName("labelAI19")
        self.verticalLayout.addWidget(self.labelAI19)
        self.lineEditAI19 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI19.setFont(font)
        self.lineEditAI19.setAutoFillBackground(False)
        self.lineEditAI19.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI19.setReadOnly(True)
        self.lineEditAI19.setObjectName("lineEditAI19")
        self.verticalLayout.addWidget(self.lineEditAI19)
        self.labelAI20 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI20.setFont(font)
        self.labelAI20.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI20.setObjectName("labelAI20")
        self.verticalLayout.addWidget(self.labelAI20)
        self.lineEditAI20 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI20.setFont(font)
        self.lineEditAI20.setAutoFillBackground(False)
        self.lineEditAI20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI20.setReadOnly(True)
        self.lineEditAI20.setObjectName("lineEditAI20")
        self.verticalLayout.addWidget(self.lineEditAI20)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelAI21 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI21.setFont(font)
        self.labelAI21.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI21.setObjectName("labelAI21")
        self.verticalLayout_3.addWidget(self.labelAI21)
        self.lineEditAI21 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI21.setFont(font)
        self.lineEditAI21.setAutoFillBackground(False)
        self.lineEditAI21.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI21.setReadOnly(True)
        self.lineEditAI21.setObjectName("lineEditAI21")
        self.verticalLayout_3.addWidget(self.lineEditAI21)
        self.labelAI22 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI22.setFont(font)
        self.labelAI22.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI22.setObjectName("labelAI22")
        self.verticalLayout_3.addWidget(self.labelAI22)
        self.lineEditAI22 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI22.setFont(font)
        self.lineEditAI22.setAutoFillBackground(False)
        self.lineEditAI22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI22.setReadOnly(True)
        self.lineEditAI22.setObjectName("lineEditAI22")
        self.verticalLayout_3.addWidget(self.lineEditAI22)
        self.labelAI23 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI23.setFont(font)
        self.labelAI23.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI23.setObjectName("labelAI23")
        self.verticalLayout_3.addWidget(self.labelAI23)
        self.lineEditAI23 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI23.setFont(font)
        self.lineEditAI23.setAutoFillBackground(False)
        self.lineEditAI23.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI23.setReadOnly(True)
        self.lineEditAI23.setObjectName("lineEditAI23")
        self.verticalLayout_3.addWidget(self.lineEditAI23)
        self.labelAI24 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI24.setFont(font)
        self.labelAI24.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI24.setObjectName("labelAI24")
        self.verticalLayout_3.addWidget(self.labelAI24)
        self.lineEditAI24 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI24.setFont(font)
        self.lineEditAI24.setAutoFillBackground(False)
        self.lineEditAI24.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI24.setReadOnly(True)
        self.lineEditAI24.setObjectName("lineEditAI24")
        self.verticalLayout_3.addWidget(self.lineEditAI24)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelAI25 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI25.setFont(font)
        self.labelAI25.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI25.setObjectName("labelAI25")
        self.verticalLayout_4.addWidget(self.labelAI25)
        self.lineEditAI25 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI25.setFont(font)
        self.lineEditAI25.setAutoFillBackground(False)
        self.lineEditAI25.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI25.setReadOnly(True)
        self.lineEditAI25.setObjectName("lineEditAI25")
        self.verticalLayout_4.addWidget(self.lineEditAI25)
        self.labelAI26 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI26.setFont(font)
        self.labelAI26.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI26.setObjectName("labelAI26")
        self.verticalLayout_4.addWidget(self.labelAI26)
        self.lineEditAI26 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI26.setFont(font)
        self.lineEditAI26.setAutoFillBackground(False)
        self.lineEditAI26.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI26.setReadOnly(True)
        self.lineEditAI26.setObjectName("lineEditAI26")
        self.verticalLayout_4.addWidget(self.lineEditAI26)
        self.labelAI27 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI27.setFont(font)
        self.labelAI27.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI27.setObjectName("labelAI27")
        self.verticalLayout_4.addWidget(self.labelAI27)
        self.lineEditAI27 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI27.setFont(font)
        self.lineEditAI27.setAutoFillBackground(False)
        self.lineEditAI27.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI27.setReadOnly(True)
        self.lineEditAI27.setObjectName("lineEditAI27")
        self.verticalLayout_4.addWidget(self.lineEditAI27)
        self.labelAI28 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI28.setFont(font)
        self.labelAI28.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI28.setObjectName("labelAI28")
        self.verticalLayout_4.addWidget(self.labelAI28)
        self.lineEditAI28 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI28.setFont(font)
        self.lineEditAI28.setAutoFillBackground(False)
        self.lineEditAI28.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI28.setReadOnly(True)
        self.lineEditAI28.setObjectName("lineEditAI28")
        self.verticalLayout_4.addWidget(self.lineEditAI28)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelAI29 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI29.setFont(font)
        self.labelAI29.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI29.setObjectName("labelAI29")
        self.verticalLayout_5.addWidget(self.labelAI29)
        self.lineEditAI29 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI29.setFont(font)
        self.lineEditAI29.setAutoFillBackground(False)
        self.lineEditAI29.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI29.setReadOnly(True)
        self.lineEditAI29.setObjectName("lineEditAI29")
        self.verticalLayout_5.addWidget(self.lineEditAI29)
        self.labelAI30 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI30.setFont(font)
        self.labelAI30.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI30.setObjectName("labelAI30")
        self.verticalLayout_5.addWidget(self.labelAI30)
        self.lineEditAI30 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI30.setFont(font)
        self.lineEditAI30.setAutoFillBackground(False)
        self.lineEditAI30.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI30.setReadOnly(True)
        self.lineEditAI30.setObjectName("lineEditAI30")
        self.verticalLayout_5.addWidget(self.lineEditAI30)
        self.labelAI31 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI31.setFont(font)
        self.labelAI31.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI31.setObjectName("labelAI31")
        self.verticalLayout_5.addWidget(self.labelAI31)
        self.lineEditAI31 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI31.setFont(font)
        self.lineEditAI31.setAutoFillBackground(False)
        self.lineEditAI31.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI31.setReadOnly(True)
        self.lineEditAI31.setObjectName("lineEditAI31")
        self.verticalLayout_5.addWidget(self.lineEditAI31)
        self.labelAI32 = QtWidgets.QLabel(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAI32.setFont(font)
        self.labelAI32.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAI32.setObjectName("labelAI32")
        self.verticalLayout_5.addWidget(self.labelAI32)
        self.lineEditAI32 = QtWidgets.QLineEdit(EPSInterface)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEditAI32.setFont(font)
        self.lineEditAI32.setAutoFillBackground(False)
        self.lineEditAI32.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAI32.setReadOnly(True)
        self.lineEditAI32.setObjectName("lineEditAI32")
        self.verticalLayout_5.addWidget(self.lineEditAI32)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)

        self.retranslateUi(EPSInterface)
        QtCore.QMetaObject.connectSlotsByName(EPSInterface)

    def retranslateUi(self, EPSInterface):
        _translate = QtCore.QCoreApplication.translate
        EPSInterface.setWindowTitle(_translate("EPSInterface", "EPS Interface"))
        self.LinkButtonBackEPS.setText(_translate("EPSInterface", "Back"))
        self.labelAI1.setText(_translate("EPSInterface", "Analog Input 1"))
        self.labelAI2.setText(_translate("EPSInterface", "Analog Input 2"))
        self.labelAI3.setText(_translate("EPSInterface", "Analog Input 3"))
        self.labelAI4.setText(_translate("EPSInterface", "Analog Input 4"))
        self.labelAI5.setText(_translate("EPSInterface", "Analog Input 1"))
        self.labelAI6.setText(_translate("EPSInterface", "Analog Input 2"))
        self.labelAI7.setText(_translate("EPSInterface", "Analog Input 3"))
        self.labelAI8.setText(_translate("EPSInterface", "Analog Input 4"))
        self.labelAI9.setText(_translate("EPSInterface", "Analog Input 1"))
        self.labelAI10.setText(_translate("EPSInterface", "Analog Input 2"))
        self.labelAI11.setText(_translate("EPSInterface", "Analog Input 3"))
        self.labelAI12.setText(_translate("EPSInterface", "Analog Input 4"))
        self.labelAI13.setText(_translate("EPSInterface", "Analog Input 1"))
        self.labelAI14.setText(_translate("EPSInterface", "Analog Input 2"))
        self.labelAI15.setText(_translate("EPSInterface", "Analog Input 3"))
        self.labelAI16.setText(_translate("EPSInterface", "Analog Input 4"))
        self.labelAI17.setText(_translate("EPSInterface", "Analog Input 1"))
        self.labelAI18.setText(_translate("EPSInterface", "Analog Input 2"))
        self.labelAI19.setText(_translate("EPSInterface", "Analog Input 3"))
        self.labelAI20.setText(_translate("EPSInterface", "Analog Input 4"))
        self.labelAI21.setText(_translate("EPSInterface", "Analog Input 1"))
        self.labelAI22.setText(_translate("EPSInterface", "Analog Input 2"))
        self.labelAI23.setText(_translate("EPSInterface", "Analog Input 3"))
        self.labelAI24.setText(_translate("EPSInterface", "Analog Input 4"))
        self.labelAI25.setText(_translate("EPSInterface", "Analog Input 1"))
        self.labelAI26.setText(_translate("EPSInterface", "Analog Input 2"))
        self.labelAI27.setText(_translate("EPSInterface", "Analog Input 3"))
        self.labelAI28.setText(_translate("EPSInterface", "Analog Input 4"))
        self.labelAI29.setText(_translate("EPSInterface", "Analog Input 1"))
        self.labelAI30.setText(_translate("EPSInterface", "Analog Input 2"))
        self.labelAI31.setText(_translate("EPSInterface", "Analog Input 3"))
        self.labelAI32.setText(_translate("EPSInterface", "Analog Input 4"))

import resources_rc