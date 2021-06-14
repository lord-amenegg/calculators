import tkinter as tk
from tkinter import ttk
from tkinter import *

#calculates prophylactic enoxaparin dose
def enoxaparin():
    if Crcl < 15 and peso > 0 :
        enox_dose_entry.delete('1.0', END)
        enox_dose_entry.insert('1.0', "Heparin dose 5000units SC BD" )
    if Crcl  > 15 and Crcl < 30  and peso > 0:
        enox_dose_entry.delete('1.0', END)
        enox_dose_entry.insert('1.0', "Enoxaparin dose 20mg SC OD")
    for index, bracket in enumerate(wproph):
        if bracket[0] <= peso <= bracket[1]:
            dose = proph[index]
            enox_dose_entry.delete('1.0', END)
            enox_dose_entry.insert('1.0', dose)

#calculates medium risk dose
def enox_medium_risk():
    if Crcl < 15 and peso > 0:
        enox_dose_entry.delete('1.0', END)
        enox_dose_entry.insert('1.0', "Administer unfractionated Heparin by continuous intravenous infusion" )
    for index, bracket in enumerate(wmed):
        if bracket[0] <= peso <= bracket[1] and Crcl > 15:
            dose = med[index]
            enox_dose_entry.delete('1.0', END)
            enox_dose_entry.insert('1.0', dose)
#calculates high risk dose
def enox_high_risk():
    if Crcl >= 15 and Crcl < 30:
        enox_medium_risk()
    if Crcl < 15 and peso > 0:
        enox_dose_entry.delete('1.0', END)
        enox_dose_entry.insert('1.0', "Administer unfractionated Heparin by continuous intravenous infusion")
    if peso > 125 and Crcl >= 15:
        enox_dose_entry.delete('1.0', END)
        enox_dose_entry.insert('1.0', "Contact consultant haematologist")
    for index, bracket in enumerate(wmed):
        if bracket[0] <= peso <= bracket[1] and Crcl > 30:
            dose = high[index]
            enox_dose_entry.delete('1.0', END)
            enox_dose_entry.insert('1.0', dose)

#calculates mech valve dose
def mech_valve_enox():
    if Crcl >= 15 and Crcl < 30:
        enox_medium_risk()
    if Crcl < 15 and peso > 0:
        enox_dose_entry.delete('1.0', END)
        enox_dose_entry.insert('1.0', "Administer unfractionated Heparin by continuous intravenous infusion")
    if  Crcl >= 30 and peso > 125 and Crcl >= 15:
        enox_dose_entry.delete('1.0', END)
        enox_dose_entry.insert('1.0', "Contact consultant haematologist")
    for index, bracket in enumerate(wmech):
        if bracket[0] <= peso <= bracket[1] and Crcl > 30:
            dose = mech[index]
            enox_dose_entry.delete('1.0', END)
            enox_dose_entry.insert('1.0', dose)

#calculates prophylactic dose
def proph_dose():
    pdose = Toplevel(window)
    pdose.title('Prophylactic Enoxaparin Dose')
    GFR_lbl = ttk.Label(pdose, text = 'Creatinine clearance', font = ('', 15, 'bold'))
    GFR_entry = tk.Entry(pdose, font = ('', 15, 'bold'))
    enox_dose_entry = tk.Text(pdose, font = ('', 15), width = 25, height = 1)
    GFR_lbl.grid(row = 0, column = 0)
    GFR_entry.grid(row = 1,  column = 0)
    enox_dose_entry.config(wrap = WORD)
    enox_dose_entry.grid(row = 3, column = 0, columnspan = 2)
    s = n.get()
    edad = float(Age_entry.get())
    peso = float(Weight_entry.get())
    creatinina = float(Serum_creatinine_entry.get())

    if s == "Male" :
            Crcl = ((140 - edad) * peso * 1.23) / creatinina
            GFR_entry.delete(0, tk.END)
            GFR_entry.insert(0, Crcl)
            GFR_entry.insert(tk.END, 'ml/min')
    if s == "Female" :
            Crcl = ((140 - edad) * peso * 1.04) / creatinina
            GFR_entry.delete(0, tk.END)
            GFR_entry.insert(0, Crcl)
            GFR_entry.insert(tk.END, 'ml/min')

    if Crcl < 15 and peso > 0 :
        enox_dose_entry.delete('1.0', END)
        enox_dose_entry.insert('1.0', "Heparin dose 5000units SC BD" )

    if Crcl  > 15 and Crcl < 30  and peso > 0:
        enox_dose_entry.delete('1.0', END)
        enox_dose_entry.insert('1.0', "Enoxaparin dose 20mg SC OD")

    for index, bracket in enumerate(wproph):
        if bracket[0] <= peso <= bracket[1] and Crcl > 30:
            dose = proph[index]
            enox_dose_entry.delete('1.0', END)
            enox_dose_entry.insert('1.0', dose)


