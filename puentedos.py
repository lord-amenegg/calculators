import tkinter as tk
from tkinter import ttk
from tkinter import *

from tkinter.messagebox import *
from PIL import Image


proph = ['Enoxaparin dose 20mg SC OD','Enoxaparin dose 40mg SC OD','Enoxaparin dose 40mg SC BD', 'Enoxaparin dose 60mg SC BD']
proph_r = ['Enoxaparin dose 20mg SC OD', 'Enoxaparin dose 20mg SC OD', 'Enoxaparin dose 20mg SC OD', 'Enoxaparin dose 20mg SC OD' ]
wproph = ([0, 49.99], [50, 100], [100.1, 150], [150.1, 2000])
wmed = ([40, 49.99], [50, 59.99], [60, 74.99], [75, 89.99], [90, 109.99], [110, 124.99], [125, 200])
med = ['Enoxaparin dose 40mg SC OD', 'Enoxaparin dose 60mg SC OD', 'Enoxaparin dose 60mg SC OD', 'Enoxaparin dose 80mg SC OD', 'Enoxaparin dose 100mg SC OD', 'Enoxaparin dose 120mg SC OD', 'Contact consultant haematologist']
high = ['Enoxaparin dose 60mg SC OD', 'Enoxaparin dose 80mg SC OD', 'Enoxaparin dose 100mg SC OD', 'Enoxaparin dose 120mg SC OD', 'Enoxaparin dose 150mg SC OD', 'Enoxaparin dose 180mg SC OD']
high_r = ['Enoxaparin dose 40mg SC OD', 'Enoxaparin dose 60mg SC OD', 'Enoxaparin dose 60mg SC OD', 'Enoxaparin dose 80mg SC OD', 'Enoxaparin dose 100mg SC OD', 'Enoxaparin dose 120mg SC OD']
mech = ['Enoxaparin dose 40mg SC BD', 'Enoxaparin dose 60mg SC BD', 'Enoxaparin dose 60mg SC BD', 'Enoxaparin dose 80mg SC BD', 'Enoxaparin dose 100mg SC BD', 'Enoxaparin dose 120mg SC BD']
mech_r = ['Enoxaparin dose 40mg SC OD', 'Enoxaparin dose 60mg SC OD',  'Enoxaparin dose 60mg SC OD', 'Enoxaparin dose 80mg SC OD', 'Enoxaparin dose 100mg SC OD', 'Enoxaparin dose 120mg SC OD']


class EnoxDose:

    def __init__(self, name, weight_table):
        self.name = name
        self.weight_table = weight_table
        

    def drug_dose(self, weight, dose_table):
        
        for index, bracket in enumerate(self.weight_table):
            if bracket[0] <= weight <= bracket[1]:
                dose = dose_table[index]
                return(dose)


