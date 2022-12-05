import sys
import time
import urllib
import urllib.request

from PyQt6.QtCore import QDateTime, Qt, QTimer
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox, QDial, QDialog,
                             QDialogButtonBox, QFrame, QFormLayout, QGridLayout, QHBoxLayout,
                             QLabel, QLineEdit, QMessageBox, QPushButton,
                             QRadioButton, QStackedWidget, QStyleFactory, QStackedLayout, QVBoxLayout, QWidget)

proph = ['Enoxaparin dose 20mg SC OD','Enoxaparin dose 40mg SC OD','Enoxaparin dose 40mg SC BD', 'Enoxaparin dose 60mg SC BD']
proph_r = ['Enoxaparin dose 20mg SC OD', 'Enoxaparin dose 20mg SC OD', 'Enoxaparin dose 20mg SC OD', 'Enoxaparin dose 20mg SC OD' ]
wproph = ([0, 49.99], [50, 100], [100.1, 150], [150.1, 2000])
wmed = ([40, 49.99], [50, 59.99], [60, 74.99], [75, 89.99], [90, 109.99], [110, 124.99], [125, 200])
med = ['Enoxaparin dose 40mg SC OD', 'Enoxaparin dose 60mg SC OD', 'Enoxaparin dose 60mg SC OD', 'Enoxaparin dose 80mg SC OD', 'Enoxaparin dose 100mg SC OD', 'Enoxaparin dose 120mg SC OD', 'Contact consultant haematologist']
high = ['Enoxaparin dose 60mg SC OD', 'Enoxaparin dose 80mg SC OD', 'Enoxaparin dose 100mg SC OD', 'Enoxaparin dose 120mg SC OD', 'Enoxaparin dose 150mg SC OD', 'Enoxaparin dose 180mg SC OD',  'Contact consultant haematologist']
high_r = ['Enoxaparin dose 40mg SC OD', 'Enoxaparin dose 60mg SC OD', 'Enoxaparin dose 60mg SC OD', 'Enoxaparin dose 80mg SC OD', 'Enoxaparin dose 100mg SC OD', 'Enoxaparin dose 120mg SC OD',  'Contact consultant haematologist']
mech = ['Enoxaparin dose 40mg SC BD', 'Enoxaparin dose 60mg SC BD', 'Enoxaparin dose 60mg SC BD', 'Enoxaparin dose 80mg SC BD', 'Enoxaparin dose 100mg SC BD', 'Enoxaparin dose 120mg SC BD']
mech_r = ['Enoxaparin dose 40mg SC OD', 'Enoxaparin dose 60mg SC OD',  'Enoxaparin dose 60mg SC OD', 'Enoxaparin dose 80mg SC OD', 'Enoxaparin dose 100mg SC OD', 'Enoxaparin dose 120mg SC OD']

class EnoxDose:

    @staticmethod
    def drug_dose(weight, weight_table, dose_table):
        for index, bracket in enumerate(weight_table):
            if bracket[0] <= weight <= bracket[1]:
                dose = dose_table[index]
                print(dose)
                return(dose)