def bridging_dose():
    global Crcl
    global peso
    global edad
    s = n.get()
    edad = float(Age_entry.get())
    peso = float(Weight_entry.get())
    creatinina = float(Serum_creatinine_entry.get())
    medicine = var.get()
    indication = indication_var.get()


    if s == "Male" :
            Crcl = ((140 - edad) * peso * 1.23) / creatinina
    if s == "Female" :
            Crcl = ((140 - edad) * peso * 1.04) / creatinina

#calculates risk and bridging dose if on warfarin
    if medicine == 'warfarin, \n acenocumarol' and indication == "AF":
        if afvar.get() == "No" :
                enoxaparin()
        if afvar.get() == "Yes" :
                enox_medium_risk()

    if medicine == 'warfarin, \n acenocumarol' and indication == "MECH":
        mech_valve_enox()

    if medicine == 'warfarin, \n acenocumarol' and indication == "VTE":
            if vtevar.get() == 'single VTE > 12 months':
                enoxaparin()
            if vtevar.get() == 'VTE 3-12 months or  \n multiple, large volume PE or \n active cancer':
                enox_medium_risk()
            if vtevar.get() == 'VTE < 3 months \n or known antithrombin deficiency or \n antiphospholipid syndrome':
                enox_high_risk()

    #calculates risk and bridging dose if on a DOAC
    if medicine == "DOAC" and indication == "VTE" :
            if vtevar.get() == 'single VTE > 12 months':
                enoxaparin()
            if vtevar.get() == 'VTE 3-12 months or  \n multiple, large volume PE or \n active cancer':
                enox_medium_risk()
            if vtevar.get() == 'VTE < 3 months \n or known antithrombin deficiency or \n antiphospholipid syndrome':
                enox_high_risk()

    if medicine == "DOAC" and indication == "AF" :
            if afvar.get() == "No" :
                    enoxaparin()
            if afvar.get() == "Yes" :
                    enox_medium_risk()

    if medicine == "DOAC" and indication == "MECH" :
            enox_dose_entry.delete('1.0', END)
            enox_dose_entry.insert('1.0', "Why are you asking this? You do know DOACs are not licensed for mech heart valves, get hold of a Haematologist, now!")

#indication selector for briding dose open_vte_window
def open_indication_window():
    global var
    global indication_var
    indic_window = Toplevel(window)
    indic_window.title("Select current anticoagulant and indication")
    ac = ttk.Label(indic_window, text = "Anticoagulant? ", font = ('', 15, 'bold')).grid(column = 0, row = 7, sticky = (N, W))
    var = tk.StringVar()
    for a in range(len(anticoagulant)):
        tk.Radiobutton(indic_window, text = anticoagulant[a], font = ('', 15, 'bold'), indicatoron = 0, variable = var, value = anticoagulant[a]).grid(row = (a + 7), column = 1, sticky = (N, S, E, W))

    indic_label = ttk.Label(indic_window, text  = 'Indication ?', font = ('', 15, 'bold')).grid(column = 0, row = 12)
    indication_var = tk.StringVar()
    tk.Radiobutton(indic_window, text = "Venous Thromboembolism", font = ('', 15, 'bold'), indicatoron = 0,  variable = indication_var, value = 'VTE', command = open_vte_window).grid(row = 12, column = 1, sticky = (N, S, E, W))
    tk.Radiobutton(indic_window, text = "Atrial Fibrillation", font = ('', 15, 'bold'), indicatoron = 0,  variable = indication_var, value = 'AF', command = open_afib_window).grid(row = 13, column = 1, sticky = (N, S, E, W))
    tk.Radiobutton(indic_window, text = "Mechanical Heart Valve", font = ('', 15, 'bold'), indicatoron = 0, variable = indication_var, value = 'MECH', command = open_mech_window).grid(row = 14, column = 1, sticky = (N, S, E, W))


