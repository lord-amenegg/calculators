import tkinter as tk
from tkinter import ttk
from tkinter import *

def more_than_20mg_per_kg():
    a = weight_entry.get()
    dosewk1 = (20*float(a))
    dosewk2 = (dose - dosewk1)
    if dosewk2 >= 500:
        split_dose = Toplevel(window)
        split_dose.title('PLEASE READ')
        split_dose.configure(bg = 'sienna2')
        tk.Label(split_dose, text = 'Dose must be split on 2 administrations,\n with an interval of at least 1 week', font = ('Helvetica', 20, 'bold'), bg = 'sienna2').grid(column = 0, row = 41, columnspan = 2)
        dw1_lbl = tk.Label(split_dose, text = 'Dose to be given on week 1', font = ('Helvetica', 20, 'bold'), bg = 'sienna2').grid(column  = 0, row  = 42)
        tk.Label(split_dose, text = 'Dose to be given on week 2', font = ('Helvetica', 20, 'bold'), bg = 'sienna2').grid(column = 0, row = 43)
        dw1_ent = ttk.Entry(split_dose, width = 10, font = ('Helvetica', 20), justify = 'right')
        dw2_ent = ttk.Entry(split_dose, width = 10, font = ('Helvetica', 20), justify = 'right')
        dw1_ent.grid(column = 1, row = 42, sticky = (N, E), padx = 5, pady = 5)
        dw2_ent.grid(column = 1, row = 43, sticky = (N, E), padx = 5, pady = 5)
        dw1_ent.delete(0, tk.END)
        dw1_ent.insert(0, dosewk1)
        dw2_ent.delete(0, tk.END)
        dw2_ent.insert(0, round(dosewk2, -2))
    else:
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dosewk1, -2))
        PI_Dose.insert(tk.END, 'mg')

#calculates iron needed as per ganzoni equation
def ganzoni():
    a = weight_entry.get()
    b = height_entry.get()
    c = Hb_entry.get()
    s = sex.get()
    global dose
    peso = float(a)
    altura = float(b)
    actual_hb = float(c)
    bmi = peso / ((altura * altura) / 10000)
    BMI.delete(0, tk.END)
    BMI.insert(0, round(bmi, 2))
    if actual_hb >= 120:
        dose = 500
        print("Parenteral Iron dose", dose,"mg")
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -3))
        PI_Dose.insert(tk.END, 'mg')
        test_dose()

    if bmi > 30 and s == "Male" and actual_hb < 120 :
        peso = 50 + 0.91 * (altura - 152)
        peso_ent.delete(0, tk.END)
        peso_ent.insert(0, peso)
        peso_ent.insert(tk.END, 'kg')
        dose = ((120 - actual_hb) * peso * 0.24) + 500
        if dose > 20 * (float(a)):
            print("Parenteral Iron dose", round(dose, -2), "mg")
            PI_Dose.delete(0, tk.END)
            PI_Dose.insert(0, round(dose, -2))
            PI_Dose.insert(tk.END, 'mg')
            more_than_20mg_per_kg()
        else:
            print("Parenteral Iron dose", round(dose, -2), "mg")
            PI_Dose.delete(0, tk.END)
            PI_Dose.insert(0, round(dose, -2))
            PI_Dose.insert(tk.END, 'mg')
            test_dose()

    elif bmi > 30 and s == "Female" and actual_hb < 120:
        peso = 45 + 0.91 * (altura - 152)
        peso_ent.delete(0, tk.END)
        peso_ent.insert(0, peso)
        peso_ent.insert(tk.END, 'kg')
        dose = ((120 - actual_hb) * peso * 0.24) + 500
        if dose > 20 * (float(a)):
            print("Parenteral Iron dose", round(dose, -2), "mg")
            PI_Dose.delete(0, tk.END)
            PI_Dose.insert(0, round(dose, -2))
            PI_Dose.insert(tk.END, 'mg')
            more_than_20mg_per_kg()
        else:
            print("Parenteral Iron dose", round(dose, -2), "mg")
            PI_Dose.delete(0, tk.END)
            PI_Dose.insert(0, round(dose, -2))
            PI_Dose.insert(tk.END, 'mg')
            test_dose()

    elif bmi <= 30 and s == "Male" or s == "Female" and actual_hb < 120:
        peso_ent.delete(0, tk.END)
        peso_ent.insert(0, peso)
        peso_ent.insert(tk.END, 'kg')
        dose = ((120 - actual_hb) * peso * 0.24) + 500
        if dose > 20 * (float(a)):
            print("Parenteral Iron dose", round(dose, -2), "mg")
            PI_Dose.delete(0, tk.END)
            PI_Dose.insert(0, round(dose, -2))
            PI_Dose.insert(tk.END, 'mg')
            more_than_20mg_per_kg()
        else:
            print("Parenteral Iron dose", round(dose, -2), "mg")
            PI_Dose.delete(0, tk.END)
            PI_Dose.insert(0, round(dose, -2))
            PI_Dose.insert(tk.END, 'mg')
            test_dose()