class EnoxDoseCalculator: 
          
    entries = {} 
        
    def __init__(self, root):
        self.root = root
        self.root.title('Enoxaparin Dose Calculator')
        self.metrics = ['Age ?', 'Height in cm ?', 'Serum Creatinine   ?', 'Weight in kg ?', 'Sex ?']
        self.anticoagulant = ['DOAC', 'warfarin, \nacenocumarol']
        self.indication = {'VTE': self.vte,  'Atrial Fibrilation': self.af, 'Mechanical Heart valve': self.mech}
        self.questions = {'VTE': ['single VTE > 12 months', 'VTE 3-12 months or  \n multiple, large volume PE or \n active cancer', 'VTE < 3 months \n or known antithrombin deficiency or \n antiphospholipid syndrome'], 'af': ['No',"Yes, within the past 12 months","Yes, within the past 3 months"], 'Mech': 'mech'}
        style = ttk.Style(root)
        style.theme_use('alt')
        print(style.theme_names())
        ttk.Style().configure('TButton', font = ('Helvetica', 20, 'bold'))
        ttk.Style().configure('TLabel', font = ('Helvetica', 20, 'bold'), justify = 'left')
        ttk.Style().configure('TRadiobutton', font = ('Helvetica', 20, 'bold'), indicatormargin = '10')
        layout = style.layout('TRadiobutton')
        print(layout)
        print(style.element_options('Radiobutton.label'))
        self.var = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var3 = tk.StringVar()        
        
             
        
        self.mainframe = ttk.Frame(root)
        self.mainframe.grid(column = 0, row = 0, sticky='nsew')
        self.contentm = ttk.Frame(self.mainframe, borderwidth = 5, relief = "ridge", padding =(3, 3, 12, 12))
        self.contentm.grid(column = 0, row = 0, sticky='nsew')
        
        n = 0
        for m in self.metrics:
            if m != 'Sex ?':
                self.lab = ttk.Label(self.contentm, text= m)
                self.ent = ttk.Entry(self.contentm, font = ('Helvetica', 20, 'bold'), justify = 'right')
                self.lab.grid(row = n, column = 0, sticky = 'nw')
                self.ent.grid(row = n, column = 1, sticky = 'ne')
                n = n + 1
            else:
                gender = ['Male', 'Female']
                self.sexo = tk.StringVar()
                for s in range(len(gender)):
                    ttk.Radiobutton(self.contentm, text = gender[s],  var = self.sexo, value = gender[s]).grid(row = n, column = (s), sticky = (N, S, E, W), padx = 5, pady = 5)
                n = n +1
            self.entries[m] = self.ent
            print(self.entries)
        self.entries['Age ?'].focus()
        self.GFR_button = ttk.Button(self.contentm, text = 'GFR', command = self.GFR)
        self.GFR_button.grid(row = n, column = 0, sticky=(N, S, E, W))
        self.bridging_dose_btn = ttk.Button(self.contentm, text = 'Bridging dose', command = self.bridging_dose)
        self.bridging_dose_btn.grid(row = n, column = 1, sticky = (N, S, E, W))
        n = n+1

        self.pdose = ttk.Labelframe(self.mainframe, text= 'Enoxaparin dose', borderwidth = 5, relief = "ridge", padding =(3, 3, 12, 12))
        self.pdose.grid(column = 0, row = 1, sticky = (N, S, E, W))
        self.anticoag_dose_btn = ttk.Button(self.pdose, text = 'Anticoagulant Dose', command = self.anticoag_dose)
        self.anticoag_dose_btn.grid(row = 0, column = 0, sticky = (N, S, E, W), columnspan = 2)
        self.weight_used_lbl = ttk.Label(self.pdose, text = 'Weight used')
        self.weight_used_ent = ttk.Entry(self.pdose, font = ('Helvetica', 20, 'bold'), justify = 'right')
        self.GFR_lbl = ttk.Label(self.pdose, text = 'Creatinine clearance')
        self.GFR_entry = tk.Entry(self.pdose, font = ('Helvetica', 20, 'bold'), justify= 'right')
        self.enox_dose_entry = tk.Entry(self.pdose, font = ('Helvetica', 20, 'bold'), width = 30, justify='right')
        self.weight_used_lbl.grid(row = 1, column= 0, sticky='nw')
        self.weight_used_ent.grid(row = 1, column = 1, sticky = 'ne')
        self.GFR_lbl.grid(row = 2, column = 0, sticky = 'nw')
        self.GFR_entry.grid(row = 2,  column = 1, sticky = 'ne')
        self.enox_dose_entry.grid(row = 3, column = 0, sticky = 'nswe', columnspan=2)
        self.root.bind('<Return>', self.anticoag_dose)
            

    def GFR(self):

        altura = float(self.entries['Height in cm ?'].get())
        peso = float(self.entries['Weight in kg ?'].get())
        sex = self.sexo.get()
        edad = float(self.entries['Age ?'].get())
        creatinina = float(self.entries['Serum Creatinine   ?'].get())

        if sex == "Male":
            ibw =  50 + 0.91 * (altura - 152)
            if ibw / peso < 0.7:
                peso = ibw + (0.2 * ibw)
                crcl = ((140 - edad) * peso * 1.23) / creatinina
                self.GFR_entry.delete(0, tk.END)
                self.GFR_entry.insert(0, round(crcl, 2))
                self.weight_used_ent.delete(0, tk.END)
                self.weight_used_ent.insert(0, str(round(peso, 2))+'kg')
                return(crcl)
                print(crcl)
            else:
                crcl = ((140 - edad) * peso * 1.23) / creatinina
                self.GFR_entry.delete(0, tk.END)
                self.GFR_entry.insert(0, round(crcl, 2))
                self.weight_used_ent.delete(0, tk.END)
                self.weight_used_ent.insert(0, str(round(peso, 2))+'kg')
                return(crcl)
                print(crcl)

        if sex == "Female":
            ibw = 45 + 0.91 * (altura - 152)
            if ibw / peso < 0.7:
                peso = ibw + (0.2 * ibw)
                crcl = ((140 - edad) * peso * 1.04) / creatinina
                self.GFR_entry.delete(0, tk.END)
                self.GFR_entry.insert(0, str(round(crcl, 2))+'mL/min')
                self.weight_used_ent.delete(0, tk.END)
                self.weight_used_ent.insert(0, str(round(peso, 2))+'kg')
                return(crcl)
                print(crcl)
            else:
                crcl = ((140 - edad) * peso * 1.04) / creatinina
                print(crcl)
                self.GFR_entry.delete(0, tk.END)
                self.GFR_entry.insert(0, str(round(crcl, 2))+'mL/min')
                self.weight_used_ent.delete(0, tk.END)
                self.weight_used_ent.insert(0, str(round(peso, 2))+'kg')
                return(crcl)
                print(crcl)

    def bridging_dose(self):
         
        self.bridging_dose_frame = ttk.Labelframe(self.mainframe, text = 'Select anticoagulant and indication', borderwidth = 5, relief = "ridge", padding =(3, 3, 12, 12))
        self.bridging_dose_frame.grid(row = 0, column=1, sticky ='nsew')
        for a in range(len(self.anticoagulant)):
            ttk.Radiobutton(self.bridging_dose_frame, text = self.anticoagulant[a], variable =self.var, value = self.anticoagulant[a]).grid(row = (a), column = 0, padx = 5, pady = 5, sticky = (N, S, E, W))
        for i, (k, v) in enumerate(self.indication.items()):
            ttk.Radiobutton(self.bridging_dose_frame, text = k, variable = self.var2, value = k, command = v).grid(row = i+2, column =0, sticky = 'nswe')
        self.restart = ttk.Button(self.bridging_dose_frame, text = 'Start Over', command = self.start_over)
        self.restart.grid(row = 5, column =0)
        
    
    
    def vte(self):

        try:
            self.qframe.destroy()
            self.qframe = ttk.Labelframe(self.mainframe, text= 'Recent VTE ?', borderwidth = 5, relief = "ridge", padding =(3, 3, 12, 12))
            self.qframe.grid(row =1, column = 1)
            self.var3 = tk.StringVar()
            for i in range(len(self.questions['VTE'])):
                ttk.Radiobutton(self.qframe, text = self.questions['VTE'][i],  variable = self.var3, value = self.questions['VTE'][i]).grid(row = i, column =0, sticky = 'nswe')
            

        except AttributeError:
            self.qframe = ttk.Labelframe(self.mainframe, text= 'Recent VTE ?', borderwidth = 5, relief = "ridge", padding =(3, 3, 12, 12))
            self.qframe.grid(row =1, column = 1)
            self.var3 = tk.StringVar()
            for i in range(len(self.questions['VTE'])):
                ttk.Radiobutton(self.qframe, text = self.questions['VTE'][i],  variable = self.var3, value = self.questions['VTE'][i]).grid(row = i, column =0, sticky = 'nswe')
            


    def af(self):
        d = len(self.questions['af'])
        print(d)
        try:
            self.qframe.destroy()    
            self.qframe = ttk.Labelframe(self.mainframe, text= 'Recent TIA ?', borderwidth = 5, relief = "ridge", padding =(3, 3, 12, 12))
            self.qframe.grid(row =1, column = 1, sticky = 'nswe')
           
            print(self.var.get())

            if self.var.get() == self.anticoagulant[1]:
                d = d - 1
                for i in range(d):
                    ttk.Radiobutton(self.qframe, text = self.questions['af'][i],  variable = self.var3, value = self.questions['af'][i]).grid(row = i, column =0, sticky = 'nswe')
                    
            
            else:
                for i in range(d):
                    ttk.Radiobutton(self.qframe, text = self.questions['af'][i],  variable = self.var3, value = self.questions['af'][i]).grid(row = i, column =0, sticky = 'nswe')
                   

        except AttributeError: 
            self.qframe = ttk.Labelframe(self.mainframe, text= 'Recent TIA ?', borderwidth = 5, relief = "ridge", padding =(3, 3, 12, 12))
            self.qframe.grid(row =1, column = 1, sticky = 'nswe')
            self.var3 = tk.StringVar()
            if self.var2.get() == 'warfarin, \n acenocumarol':
                d = d - 1
                print(d)
                for i in range(d):
                #for i in range(len(self.questions['af'])):
                    ttk.Radiobutton(self.qframe, text = self.questions['af'][i],  variable = self.var3, value = self.questions['af'][i]).grid(row = i, column =0, sticky = 'nswe')
                    
            else:
                print(d+1)
                for i in range(d):
                #for i in range(len(self.questions['af'])):
                    ttk.Radiobutton(self.qframe, text = self.questions['af'][i],  variable = self.var3, value = self.questions['af'][i]).grid(row = i, column =0, sticky = 'nswe')
                    


    

    def mech(self):
        try:
            self.qframe.destroy()
            
        except AttributeError:
            pass
                      
            

       
    def anticoag_dose(self, *args):
        kilos = float(self.entries['Weight in kg ?'].get())
        renal = float(self.GFR_entry.get()[:(self.GFR_entry.get().find('m'))])
        #float(GFR.text()[:(GFR.text().find('m'))])

        if self.var.get() != 'DOAC' or self.var.get() != 'warfarin, \nacenocumarol':
            if renal < 30:
                enox_dose = enoxp.drug_dose(kilos, proph_r)
                self.enox_dose_entry.delete(0, tk.END)
                self.enox_dose_entry.insert(0, enox_dose)
            else:
                enox_dose = enoxp.drug_dose(kilos, proph)
                self.enox_dose_entry.delete(0, tk.END)
                self.enox_dose_entry.insert(0, enox_dose)



        if self.var.get() == 'DOAC' and self.var2.get() == 'Mechanical Heart valve':
            img = Image.open('doacmech.jpg')
            img.show()
                        

        if renal < 15:
            if self.var.get() != 'DOAC' or self.var.get() != 'warfarin, \nacenocumarol':
                self.enox_dose_entry.delete(0, tk.END)
                self.enox_dose_entry.insert(0, "Heparin dose 5000units SC BD")
            
            if self.var.get() == 'DOAC' or self.var.get() == 'warfarin, \nacenocumarol':
                self.enox_dose_entry.delete(0, tk.END)
                self.enox_dose_entry.insert(0, "Heparin continuous intravenous infusion")
        

        if self.var2.get() == 'Mechanical Heart valve' and self.var.get() == 'warfarin, \nacenocumarol' and renal >= 15:
            if renal < 30:
                enox_dose = enoxbridg.drug_dose(kilos, mech_r)
                self.enox_dose_entry.delete(0, tk.END)
                self.enox_dose_entry.insert(0, enox_dose)
            else:
                enox_dose = enoxbridg.drug_dose(kilos, mech)
                self.enox_dose_entry.delete(0, tk.END)
                self.enox_dose_entry.insert(0, enox_dose)
        
        if self.var2.get() == 'Atrial Fibrilation' and renal >= 15:
            if self.var3.get() == self.questions['af'][0]:
                if renal < 30:
                    enox_dose = enoxp.drug_dose(kilos, proph_r)
                    self.enox_dose_entry.delete(0, tk.END)
                    self.enox_dose_entry.insert(0, enox_dose)
                else:
                    enox_dose = enoxp.drug_dose(kilos, proph)
                    self.enox_dose_entry.delete(0, tk.END)
                    self.enox_dose_entry.insert(0, enox_dose)
                
            if self.var3.get() == self.questions['af'][1]:
                enox_dose = enoxbridg.drug_dose(kilos, med)
                self.enox_dose_entry.delete(0, tk.END)
                self.enox_dose_entry.insert(0, enox_dose)
                

            if self.var3.get() == self.questions['af'][2]:
                if renal < 30:
                    enox_dose = enoxbridg.drug_dose(kilos, high_r)
                    self.enox_dose_entry.delete(0, tk.END)
                    self.enox_dose_entry.insert(0, enox_dose)
                else:
                    enox_dose = enoxbridg.drug_dose(kilos, high)
                    self.enox_dose_entry.delete(0, tk.END)
                    self.enox_dose_entry.insert(0, enox_dose)

        if self.var2.get() == 'VTE' and renal >= 15:
            if self.var3.get() == 'single VTE > 12 months':
                if renal < 30:
                    enox_dose = enoxp.drug_dose(kilos, proph_r)
                    self.enox_dose_entry.delete(0, tk.END)
                    self.enox_dose_entry.insert(0, enox_dose)
                else:
                    
                    enox_dose = enoxp.drug_dose(kilos, proph)
                    self.enox_dose_entry.delete(0, tk.END)
                    self.enox_dose_entry.insert(0, enox_dose)
                    
            if self.var3.get() == self.questions['VTE'][1]:
                enox_dose = enoxbridg.drug_dose(kilos, med)
                self.enox_dose_entry.delete(0, tk.END)
                self.enox_dose_entry.insert(0, enox_dose)

            if self.var3.get() == self.questions['VTE'][2]:
                if renal < 30:
                    enox_dose = enoxbridg.drug_dose(kilos, high_r)
                    self.enox_dose_entry.delete(0, tk.END)
                    self.enox_dose_entry.insert(0, enox_dose)
                else:
                    enox_dose = enoxbridg.drug_dose(kilos, high)
                    self.enox_dose_entry.delete(0, tk.END)
                    self.enox_dose_entry.insert(0, enox_dose)
            
    def start_over(self):
        try:
            self.bridging_dose_frame.destroy()
            self.qframe.destroy()
            entradas = list(self.entries.values())
            for e in range(len(entradas)-1):
                entradas[e].delete(0, tk.END)
            self.weight_used_ent.delete(0, tk.END)
            self.enox_dose_entry.delete(0, tk.END)
            self.GFR_entry.delete(0, tk.END)
            self.entries['Age ?'].focus()
        except AttributeError:
            entradas = list(self.entries.values())
            for e in range(len(entradas)-1):
                entradas[e].delete(0, tk.END)
            self.weight_used_ent.delete(0, tk.END)
            self.enox_dose_entry.delete(0, tk.END)
            self.GFR_entry.delete(0, tk.END)
            self.entries['Age ?'].focus()


enoxp = EnoxDose('Prophylactic dose', wproph)
enoxbridg = EnoxDose('Bridging Dose', wmed)

        
root = Tk()
EnoxDoseCalculator(root)


#print(dir(EnoxDoseCalculator))

root.mainloop()