#atrial fibrillation window
def open_afib_window():
    global afvar
    global enox_dose_entry
    global vtevar
    afib = Toplevel(window)
    afib.title("TIA or stroke within the last 12 months?")
    afvar = tk.StringVar()
    tk.Radiobutton(afib, text = "Yes", font = ('', 15, 'bold'), indicatoron = 0, variable = afvar, value = 'Yes').grid(row = 0, column = 1, sticky = (N, S, E, W))
    tk.Radiobutton(afib, text = "No", font = ('', 15, 'bold'), indicatoron = 0,  variable = afvar, value = 'No').grid(row = 1, column = 1, sticky = (N, S, E, W))
    enox_dose = tk.Button(afib, text = "Enoxaparin dose", font = ('', 15, 'bold'), command = bridging_dose).grid(column = 0, row = 4, sticky = (N, W), padx = 5, pady = 5)
    enox_dose_entry = tk.Text(afib, font = ('', 15), width = 20, height = 4)
    enox_dose_entry.config(wrap = WORD)
    enox_dose_entry.grid(column = 1, row = 4, sticky = (N, S, E, W), padx = 5, pady = 5)

#vte window
def open_vte_window():
    vte = Toplevel(window)
    vte.title("VTE")
    global afvar
    global enox_dose_entry
    global vtevar
    vtevar = tk.StringVar()
    for v in range(len(ind_1)):
        tk.Radiobutton(vte, text = ind_1[v], font = ('', 15, 'bold'), indicatoron = 0, variable = vtevar, value = ind_1[v], command = print(ind_1[v])).grid(row = (v), column = 0, columnspan = 2, sticky = (N, S, E, W))
    enox_dose = tk.Button(vte, text = "Enoxaparin dose", font = ('', 15, 'bold'), command = bridging_dose).grid(column = 0, row = 4, sticky = (N, W), padx = 5, pady = 5)
    enox_dose_entry = tk.Text(vte, font = ('', 15), width = 20, height = 4)
    enox_dose_entry.config(wrap = WORD)
    enox_dose_entry.grid(column = 1, row = 4, sticky = (N, S, E, W), padx = 5, pady = 5)

#mechanical heart valve window
def open_mech_window():
    global afvar
    global enox_dose_entry
    global vtevar
    mech = Toplevel(window)
    mech.title("Mechanical heart Valve")
    enox_dose = tk.Button(mech, text = "Enoxaparin dose", font = ('', 15, 'bold'), command = bridging_dose).grid(column = 0, row = 4, sticky = (N, W), padx = 5, pady = 5)
    enox_dose_entry = tk.Text(mech, font = ('Arial', 15), width = 20, height = 7)
    enox_dose_entry.config(wrap = WORD)
    enox_dose_entry.grid(column = 0, row = 5, columnspan = 4, sticky = (N, S, E, W), padx = 5, pady = 5)