#calculates iron need as per ironman trial
def ironman():
    global dose
    a = weight_entry.get()
    b = height_entry.get()
    c = Hb_entry.get()
    s = sex.get()

    peso = float(a)
    altura = float(b)
    actual_hb = float(c)
    bmi = peso / ((altura * altura) / 10000)
    BMI.delete(0, tk.END)
    BMI.insert(0, round(bmi, 2))
    peso_ent.delete(0, tk.END)
    peso_ent.insert(0, peso)
    peso_ent.insert(tk.END, 'kg')
    if peso < 50 and actual_hb >= 100:
        dose = 20 * peso
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')
        test_dose()
    if peso < 50 and actual_hb < 100:
        dose = 20 * peso
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')
        test_dose()
    if peso >= 50 and peso < 70 and actual_hb > 100:
        dose = 1000
        print("Parenteral Iron dose 1000mg")
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')
        test_dose()
    if peso >= 50 and peso < 70 and actual_hb < 100:
        dose = 20 * peso
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')
        test_dose()
    if peso >= 70 and actual_hb >= 100:
        dose = 20 * peso
        if dose >= 1500:
            dose = 1500
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')
        test_dose()
    if peso >= 70 and actual_hb < 100:
        dose = 20 * peso
        if dose >= 2000:
            dose = 2000
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')
        test_dose()

def calculate_iron_dose():
    global dose
    option = var.get()
    if option == 'ganzoni':
        ganzoni()
    if option == 'ironman':
        ironman()

def test_dose():
    vol = (dose/50) + 500
    t_dose = (25 * vol)/dose
    test_dose_ent.delete(0, tk.END)
    test_dose_ent.insert(0, round(t_dose))
    test_dose_ent.insert(tk.END, 'mL')
#sets window
window = Tk()
window.title('Parenteral Iron Dose Calculator')
window.configure(bg = 'sienna3')


#sets Frames
content = tk.Frame(window, bg = 'sienna2', borderwidth = 5, relief = "ridge")
content.grid(column = 0, row = 0, sticky = (N, S, E, W))
results = tk.Frame(window, bg = 'sienna2', borderwidth = 5, relief = "ridge")
results.grid(column = 1, row = 0, sticky=(N, S, E, W))

#data entry
#sets combobox sex
tk.Label(content, text = "Select Sex :",
        font = ('Helvetica', 20, 'bold'), bg = 'sienna2').grid(column = 0,
        row = 5, sticky = (N, W), padx = 5, pady = 5)
