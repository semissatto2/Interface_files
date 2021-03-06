#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QStatusBar
from PyQt5 import uic, QtCore, QtGui, QtWidgets
import sys
import myEpics
import myAlarm
import time
import datetime
from epics import PV, caget
#from pydm import PyDMApplication

# Load UI Files
Ui_Form_telaInicial, QtBaseClass = uic.loadUiType("telaInicial.ui")
Ui_Form_epicsInterface, QtBaseClass = uic.loadUiType("epicsInterface.ui")
Ui_Form_EPSInterface, QtBaseClass = uic.loadUiType("EPSInterface.ui")
Ui_Form_TempScreen, QtBaseClass = uic.loadUiType("TempScreen.ui")
Ui_Form_archiverInterface, QtBaseClass = uic.loadUiType("archiverInterface.ui")
Ui_Form_EPSFrontEndInterface, QtBaseClass = uic.loadUiType("EPSFrontEnd.ui")


# Window #1 Class
class TelaInicial(QMainWindow, Ui_Form_telaInicial):
    def __init__(self, parent=None):
        super(TelaInicial, self).__init__(parent)
        super(Ui_Form_telaInicial, self).__init__()
        self.setupUi(self)

        # Add things to my TelaInicial
        self.setGeometry(60,0,500,500)

        # Bind signal to slot
        self.LinkButtonEPICS.clicked.connect(self.openEPICS)
        self.LinkButtonEPS.clicked.connect(self.openEPS)
        #self.LinkButtonTempScreen.clicked.connect(self.openTempScreen)
        #self.LinkButtonPyDM.clicked.connect(self.openPyDM)
        self.LinkButtonArchiver.clicked.connect(self.openArchiver)


    # My slots
    def openEPICS(self):
        self.epicsInterface = EpicsInterface()
        self.epicsInterface.show()
        self.close()

    def openEPS(self):
        self.EPSFrontEndInterface = EPSFrontEndInterface()
        self.EPSFrontEndInterface.showMaximized()
        self.close()        
    
    '''def openTempScreen(self):
        self.TempScreen = TempScreen()
        self.TempScreen.show()
        self.close()'''   

    def openArchiver(self):
        self.archiverInterface = archiverInterface()
        self.archiverInterface.show()
        self.close()

    '''def openPyDM(self):
        app_pydm = PyDMApplication(sys.argv)
        app_pydm.new_window("lineEditTestPyDM.ui")'''
        
        # Window Epics Interface #2 Class
class EpicsInterface(QWidget, Ui_Form_epicsInterface):
    def __init__(self, parent=None):
        super(EpicsInterface, self).__init__(parent)
        super(Ui_Form_epicsInterface, self).__init__()
        self.setupUi(self)

        # Bind signal to slot
        self.LinkButtonBack.clicked.connect(self.onClickBack)
        self.pushButton_readPv.clicked.connect(self.readPv)
        
    # My slots
    def onClickBack(self):
        self.close()
        self.window = TelaInicial()
        self.window.show()
        
    def readPv(self):
         nome_da_pv = self.lineEdit_readPv.text()
         if nome_da_pv != '':
             pv = PV(nome_da_pv)
             if pv.connected:
                      pv_value = str(float(pv.value))
                      self.lineEdit_PvValue.setText(pv_value)
             else:
                      self.lineEdit_PvValue.setText('PV not connected')  

        