window = tk.Tk()
window.title("Enoxaparin bridging dose calculator")
metrics = ['Age ?', 'Height in cm ?', 'Serum Creatinine ?', 'Weight in kg ?']
anticoagulant = ['DOAC', 'warfarin, \n acenocumarol', 'Prophylactic Dose']
ind_1 = ['single VTE > 12 months', 'VTE 3-12 months or  \n multiple, large volume PE or \n active cancer', 'VTE < 3 months \n or known antithrombin deficiency or \n antiphospholipid syndrome']
sex = ['Male', 'Female']
wproph = ([0, 49.99], [50, 100], [100.1, 150], [150.1, 2000])
proph = ['Enoxaparin dose 20mg SC OD','Enoxaparin dose 40mg SC OD','Enoxaparin dose 40mg SC BD', 'Enoxaparin dose 60mg SC BD']
wmed = ([40, 49.99], [50, 59.99], [60, 74.99], [75, 89.99], [90, 109.99], [110, 124.99], [125, 200])
med = ['Enoxaparin dose 40mg SC OD', 'Enoxaparin dose 60mg SC OD', 'Enoxaparin dose 60mg SC OD', 'Enoxaparin dose 80mg SC OD', 'Enoxaparin dose 100mg SC OD', 'Enoxaparin dose 120mg SC OD', 'Contact consultant haematologist']
high = ['Enoxaparin dose 60mg SC OD', 'Enoxaparin dose 80mg SC OD', 'Enoxaparin dose 100mg SC OD', 'Enoxaparin dose 120mg SC OD', 'Enoxaparin dose 150mg SC OD', 'Enoxaparin dose 180mg SC OD']
wmech = ([40, 49.99], [50, 74.99], [75, 89.99], [90, 109.99], [110, 125])
mech = ['Enoxaparin dose 40mg SC BD', 'Enoxaparin dose 60mg SC BD', 'Enoxaparin dose 80mg SC BD', 'Enoxaparin dose 100mg SC BD', 'Enoxaparin dose 120mg SC BD']


#sets Frames
contentm = ttk.Frame(window, borderwidth = 5, relief = "ridge", padding =(3, 3, 12, 12))
contentm.grid(column = 0, row = 0, sticky = (N, S, E, W))
#fills data for entry frame

Age_lbl = ttk.Label(contentm, text = 'Age ?', font = ('', 15, 'bold'))
Age_entry = ttk.Entry(contentm, font = ('', 15, 'bold'), width = 10, justify = 'right')
Age_lbl.grid(row = 0, column = 0, sticky = (N, S, E, W))
Age_entry.grid(row = 0, column = 1, sticky = (N, E))

Height_lbl = ttk.Label(contentm, text = 'Height in cm ?', font = ('', 15, 'bold'))
Height_entry = ttk.Entry(contentm, font = ('', 15, 'bold'), width = 10, justify = 'right')
Height_lbl.grid(row = 1, column = 0, sticky = (N, S, E, W))
Height_entry.grid(row = 1, column = 1, sticky = (N, E))

SerCr_lbl = ttk.Label(contentm, text = 'Serum Creatinine ?', font = ('', 15, 'bold'))
Serum_creatinine_entry = ttk.Entry(contentm, font = ('', 15, 'bold'), width = 10, justify = 'right')
SerCr_lbl.grid(row = 2, column = 0, sticky = (N, S, E, W))
Serum_creatinine_entry.grid(row = 2, column = 1, sticky = (N, E))

Weight_lbl = ttk.Label(contentm, text = 'Weight in kg ?', font = ('', 15, 'bold'))
Weight_entry = ttk.Entry(contentm, font = ('', 15, 'bold'), width = 10, justify = 'right')
Weight_lbl.grid(row = 3, column = 0, sticky = (N, S, E, W))
Weight_entry.grid(row = 3, column = 1, sticky = (N, E))




sx = ttk.Label(contentm, text = 'Sex? ', font = ('', 15, 'bold')).grid(column = 0, row = 5, sticky = (N, W))
n = tk.StringVar()
for s in range(len(sex)):
    tk.Radiobutton(contentm, text = sex[s], font = ('', 15, 'bold'), indicatoron = 0,  var = n, value = sex[s]).grid(row = (s + 5), column = 1, sticky = (N, S, E, W))
proph_dose_btn = tk.Button(contentm, text = 'Prophylactic dose', font = ('', 15, 'bold'), command = proph_dose)
proph_dose_btn.grid(row = 16, column = 1, sticky = (N, S, E, W))
bridging_dose_btn = tk.Button(contentm, text = 'Bridging dose', font = ('', 15, 'bold'), command = open_indication_window)
bridging_dose_btn.grid(row = 18, column = 1, sticky = (N, S, E, W))


window.rowconfigure(0, weight = 3)
window.columnconfigure([0, 1, 2], weight = 3)
contentm.rowconfigure(0, weight = 3)
contentm.columnconfigure([0, 1, 2], weight = 3)

window.mainloop()