n = tk.StringVar()
sex = ttk.Combobox(content, width = 10, textvariable = n, font = ('Helvetica', 20), justify = 'right')
sex['values'] = ('Male', 'Female')
sex.current(1)
sex.grid(column = 1, row = 5, sticky = (N, E), padx = 5, pady = 5)
height = tk.Label(content, text = "Height in cm? :", font = ('Helvetica', 20, 'bold'), bg = 'sienna2').grid(column = 0, row = 15, sticky = (N, W), padx = 5, pady = 5)
weight = tk.Label(content, text = "Weight in kg? :", font = ('Helvetica', 20, 'bold'), bg = 'sienna2').grid(column = 0, row = 20,sticky = (N, W), padx = 5, pady = 5)
Hb = tk.Label(content, text = "Current Hb? :", font = ('Helvetica', 20, 'bold'), bg = 'sienna2').grid(column = 0, row = 25, sticky = (N, W), padx = 5, pady = 5)
height_entry = IntVar()
height_entry = ttk.Entry(content, font = ('Helvetica', 20), width = 10, justify = 'right')
height_entry.grid(column = 1, row = 15, sticky = (N, E), padx = 5, pady = 5)
weight_entry = IntVar()
weight_entry = ttk.Entry(content, font = ('Helvetica', 20), width = 10, justify = 'right')
weight_entry.grid(column = 1, row = 20, sticky = (N, E), padx = 5, pady = 5)
Hb_entry = IntVar()
Hb_entry = ttk.Entry(content, font = ('Helvetica', 20), width = 10, justify = 'right')
Hb_entry.grid(column = 1, row = 25, sticky = (N, E), padx = 5, pady = 5)
var = tk.StringVar()
tk.Radiobutton(content, text = 'Heart failure patient?', font = ('Helvetica', 20, 'bold'), bg = 'sienna2', var = var, value = 'ironman').grid(column = 0, row = 40, columnspan = 2, sticky = (W), padx = 5, pady = 5)
tk.Radiobutton(content, text = 'Any other condition?', font = ('Helvetica', 20, 'bold'), bg = 'sienna2', var = var, value = 'ganzoni').grid(column = 0, row = 41, columnspan = 2, sticky = (W), padx = 5, pady = 5)

#results entries
BMI_lbl = tk.Label(results, text = 'BMI :', font = ('Helvetica', 20, 'bold'), bg = 'sienna2').grid(column = 0, row = 1, sticky = ('N, W'), padx = 5, pady = 5)
peso_lbl = tk.Label(results, text = 'Weight used \nfor calculation :', font = ('Helvetica', 20, 'bold'), bg = 'sienna2').grid(column = 0, row = 2, sticky = ('N, W'), padx = 5, pady = 5)
BMI = ttk.Entry(results, width = 10, font = ('Helvetica', 20), justify = 'right')
BMI.grid(column = 1, row = 1, sticky = (N, E), padx = 5, pady = 5)
peso_ent = ttk.Entry(results, width = 10, font = ('Helvetica', 20), justify = 'right')
peso_ent.grid(column = 1, row = 2, sticky = (N, E), padx = 5, pady = 5)
Iron_Dose = tk.Button(results, text = 'Iron Dose', font = ('Helvetica', 20, 'bold'), command = calculate_iron_dose, bg = 'sienna3').grid(column = 0, row = 3, sticky = (N, W), padx = 5, pady = 5)
PI_Dose = ttk.Entry(results, width = 10, font = ('Helvetica', 20), justify = 'right')
PI_Dose.grid(column = 1, row = 3, sticky = (N, E), padx = 5, pady = 5)
cosmofer = ttk.Labelframe(results, text = 'If administering Cosmofer')
cosmofer.grid(column = 0, row = 4, sticky=(N, S, E, W), columnspan = 2)
test_dose_lbl = tk.Label(cosmofer, text = 'Test Dose:', font = ('Helvetica', 20, 'bold'), bg = 'sienna2')
test_dose_lbl.grid(column = 0, row = 0)
test_dose_ent = ttk.Entry(cosmofer, width = 10, font = ('Helvetica', 20, 'bold'), justify = 'right')
test_dose_ent.grid(column = 1, row = 0, sticky = (N, E), padx = 5, pady = 5)
window.bind('<Return>', calculate_iron_dose)
#quit button
btn = Button(window, text = "EXIT", font = ('Helvetica', 10, 'bold'), command = window.destroy).grid(column = 0, row = 35, sticky = (N, W), padx = 5, pady = 5)
#rowspan
window.columnconfigure([0, 1], weight = 1)
window.rowconfigure(0, weight = 1)
content.columnconfigure([0, 1, 2], weight = 1)
results.columnconfigure([0, 1, 2], weight = 1)

window.mainloop()