# Window EPSFrontEndInterface #3 Class
class EPSFrontEndInterface(QWidget, Ui_Form_EPSFrontEndInterface):
    def __init__(self, parent=None):
        super(EPSFrontEndInterface, self).__init__(parent)
        super(Ui_Form_EPSFrontEndInterface, self).__init__()
        self.setupUi(self)

        # Add things to my Window
        self.threadclass = ThreadClass()
        self.threadclass.start()
        self.threadclass_alarms = ThreadAlarmPoll()
        self.threadclass_alarms.start()
        self.threadconn = ThreadConn()
        self.threadconn.start()
        self.setGeometry(54,-8,1538,878)
        self.k = 0  # Control Variable for Alarm filtering
        self.filter = 0 # Control Variable for Alarm filtering
        self.tempo_inferior = 0
        self.tempo_superior = 0
        
       # Set things to my Window
        
       # Bind signal to method
        self.pushButtonBack.clicked.connect(self.onClickBack)
        self.box.stateChanged.connect(self.checkChecked)
        self.pushButtonNow.clicked.connect(self.setNow)
        self.pushButtonOpenArchiver.clicked.connect(self.openArchiver)
        self.threadclass.sig.connect(self.updateScreen)
        self.threadclass_alarms.sig_alarms.connect(self.updateAlarmScreen)
        self.threadconn.sig_conn.connect(self.updateConnStatus)
     
    def onClickBack(self):
        self.close()
        self.window = TelaInicial()
        self.window.show()

    def checkChecked(self):
        if self.k%2 == 0:
            self.filter = 2
            try:
                ano_inferior = int(self.lineEditAnoInf.text())
                mes_inferior = int(self.lineEditMesInf.text())
                dia_inferior = int(self.lineEditDiaInf.text())
                hora_inferior = int(self.lineEditHoraInf.text())
                minuto_inferior = int(self.lineEditMinutoInf.text())
                segundo_inferior = int(self.lineEditSegundoInf.text())
                ano_superior = int(self.lineEditAnoSup.text())
                mes_superior = int(self.lineEditMesSup.text())
                dia_superior = int(self.lineEditDiaSup.text())
                hora_superior = int(self.lineEditHoraSup.text())
                minuto_superior = int(self.lineEditMinutoSup.text())
                segundo_superior = int(self.lineEditSegundoSup.text())
            except ValueError:
                self.lineEditAlarmstatus_2.setText("That's not a valid date. Try again!")
                return None
            
            if self.lineEditAnoInf.text() != '':
                self.lineEditAlarmstatus_2.setText("That's a valid date.")
                ano_inferior = int(self.lineEditAnoInf.text())
            else:
                ano_inferior = 2000
                
            if self.lineEditMesInf.text() != '':            
                mes_inferior = int(self.lineEditMesInf.text())
            else:
                mes_inferior = 0
            
            if self.lineEditDiaInf.text() != '':
                dia_inferior = int(self.lineEditDiaInf.text())
            else:
                dia_inferior = 0
            
            if self.lineEditHoraInf.text() != '':
                hora_inferior = int(self.lineEditHoraInf.text())
            else:
                hora_inferior = 0
            
            if self.lineEditMinutoInf.text() != '':
                minuto_inferior = int(self.lineEditMinutoInf.text())
            else:
                minuto_inferior = 0
            
            if self.lineEditSegundoInf.text() != '':
                segundo_inferior = int(self.lineEditSegundoInf.text())
            else:
                segundo_inferior = 0
            
            if self.lineEditAnoSup.text() != '':
                ano_superior = int(self.lineEditAnoSup.text())
            else:
                ano_superior = 2000
            
            if self.lineEditMesSup.text() != '':
                mes_superior = int(self.lineEditMesSup.text())
            else:
                mes_superior = 0
            
            if self.lineEditDiaSup.text() != '':
                dia_superior = int(self.lineEditDiaSup.text())
            else:
                dia_superior = 0
            
            if self.lineEditHoraSup.text() != '':
                hora_superior = int(self.lineEditHoraSup.text())
            else:
                hora_superior = 0
            
            if self.lineEditMinutoSup.text() != '':
                minuto_superior = int(self.lineEditMinutoSup.text())
            else:
                minuto_superior = 0
            
            if self.lineEditSegundoSup.text() != '':
                segundo_superior = int(self.lineEditSegundoSup.text())
            else:
                segundo_superior = 0
                
            self.tempo_inferior = (ano_inferior-2000)*365*24 + dia_inferior*24 + mes_inferior*30*24 + hora_inferior + minuto_inferior/60 + segundo_inferior/3600 # Tempo fisico do limite inferior total em horas
            self.tempo_superior = (ano_superior-2000)*365*24 + dia_superior*24 + mes_superior*30*24 + hora_superior + minuto_superior/60 + segundo_superior/3600 # Tempo fisico do limite inferior total em horas
        else:
            self.filter = 1
        self.k += 1
    
    def setNow(self):
        Y =datetime.datetime.now().strftime("%Y")
        self.lineEditAnoSup.setText(Y)
        month = datetime.datetime.now().strftime("%m")
        self.lineEditMesSup.setText(month)
        d =datetime.datetime.now().strftime("%d")
        self.lineEditDiaSup.setText(d)
        H =datetime.datetime.now().strftime("%H")
        self.lineEditHoraSup.setText(H)
        minute =datetime.datetime.now().strftime("%M")
        self.lineEditMinutoSup.setText(minute)
        S =datetime.datetime.now().strftime("%S")
        self.lineEditSegundoSup.setText(S)        
        
    def openArchiver(self):
        self.archiverInterface = archiverInterface()
        self.archiverInterface.show()
        #self.close()
        
    def updateConnStatus(self, connStatus, alarmStatus):
        connStatus_ =  myEpics.pv[myEpics.getIndexPV('IVUFE:EPS:status')].connected
        print ("connStatus_: ", connStatus_)
        if connStatus_ ==  True:
            self.labelConnection_2.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelConnection_2.setPixmap(QtGui.QPixmap("images/led_red.png"))
            
        if myAlarm.flag_alarmes_criados == 1:
            self.lineEditAlarmstatus.setText("Alarms has been\ncreated successfully.")
        else:
            self.lineEditAlarmstatus.setText("Creating alarms ...")
        
    def updateAlarmScreen(
        self,
        counter,
        item_name,
        data,
        hora,
        classe,
        texto,
        tempo_total_list
        ):
        
        if self.filter == 2:
            aux = 0
            aux_2 = 0
            numero_elementos_filtrados = 0
            for k in range(len(tempo_total_list)):
                if tempo_total_list[k] < self.tempo_superior and tempo_total_list[k] > self.tempo_inferior :
                    numero_elementos_filtrados += 1
            self.tableWidget.setRowCount(numero_elementos_filtrados)                    
            for i in reversed(range(counter)):
                if tempo_total_list[i] < self.tempo_superior and tempo_total_list[i] > self.tempo_inferior : #troquei aux_2 por i
                    for j in range(6):
                        item = QtWidgets.QTableWidgetItem()
                        if j == 0:
                            item.setText(str(item_name[i])) #i
                        if j == 1:
                            item.setText(str(hora[i]))#i
                        if j == 2:
                            item.setText(str(texto[i]))#i
                        if j == 3:
                            item.setText(str(classe[i]))#i
                            if classe[i] == 'Defeito': #i
                                brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                                brush.setStyle(QtCore.Qt.SolidPattern)
                                item.setBackground(brush)
                                item.setTextAlignment(QtCore.Qt.AlignCenter)
                                font = QtGui.QFont()
                                font.setFamily("Utopia")
                                font.setPointSize(10)
                                font.setBold(True)
                                font.setWeight(75)
                                item.setFont(font)
                                
                            if classe[i] == 'Falha': #i
                                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                                brush.setStyle(QtCore.Qt.SolidPattern)
                                item.setBackground(brush)
                                item.setTextAlignment(QtCore.Qt.AlignCenter)
                                font = QtGui.QFont()
                                font.setFamily("Utopia")
                                font.setPointSize(10)
                                font.setBold(True)
                                font.setWeight(75)
                                item.setFont(font)
                                
                            if classe[i][len(classe[i])-7:] == ' solved':#i
                                brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
                                brush.setStyle(QtCore.Qt.SolidPattern)
                                item.setBackground(brush)
                                item.setTextAlignment(QtCore.Qt.AlignCenter)
                                font = QtGui.QFont()
                                font.setFamily("Utopia")
                                font.setPointSize(10)
                                font.setBold(True)
                                font.setWeight(75)
                                item.setFont(font)
                                
                        if j == 4:
                            item.setText(str(data[i])) #i
                        if j == 5:
                            item.setText(str(aux))
                            aux += 1

                        self.tableWidget.setItem(aux, j, item)
                aux_2 += 1
                
        elif self.filter ==  1 or self.filter == 0: #Show all alarms if _Check box_ is unchecked
            aux_else = 0
            self.tableWidget.setRowCount(counter)
            for i in reversed(range(counter)):
                if True :
                    for j in range(6):
                        item = QtWidgets.QTableWidgetItem()
                        if j == 0:
                            item.setText(str(item_name[i]))
                        if j == 1:
                            item.setText(str(hora[i]))
                        if j == 2:
                            item.setText(str(texto[i]))
                        if j == 3:
                            item.setText(str(classe[i]))
                            if classe[i] == 'Defeito':
                                brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                                brush.setStyle(QtCore.Qt.SolidPattern)
                                item.setBackground(brush)
                                item.setTextAlignment(QtCore.Qt.AlignCenter)
                                font = QtGui.QFont()
                                font.setFamily("Utopia")
                                font.setPointSize(10)
                                font.setBold(True)
                                font.setWeight(75)
                                item.setFont(font)
                                
                            if classe[i] == 'Falha':
                                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                                brush.setStyle(QtCore.Qt.SolidPattern)
                                item.setBackground(brush)
                                item.setTextAlignment(QtCore.Qt.AlignCenter)
                                font = QtGui.QFont()
                                font.setFamily("Utopia")
                                font.setPointSize(10)
                                font.setBold(True)
                                font.setWeight(75)
                                item.setFont(font)
                                
                            if classe[i][len(classe[i])-7:] == ' solved':
                                brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
                                brush.setStyle(QtCore.Qt.SolidPattern)
                                item.setBackground(brush)
                                item.setTextAlignment(QtCore.Qt.AlignCenter)
                                font = QtGui.QFont()
                                font.setFamily("Utopia")
                                font.setPointSize(10)
                                font.setBold(True)
                                font.setWeight(75)
                                item.setFont(font)                        
                                
                                
                        if j == 4:
                            item.setText(str(data[i]))
                        if j == 5:
                            item.setText(str(aux_else))
                            aux_else += 1
                                               
                        self.tableWidget.setItem(aux_else, j, item)
                        
    def updateScreen(self, EPSList):
        #EPICS Connection Status Bool
        if myEpics.pv[myEpics.getIndexPV('IVUFE:EPS:status')].value == 1: 
            self.labelConnection.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelConnection.setPixmap(QtGui.QPixmap("images/led_red.png"))
            
        # Update Real time
        self.lineEditTemporeal.setText(str(datetime.datetime.now()))
        
        # Update TT[i], FIT
        self.lineEditXbpm1.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-XBPM1-TT1')].value)+" ºC")
        self.lineEditXbpm1_2.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-XBPM1-TT2')].value)+" ºC")
        self.lineEditXbpm1_3.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-XBPM1-TT3')].value)+" ºC")
        self.lineEditXbpm1_4.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-XBPM1-TT4')].value)+" ºC")
        self.lineEditXbpm1_5.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AS_DEV-XBPM1-FIT')].value)+" L/Min")
        self.lineEditXbpm1_6.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-XBPM1-TT')].value)+" ºC")
        self.lineEditXbpm2.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-XBPM2-TT1')].value)+" ºC")
        self.lineEditXbpm2_2.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-XBPM2-TT2')].value)+" ºC")
        self.lineEditXbpm2_3.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-XBPM2-TT3')].value)+" ºC")
        self.lineEditXbpm2_4.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-XBPM2-TT4')].value)+" ºC")        
        self.lineEditXbpm2_5.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AS_DEV-XBPM2-FIT')].value)+" L/Min")
        self.lineEditXbpm2_6.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-XBPM2-TT')].value)+" ºC")
        self.lineEditMsk.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-MSK-TT1')].value)+" ºC")
        self.lineEditMsk_2.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-MSK-TT2')].value)+" ºC")
        self.lineEditMsk_3.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-MSK-TT3')].value)+" ºC")
        self.lineEditMsk_4.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-MSK-TT4')].value)+" ºC")
        self.lineEditMsk_5.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AS_DEV-MSK-FIT')].value)+" L/Min")
        self.lineEditMsk_6.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-MSK-TT')].value)+" ºC")
        self.lineEditSlits.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-SLITS-TT1')].value)+" ºC")
        self.lineEditSlits_2.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-SLITS-TT2')].value)+" ºC")
        self.lineEditSlits_3.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-SLITS-TT3')].value)+" ºC")
        self.lineEditSlits_4.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-SLITS-TT4')].value)+" ºC")
        self.lineEditSlits_5.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AS_DEV-SLITS-FIT')].value)+" L/Min")
        self.lineEditSlits_6.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-SLITS-TT')].value)+" ºC")
        self.lineEditPhoton.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_DEV-PS-TT1')].value)+" ºC")

        # Update Utilities
        self.lineEditWprtt.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_UTL-WPR-TT')].value)+" ºC")
        self.lineEditWprfit.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AS_UTL-WPR-FIT')].value)+" L/Min")
        self.lineEditWprpit.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AS_UTL-WPR-PIT')].value)+" Bar")
        self.lineEditWrttt.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AI_UTL-WRT-TT')].value)+" ºC")
        self.lineEditWrtpit.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AS_UTL-WRT-PIT')].value)+" Bar")
        self.lineEditWrtfit.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AS_UTL-WRT-FIT')].value)+" L/Min")
        self.lineEditCarpit.setText(str.format("{0:.3f}",EPSList[myEpics.getIndexPV('IVUFE:EPS:AS_UTL-CAR-PIT')].value)+" Bar")        

        # Update VG's bools
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_VAC-VG1')].value == 1:
            self.labelVG1.setPixmap(QtGui.QPixmap("images/retangulo_verde_v2.png"))
        else:
            self.labelVG1.setPixmap(QtGui.QPixmap("images/retangulo_vermelho_v2.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_VAC-VG2')].value == 1:
            self.labelVG1_2.setPixmap(QtGui.QPixmap("images/retangulo_verde_v2.png"))
        else:
            self.labelVG1_2.setPixmap(QtGui.QPixmap("images/retangulo_vermelho_v2.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_VAC-VG3')].value == 1:
            self.labelVG1_4.setPixmap(QtGui.QPixmap("images/retangulo_verde_v2.png"))
        else:
            self.labelVG1_4.setPixmap(QtGui.QPixmap("images/retangulo_vermelho_v2.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_VAC-VG4')].value == 1:
            self.labelVG1_5.setPixmap(QtGui.QPixmap("images/retangulo_verde_v2.png"))
        else:
            self.labelVG1_5.setPixmap(QtGui.QPixmap("images/retangulo_vermelho_v2.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_VAC-VG5')].value == 1:
            self.labelVG1_6.setPixmap(QtGui.QPixmap("images/retangulo_verde_v2.png"))
        else:
            self.labelVG1_6.setPixmap(QtGui.QPixmap("images/retangulo_vermelho_v2.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_VAC-VG6')].value == 1:
            self.labelVG1_7.setPixmap(QtGui.QPixmap("images/retangulo_verde_v2.png"))
        else:
            self.labelVG1_7.setPixmap(QtGui.QPixmap("images/retangulo_vermelho_v2.png"))
       # This section is commented because the automation system declared a VG variable without necessity     
        '''if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_VAC-VG7')].value == 1:
            self.labelVG1_8.setPixmap(QtGui.QPixmap("images/retangulo_verde_v2.png"))
        else:
            self.labelVG1_8.setPixmap(QtGui.QPixmap("images/retangulo_vermelho_v2.png"))'''
        
        # Update PS's bools (w/ reset logic) TROCAR retangulo por circulo
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_VAC-PS1')].value == 1:
            self.labelPS1.setPixmap(QtGui.QPixmap("images/circulo_verde_v2.png"))
        else:
            self.labelPS1.setPixmap(QtGui.QPixmap("images/circulo_vermelho_v2.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_VAC-PS2')].value == 1:
            self.labelPS1_2.setPixmap(QtGui.QPixmap("images/circulo_verde_v2.png.png"))
        else:
            self.labelPS1_2.setPixmap(QtGui.QPixmap("images/circulo_vermelho_v2.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_VAC-PS3')].value == 1:
            self.labelPS1_4.setPixmap(QtGui.QPixmap("images/circulo_verde_v2.png.png"))
        else:
            self.labelPS1_4.setPixmap(QtGui.QPixmap("images/circulo_vermelho_v2.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_VAC-PS4')].value == 1:
            self.labelPS1_5.setPixmap(QtGui.QPixmap("images/circulo_verde_v2.png.png"))
        else:
            self.labelPS1_5.setPixmap(QtGui.QPixmap("images/circulo_vermelho_v2.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_VAC-PS5')].value == 1:
            self.labelPS1_6.setPixmap(QtGui.QPixmap("images/circulo_verde_v2.png.png"))
        else:
            self.labelPS1_6.setPixmap(QtGui.QPixmap("images/circulo_vermelho_v2.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_VAC-PS6')].value == 1:
            self.labelPS1_7.setPixmap(QtGui.QPixmap("images/circulo_verde_v2.png.png"))
        else:
            self.labelPS1_7.setPixmap(QtGui.QPixmap("images/circulo_vermelho_v2.png"))

            # Update Shutter Status (0 - OPEN  / 1 - CLOSE)
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:GAMMA_STATUS_PPS')].value == 0:
            self.labelGammaShutter.setPixmap(QtGui.QPixmap("images/gamma_shutter_open.png"))
        else:
            self.labelGammaShutter.setPixmap(QtGui.QPixmap("images/gamma_shutter_closed.png"))

        # Update TT[i], FIT bool
        #Xbpm1 BOOLS
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-XBPM1-TT1')].value == 1:
            self.labelXbpm1Bool1.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelXbpm1Bool1.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-XBPM1-TT2')].value == 1:
            self.labelXbpm1Bool2.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelXbpm1Bool2.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-XBPM1-TT3')].value == 1:
            self.labelXbpm1Bool3.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelXbpm1Bool3.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-XBPM1-TT4')].value == 1:
            self.labelXbpm1Bool4.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelXbpm1Bool4.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-XBPM1-FIT')].value == 1:
            self.labelXbpm1Bool5.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelXbpm1Bool5.setPixmap(QtGui.QPixmap("images/led_yellow.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-XBPM1-TT')].value == 1:
            self.labelXbpm1Bool6.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelXbpm1Bool6.setPixmap(QtGui.QPixmap("images/led_yellow.png"))

        #Xbpm2 BOOLS
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-XBPM2-TT1')].value == 1:
            self.labelXbpm2Bool.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelXbpm2Bool.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-XBPM2-TT2')].value == 1:
            self.labelXbpm2Bool_2.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelXbpm2Bool_2.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-XBPM2-TT3')].value == 1:
            self.labelXbpm2Bool_3.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelXbpm2Bool_3.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-XBPM2-TT4')].value == 1:
            self.labelXbpm2Bool_4.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelXbpm2Bool_4.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-XBPM2-FIT')].value == 1:
            self.labelXbpm2Bool_5.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelXbpm2Bool_5.setPixmap(QtGui.QPixmap("images/led_yellow.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-XBPM2-TT')].value == 1:
            self.labelXbpm2Bool_6.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelXbpm2Bool_6.setPixmap(QtGui.QPixmap("images/led_yellow.png"))

        # Msk BOOLS
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-MSK-TT1')].value == 1:
            self.labelMskBool.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelMskBool.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-MSK-TT2')].value == 1:
            self.labelMskBool_2.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelMskBool_2.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-MSK-TT3')].value == 1:
            self.labelMskBool_3.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelMskBool_3.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-MSK-TT4')].value == 1:
            self.labelMskBool_4.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelMskBool_4.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-MSK-FIT')].value == 1:
            self.labelMskBool_5.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelMskBool_5.setPixmap(QtGui.QPixmap("images/led_yellow.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-MSK-TT')].value == 1:
            self.labelMskBool_6.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelMskBool_6.setPixmap(QtGui.QPixmap("images/led_yellow.png"))

        #Slits BOOLS
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-SLITS-TT1')].value == 1:
            self.labelSlitsBool.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelSlitsBool.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-SLITS-TT2')].value == 1:
            self.labelSlitsBool_2.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelSlitsBool_2.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-SLITS-TT3')].value == 1:
            self.labelSlitsBool_3.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelSlitsBool_3.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-SLITS-TT4')].value == 1:
            self.labelSlitsBool_4.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelSlitsBool_4.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-SLITS-FIT')].value == 1:
            self.labelSlitsBool_5.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelSlitsBool_5.setPixmap(QtGui.QPixmap("images/led_yellow.png"))
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-SLITS-TT')].value == 1:
            self.labelSlitsBool_6.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelSlitsBool_6.setPixmap(QtGui.QPixmap("images/led_red.png"))

        # Photon BOOLS
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:ER_DEV-PS-TT1')].value == 1:
            self.labelPhotonBool.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelPhotonBool.setPixmap(QtGui.QPixmap("images/led_yellow.png"))

        # Photon Shutter
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:PHOTON_STATUS_PPS')].value == 1:
            self.labelPhotonShutter.setPixmap(QtGui.QPixmap("images/photon_shutter_closed.png"))
        else:
            self.labelPhotonShutter.setPixmap(QtGui.QPixmap("images/photon_shutter_open.png"))               

        # GV status. PS: there are 3 states: OPEN (green), CLOSE (red) & ERROR (orange)

                # Fast GVs
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:GV_ER_VAC_FV1SC')].value == 0:
            self.labelFV1.setPixmap(QtGui.QPixmap("images/valvula_ERROR_amarela.png"))
        elif EPSList[myEpics.getIndexPV( 'IVUFE:EPS:EMA-FOE-VAC-FV1O')].value == 1:
            self.labelFV1.setPixmap(QtGui.QPixmap("images/valvula_verde_v2.png"))
        else:
            self.labelFV1.setPixmap(QtGui.QPixmap("images/valvula_vermelha_v2.png"))
        
                # Slow GV
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:GV_ER_VAC-GV1')].value == 0:
            self.labelGV1.setPixmap(QtGui.QPixmap("images/valvula_ERROR_amarela.png"))
        elif EPSList[myEpics.getIndexPV('IVUFE:EPS:VAC-GV1O')].value == 1:
            self.labelGV1.setPixmap(QtGui.QPixmap("images/valvula_verde_v2.png"))
        elif EPSList[myEpics.getIndexPV('IVUFE:EPS:VAC-GV1O')].value == 0 :
            self.labelGV1.setPixmap(QtGui.QPixmap("images/valvula_vermelha_v2.png"))
            
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:GV_ER_VAC-GV2')].value == 0:
            self.labelGV2.setPixmap(QtGui.QPixmap("images/valvula_ERROR_amarela.png"))
        elif EPSList[myEpics.getIndexPV('IVUFE:EPS:VAC-GV2O')].value == 1:
            self.labelGV2.setPixmap(QtGui.QPixmap("images/valvula_verde_v2.png"))
        else:
            self.labelGV2.setPixmap(QtGui.QPixmap("images/valvula_vermelha_v2.png"))
            
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:GV_ER_VAC-GV3')].value == 0:
            self.labelGV3.setPixmap(QtGui.QPixmap("images/valvula_ERROR_amarela.png"))
        elif EPSList[myEpics.getIndexPV('IVUFE:EPS:VAC-GV3O')].value == 1:
           self.labelGV3.setPixmap(QtGui.QPixmap("images/valvula_verde_v2.png"))
        else:
            self.labelGV3.setPixmap(QtGui.QPixmap("images/valvula_vermelha_v2.png"))
            
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:GV_ER_VAC-GV4')].value == 0:
            self.labelGV4.setPixmap(QtGui.QPixmap("images/valvula_ERROR_amarela.png"))
        elif EPSList[myEpics.getIndexPV('IVUFE:EPS:VAC-GV4O')].value == 1:
            self.labelGV4.setPixmap(QtGui.QPixmap("images/valvula_verde_v2.png"))
        else:
            self.labelGV4.setPixmap(QtGui.QPixmap("images/valvula_vermelha_v2.png"))
            
        if EPSList[myEpics.getIndexPV('IVUFE:EPS:GV_ER_VAC-GV5')].value == 0:
            self.labelGV5.setPixmap(QtGui.QPixmap("images/valvula_ERROR_amarela.png"))
        elif EPSList[myEpics.getIndexPV('IVUFE:EPS:VAC-GV5O')].value == 1:
            self.labelGV5.setPixmap(QtGui.QPixmap("images/valvula_verde_v2.png"))
        else:
            self.labelGV5.setPixmap(QtGui.QPixmap("images/valvula_vermelha_v2.png"))

        if EPSList[myEpics.getIndexPV('IVUFE:EPS:GV_ER_VAC-GV6')].value == 0:
            self.labelGV6.setPixmap(QtGui.QPixmap("images/valvula_ERROR_amarela.png"))
        elif EPSList[myEpics.getIndexPV('IVUFE:EPS:VAC-GV6O')].value == 1:
            self.labelGV6.setPixmap(QtGui.QPixmap("images/valvula_verde_v2.png"))
        else:
            self.labelGV6.setPixmap(QtGui.QPixmap("images/valvula_vermelha_v2.png"))

# Window TempScreen #4 Class
class TempScreen(QWidget, Ui_Form_TempScreen):
    def __init__(self, parent=None):
        super(TempScreen, self).__init__(parent)
        super(Ui_Form_TempScreen, self).__init__()
        self.setupUi(self)

        # Add things to my Window
        self.threadtempscreen = ThreadTempScreen()
        self.threadtempscreen.start()
        
        # Set things to my Window

        # Bind signal to method
        self.threadtempscreen.sig.connect(self.updateTempScreen)
        self.pushButtonBackTempScreen.clicked.connect(self.onClickBack)

        # My slots
    def onClickBack(self):
        self.close()
        self.window = TelaInicial()
        self.window.show()
        
    def updateTempScreen(self, myList):
        self.lineEditWprFitValue.setText(str(myList[24].value))
        self.lineEditWprPitValue.setText(str(myList[25].value))
        self.lineEditWprTtValue.setText(str(myList[0].value))
        self.lineEditWprFitSetPoint.setText(str(myList[184].value))
        self.lineEditWprPitSetPoint.setText(str(myList[185].value))
        self.lineEditWprTtSetPoint.setText(str(myList[160].value))
        self.lineEditWrtFitValue.setText(str(myList[26].value))
        self.lineEditWrtPitValue.setText(str(myList[27].value))
        self.lineEditWrtTtValue.setText(str(myList[1].value))
        self.lineEditWrtFitSetPoint.setText(str(myList[186].value))
        self.lineEditWrtPitSetPoint.setText(str(myList[187].value))
        self.lineEditWrtTtSetPoint.setText(str(myList[161].value))
        
        #Update Booleans variables (0 - failure/red) (1 - normal/green)
        if myList[0].value == 1:
            self.labelWprFitBool.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelWprFitBool.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if myList[114].value == 0:
            self.labelBpBool.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelBpBool.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if myList[113].value == 0:
            self.labelEpsStatusBool.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelEpsStatusBool.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if myList[116].value == 0:
            self.labelPpsStatusBool.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelPpsStatusBool.setPixmap(QtGui.QPixmap("images/led_red.png"))
        if myList[115].value == 1:
            self.lineEditShutter.setText("OPEN")
        else:
            self.lineEditShutter.setText("CLOSED")
        if myList[124].value == 1:
            self.lineEditBeamStatus.setText("ON")
        else:
            self.lineEditBeamStatus.setText("OFF")
        
        if myList[82].value == 1:
            self.labelWprFitBool.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelWprFitBool.setPixmap(QtGui.QPixmap("images/led_red.png"))
        
        
        if myList[81].value == 1:
            self.labelWprPitBool.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelWprPitBool.setPixmap(QtGui.QPixmap("images/led_red.png"))
        
        if myList[84].value == 1:
            self.labelWprTtBool.setPixmap(QtGui.QPixmap("images/led_green.png"))
        else:
            self.labelWprTtBool.setPixmap(QtGui.QPixmap("images/led_red.png"))            

        
# Window archiver Interface #5 Class
class archiverInterface(QWidget, Ui_Form_archiverInterface):
    def __init__(self, parent=None):
        super(archiverInterface, self).__init__(parent)
        super(Ui_Form_archiverInterface, self).__init__()
        self.setupUi(self)

        # Bind signal to slot
        self.pushButtonBack.clicked.connect(self.onClickBack)
        self.pushButtonBackURL.clicked.connect(self.webView.back)
        self.pushButtonForwardURL.clicked.connect(self.webView.forward)
        
    # My slots
    def onClickBack(self):
        self.close()
        self.window = TelaInicial()
        self.window.show()
        
# Threads

class ThreadTempScreen(QtCore.QThread):
    # Create the signal
    sig = QtCore.pyqtSignal(list)
    
    def __init__(self, parent=None):
        super(ThreadTempScreen, self).__init__(parent)
        
    def run(self):
        myList = list(range(280)) # Range N = numbers of elements to catch from EPICS and send to Interface
        while 1:
            myList = myEpics.pv
            time.sleep(0.4)
            
            # Emit the signal
            self.sig.emit(myList)
        
class ThreadClass(QtCore.QThread):
    # Create the signal
    sig = QtCore.pyqtSignal(list)
    
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)
        
    def run(self):
        EPSList = list()
        while 1:
            EPSList = myEpics.pv
            time.sleep(0.2)
       
            # Emit the signal
            self.sig.emit(EPSList)

# My Thread Alarm Handler Class

class ThreadAlarmPoll(QtCore.QThread):

    # Create signals
    sig_alarms = QtCore.pyqtSignal(
        int,
        list,
        list,
        list,
        list,
        list,
        list,
        )

    def __init__(self, parent=None):
        super(ThreadAlarmPoll, self).__init__(parent)

    def run(self):
        myAlarm.createAlarms()
        while 1:
            
            #pass
            # Emit the signal if alarms was created with sucess                
            if myAlarm.flag_alarmes_criados:                
                counter = myAlarm.alarm_count
                data = myAlarm.data
                hora = myAlarm.hora
                texto = myAlarm.alarmText
                classe = myAlarm.alarmClass
                item_name = myAlarm.pv_names
                tempo_total_list = myAlarm.tempo_total_list
                self.sig_alarms.emit(counter,item_name,data, hora,classe,texto, tempo_total_list)
            time.sleep(1)            

# My Thread Polling IOC Status connection
class ThreadConn(QtCore.QThread):
    # Create the signal
    sig_conn = QtCore.pyqtSignal(bool, int)
    
    def __init__(self, parent=None):
        super(ThreadConn, self).__init__(parent)
    def run(self):
        connStatus_ant = True
        
        while 1:
            #IOC Status handler
            if connStatus_ant == False and myEpics.pv[myEpics.getIndexPV('IVUFE:EPS:status')].connected == True:
                myAlarm.recebeInt(True)
                time.sleep(5) #Tempo empirico para se reconhecer que a IOC foi recem iniciada
            elif connStatus_ant == True and myEpics.pv[myEpics.getIndexPV('IVUFE:EPS:status')].connected == False:
                myAlarm.recebeInt(True)
                time.sleep(5) #Tempo empirico para se reconhecer que a IOC foi recem iniciada
            else:
                myAlarm.recebeInt(False)               
                connStatus = myEpics.pv[myEpics.getIndexPV('IVUFE:EPS:status')].connected
                connStatus_ant = connStatus
                time.sleep(0.1)

            #Alarm Status Handler
            alarmStatus = myAlarm.flag_alarmes_criados
            
            # Emit the signal
            self.sig_conn.emit(connStatus, alarmStatus)

# Init interface
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TelaInicial()
    window.show()
    sys.exit(app.exec_())