class Window(QDialog):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anticoagulant Dose calculator") 
        self.buttons = {'metrics': ['Age?', 'Height in cm?', 'Serum Creatinine?', 'Weight in kg?', 'Sex?'],
         'anticoagulant': ['DOAC', 'warfarin, \nacenocumarol'],
          'indication': ['VTE',  'Atrial Fibrilation', 'Mechanical Heart valve'],
           'VTE': ['single VTE > 12 months', 'VTE 3-12 months or  \n multiple, large volume PE or \n active cancer', 'VTE < 3 months \n or known antithrombin deficiency or \n antiphospholipid syndrome'],
            'af': ['No',"Yes, within the past 12 months","Yes, within the past 3 months"],
             'Mech': 'mech',
             'sexo': ['Male', 'Female'],
             'options': ['Low Risk', 'High Risk']}
        self.doses = {'VTE single VTE > 12 months' : self.enoxp_dose,
        'VTE VTE 3-12 months or  \n multiple, large volume PE or \n active cancer' : self.enoxmed,
         'VTE VTE < 3 months \n or known antithrombin deficiency or \n antiphospholipid syndrome': self.enoxhigh,
          'Atrial Fibrilation No': self.enoxp_dose,
           'Atrial Fibrilation Yes, within the past 12 months': self.enoxmed,
            'Atrial Fibrilation Yes, within the past 3 months': self.enoxmech,
             'mech': self.enoxmech}

        # Initialises variable
        self.var_1 = None
        self.var_2 = None
        self.var_3 = None
        self.var_4 = None

        # set Layout
        self.dialogLayout = QVBoxLayout()
        self.anticoagLayout = QVBoxLayout()
        self.bridgingLayout = QFormLayout()
        self.trtLayout = QFormLayout()
        self.questions_1Layout = QVBoxLayout()
        self.questions_2Layout = QVBoxLayout()
        self.questions_3Layout = QVBoxLayout()
        self.rejillaLayout = QGridLayout()

        # set radiobutton groups
        self.anticoagButtongroup = QButtonGroup()
        self.indicationButtongroup = QButtonGroup()
        
        
        # initialises stacks
        self.stack1 = QWidget()
        self.stackbridg = QWidget()
        self.stacktrt = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()
        self.stack5 = QWidget()
        

        self.stack1UI()
        self.stackbridgeUI()       
        self.stack3UI()
        self.stack4UI()
        self.stack5UI()
        self.stacktrttUI()
        

        self.stack = QStackedWidget(self)
        self.stack_1 = QStackedWidget(self)
        self.stack_2 = QStackedWidget(self)
        
        self.stack.addWidget(self.stack1)
        self.stack_1.addWidget(self.stackbridg)
        self.stack_1.addWidget(self.stacktrt)
        self.stack_2.addWidget(self.stack3)
        self.stack_2.addWidget(self.stack4)
        self.stack_2.addWidget(self.stack5)
        
        # sets UIcomponents
        self.Uicomponents()

        # add layouts
        self.setLayout(self.rejillaLayout)
        self.rejillaLayout.setColumnMinimumWidth(0, 350)
        self.rejillaLayout.addWidget(self.stack_1, 1, 0, 1, 2)
        self.rejillaLayout.addWidget(self.stack, 0, 1)
        self.stack.hide()
        self.stack_1.hide()
        

    
    # all connectors
            
    def onClicked(self):
        rB = self.anticoag_rb.sender()
        if rB.isChecked():
            self.var_1 = rB.text()
            print(self.var_1)
            
    
    def onClicked2(self):
        rBi = self.indication_rb.sender()
        if rBi.isChecked():
            self.var_2 = rBi.text()
            print(self.var_2)
            self.rejillaLayout.addWidget(self.stack_2, 0, 3)
            if self.var_2 == 'VTE':
                self.stack_2.show()
                self.stack_2.setCurrentIndex(0)
                
                print('embolia, embolia colectiva!!')
            elif self.var_2 == 'Atrial Fibrilation' and self.var_1 == 'DOAC':
                print('no lo so')
                self.stack_2.show()
                self.stack_2.setCurrentIndex(2)
            elif self.var_2 == 'Atrial Fibrilation' and self.var_1 == 'warfarin, \nacenocumarol':
                self.stack_2.show()
                self.stack_2.setCurrentIndex(1)
                print('no siento las piernas')
            else:
                self.stack_2.hide()
                self.var_4 = 'mech'
    
    def onClicked3(self):
        rBq = self.question_rb.sender()
        if rBq.isChecked():
            self.var_3 = rBq.text()
            self.var_4 = self.var_2 + ' ' + self.var_3
            print(self.var_4)

    def cb_onclicked(self):
        self.cbox = self.bridgingCheckBox.sender()
        self.stack.setVisible(self.bridgingCheckBox.isChecked())
        self.stack_1.setVisible(self.bridgingCheckBox.isChecked())
        self.stack_1.setCurrentIndex(0)
        self.stack_2.setVisible(self.bridgingCheckBox.isChecked())
        self.adjustSize()
        self.var_1 = None

    def cb_2_onclicked(self):
        self.cbox_2 = self.trtCheckBox.sender()
        self.stack_1.setVisible(self.trtCheckBox.isChecked())
        self.stack_1.setCurrentIndex(1)
        self.adjustSize()
        

    #all the bridging stacks

    def stack1UI(self):
        for anti in range(len(self.buttons['anticoagulant'])):
            self.anticoag_rb = QRadioButton(self.buttons['anticoagulant'][anti])
            self.anticoag_rb.toggled.connect(self.onClicked)
            print(anti)
            print(self.anticoag_rb)
            self.anticoagButtongroup.addButton(self.anticoag_rb)
            self.dialogLayout.addWidget(self.anticoag_rb)
        
        for i in self.buttons['indication']:
            self.indication_rb = QRadioButton(i)
            self.indication_rb.toggled.connect(self.onClicked2)
            print(i)
            print(self.indication_rb)
            self.indicationButtongroup.addButton(self.indication_rb)
            self.dialogLayout.addWidget(self.indication_rb)
        self.stack1.setLayout(self.dialogLayout)

    def stackbridgeUI(self):
        brbutton = QPushButton('brigding dose')
        brbutton.clicked.connect(self.bridgingdose)
        self.bridgingdose_entry = QLineEdit()
        self.bridgingLayout.addRow(brbutton, self.bridgingdose_entry)
        self.stackbridg.setLayout(self.bridgingLayout)

    def stacktrttUI(self):
        self.trtComboBox = QComboBox()
        self.trtComboBox.addItems(self.buttons['options'])
        trtLabel = QLabel('Please choose')
        trtLabel.setBuddy(self.trtComboBox)
        self.trtLayout.addRow(trtLabel, self.trtComboBox)
        trtbutton = QPushButton('Treatment dose')
        trtbutton.clicked.connect(self.enox_treat)
        self.trtdose_entry = QLineEdit()
        self.trtLayout.addRow(trtbutton, self.trtdose_entry)
        self.stacktrt.setLayout(self.trtLayout)
    

    def stack3UI(self):
        for q in self.buttons['VTE']:
            self.question_rb = QRadioButton(q)
            self.question_rb.toggled.connect(self.onClicked3)
            self.questions_1Layout.addWidget(self.question_rb)
        
        self.stack3.setLayout(self.questions_1Layout)        
        
    def stack4UI(self):
        for i in range(len(self.buttons['af'])-1):
            self.question_rb = QRadioButton(self.buttons['af'][i])
            self.question_rb.toggled.connect(self.onClicked3)
            self.questions_2Layout.addWidget(self.question_rb)
       
        print('hola')
        self.stack4.setLayout(self.questions_2Layout)
        
    def stack5UI(self):
        for i in range(len(self.buttons['af'])):
            self.question_rb = QRadioButton(self.buttons['af'][i])
            self.question_rb.toggled.connect(self.onClicked3)
            self.questions_3Layout.addWidget(self.question_rb)
        print('caracola')
        self.stack5.setLayout(self.questions_3Layout)

    


    #all the calculators

    def calculate_GFR(self):
        edad = int(self.entries['Age?'].text())
        altura = float(self.entries['Height in cm?'].text())
        scr = int(self.entries['Serum Creatinine?'].text())
        peso = float(self.entries['Weight in kg?'].text())
        sexo = self.sComboBox.currentText()
        if sexo == "Male":
            ibw =  50 + 0.91 * (altura - 152)
            if ibw / peso < 0.7:
                peso = ibw + (0.2 * ibw)
                crcl = ((140 - edad) * peso * 1.23) / scr
                self.GFR.setText(str(round(crcl, 2))+'mL/min')
                self.weight_used_ent.setText(str(round(peso, 2))+'kg')
                return(crcl)
                print(crcl)
            else:
                crcl = ((140 - edad) * peso * 1.23) / scr
                self.GFR.setText(str(round(crcl, 2))+'mL/min')
                self.weight_used_ent.setText(str(round(peso, 2))+'kg')
                return(crcl)
                print(crcl)

        if sexo == "Female":
            ibw = 45 + 0.91 * (altura - 152)
            if ibw / peso < 0.7:
                peso = ibw + (0.2 * ibw)
                crcl = ((140 - edad) * peso * 1.04) / scr
                self.GFR.setText(str(round(crcl, 2))+'mL/min')
                self.weight_used_ent.setText(str(round(peso, 2))+'kg')
                return(crcl)
                print(crcl)
            else:
                crcl = ((140 - edad) * peso * 1.04) / scr
                print(crcl)
                self.GFR.setText(str(round(crcl, 2))+'mL/min')
                self.weight_used_ent.setText(str(round(peso, 2))+'kg')
                return(crcl)
                print(crcl)



    def enoxp_dose(self):
        kilos = float(self.entries['Weight in kg?'].text())
        renal = float(self.GFR.text()[:(self.GFR.text().find('m'))])
        print(renal)
        if renal < 15:
            enoxap_dose = 'Heparin 5000iu SC BD'
        if 15 <= renal < 30:
            enoxap_dose = EnoxDose.drug_dose(kilos, wproph, proph_r)
            
        if renal >= 30:
            enoxap_dose = EnoxDose.drug_dose(kilos, wproph, proph)
            
        if self.var_1 == None:
            self.enox_dose.setText(enoxap_dose)
        else:
            self.bridgingdose_entry.setText(enoxap_dose)


    def enoxmed(self):
        kilos = float(self.entries['Weight in kg?'].text())
        renal = float(self.GFR.text()[:(self.GFR.text().find('m'))])
        print(renal)
        if renal < 15:
            enoxap_dose = 'Heparin continuous intravenous infusion'
        if 15 <= renal < 30:
            enoxap_dose = EnoxDose.drug_dose(kilos, wmed, med)
            
        if renal >= 30:
            enoxap_dose = EnoxDose.drug_dose(kilos, wmed, med)
        self.bridgingdose_entry.setText(enoxap_dose)

    def enoxhigh(self):
        kilos = float(self.entries['Weight in kg?'].text())
        renal = float(self.GFR.text()[:(self.GFR.text().find('m'))])
        print(renal)
        if renal < 15:
            enoxap_dose = 'Heparin continuous intravenous infusion'
        if 15 <= renal < 30:
            enoxap_dose = EnoxDose.drug_dose(kilos, wmed, high_r)
            
        if renal >= 30:
            enoxap_dose = EnoxDose.drug_dose(kilos, wmed, high)
            
        if self.var_1 == 'DOAC':
            self.enoxmech()
        self.bridgingdose_entry.setText(enoxap_dose)
    
    def enoxmech(self):
        kilos = float(self.entries['Weight in kg?'].text())
        renal = float(self.GFR.text()[:(self.GFR.text().find('m'))])
        print(renal)

        if renal < 15:
            enoxap_dose = 'Heparin continuous intravenous infusion'
        if 15 <= renal < 30:
            enoxap_dose = EnoxDose.drug_dose(kilos, wmed, mech_r)
            
        if renal >= 30:
            enoxap_dose = EnoxDose.drug_dose(kilos, wmed, mech)

        self.bridgingdose_entry.setText(enoxap_dose)
    
    def enox_treat(self):
        kilos = float(self.entries['Weight in kg?'].text())
        renal = float(self.GFR.text()[:(self.GFR.text().find('m'))])
        risk = self.trtComboBox.currentText()
        print(renal)
        if renal < 15:
            enoxap_dose = 'Heparin continuous intravenous infusion'
        if renal >= 15 and risk == 'Low Risk':
            if 15 <= renal < 30:
                enoxap_dose = EnoxDose.drug_dose(kilos, wmed, high_r)
            
            if renal >= 30:
                enoxap_dose = EnoxDose.drug_dose(kilos, wmed, high)
            self.trtdose_entry.setText(enoxap_dose)
        if renal >= 15 and risk == 'High Risk':
            if 15 <= renal < 30:
                enoxap_dose = EnoxDose.drug_dose(kilos, wmed, mech_r)
            else:
                enoxap_dose = EnoxDose.drug_dose(kilos, wmed, mech)
            self.trtdose_entry.setText(enoxap_dose)


        



    def bridgingdose(self):
        if self.var_1 == 'DOAC' and self.var_4 == 'mech':
            mensaje = QMessageBox.critical(self, 'Too Late', 'Run you fools! or contact a Haematologist')
            self.bridgingCheckBox.setChecked(False)
            self.var_4 = None
        else:
            for k, v in self.doses.items():
                if self.var_4 == k:
                    v()
                    print(f'The function chosen is {v.__name__}')
                else:
                    pass
                 
    #sets main UI

    def Uicomponents(self):
              
        self.entries = {}
        
        formas = QFormLayout()
        for m in self.buttons['metrics']:
            if m != 'Sex?':
                self.ent = QLineEdit()
                formas.addRow(m, self.ent)
                
            else:
                print('Sexo?')
                self.sComboBox = QComboBox()
                self.sComboBox.addItems(self.buttons['sexo'])
                sLabel = QLabel('Sex:?')
                sLabel.setBuddy(self.sComboBox)
                formas.addRow(sLabel, self.sComboBox)
                

            self.entries[m] = self.ent
        
        print(self.entries.items())

        self.trtCheckBox = QCheckBox("Treatment Dose")
        self.bridgingCheckBox = QCheckBox("Bridging dose")
        self.bridgingCheckBox.toggled.connect(self.cb_onclicked)
        self.trtCheckBox.toggled.connect(self.cb_2_onclicked)
        button = QPushButton('GFR')
        button2 = QPushButton('Enoxaparin dose')
        self.enox_dose = QLineEdit()    
        self.GFR = QLineEdit()
        weight_used = QLabel('Weight used')
        self.weight_used_ent = QLineEdit()
        formas.addRow(button, self.GFR)
        formas.addRow(weight_used, self.weight_used_ent)
        formas.addRow(button2, self.enox_dose)
        formas.addRow(self.bridgingCheckBox, self.trtCheckBox)
        self.rejillaLayout.addLayout(formas, 0, 0)

        button.clicked.connect(self.calculate_GFR)
        button.clicked.connect(lambda: print(self.entries['Age?'].text()))
        button2.clicked.connect(self.enoxp_dose)        
        

if __name__ == '__main__':

    app = QApplication([])
    window = Window()
    window.setGeometry(200, 200, 300, 160)
    window.show()
    sys.exit(app.exec())