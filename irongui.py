import tkinter as tk
from tkinter import ttk
from tkinter import *



#calculates iron needed as per ganzoni equation
def ganzoni():
    a = weight_entry.get()
    b = height_entry.get()
    c = Hb_entry.get()
    s = sex.get()

    peso = float(a)
    altura = float(b)
    actual_hb = float(c)
    bmi = peso / ((altura * altura) / 10000)
    if actual_hb >= 120:
        dose = 500
        print("Parenteral Iron dose", dose,"mg")
        PI_Dose.insert(0, round(dose, -2))

    if bmi > 30 and s == "Male":
        peso = 50 + 0.91 * (altura - 152)
        dose = ((120 - actual_hb) * peso * 0.24) + 500
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.insert(0, round(dose, -2))
    elif bmi > 30 and s == "Female":
        peso = 45 + 0.91 * (altura - 152)
        dose = ((120 - actual_hb) * peso * 0.24) + 500
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.insert(0, round(dose, -2))
    elif bmi <= 30 and s == "Male" or s == "Female":
        dose = ((120 - actual_hb) * peso * 0.24) + 500
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.insert(0, round(dose, -2))

def ironman():
    a = weight_entry.get()
    b = height_entry.get()
    c = Hb_entry.get()
    s = sex.get()

    peso = float(a)
    altura = float(b)
    actual_hb = float(c)
    bmi = peso / ((altura * altura) / 10000)
    if peso < 50 and actual_hb >= 100:
        dose = 20 * peso
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.insert(0, round(dose, -2))
    if peso < 50 and actual_hb < 100:
        dose = 20 * peso
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.insert(0, round(dose, -2))
    if peso >= 50 and peso < 70 and actual_hb > 100:
        dose = 1000
        print("Parenteral Iron dose 1000mg")
        PI_Dose.insert(0, round(dose, -2))
    if peso >= 50 and peso < 70 and actual_hb < 100:
        dose = 20 * peso
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.insert(0, round(dose, -2))
    if peso >= 70 and actual_hb >= 100:
        dose = 20 * peso
        if dose >= 1500:
            dose = 1500
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.insert(0, round(dose, -2))
    if peso >= 70 and actual_hb < 100:
        dose = 20 * peso
        if dose >= 2000:
            dose = 2000
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.insert(0, round(dose, -2))
#gets values from gui





 #sets window
window = tk.Tk()
window.title('Parenteral Iron Dose Calculator')
window.geometry('400x300')

#sets combobox 1
ttk.Label(window, text = "Select Sex :",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 5, padx = 10, pady = 25)

n = tk.StringVar()
sex = ttk.Combobox(window, width = 20, textvariable = n)
sex['values'] = ('Male', 'Female')
sex.grid(column = 1, row = 5)


#data entry
height = Label(window, text = "Height in cm? :").grid(column = 0, row = 15)
weight = Label(window, text = "Weight in kg? :").grid(column = 0, row = 20)
Hb = Label(window, text = "Current Hb? :").grid(column = 0, row = 25)

height_entry = IntVar()
height_entry = Entry(window, width = 20)
height_entry.grid(column = 1, row = 15)

weight_entry = IntVar()
weight_entry = Entry(window, width = 20)
weight_entry.grid(column = 1, row = 20)

Hb_entry = IntVar()
Hb_entry = Entry(window, width = 20)
Hb_entry.grid(column = 1, row = 25)

Iron_Dose = Label(window, text = 'Parenteral Iron Dose = ').grid(column = 0, row = 40)
PI_Dose = Entry(window, width = 20)
PI_Dose.grid(column = 1, row = 40)

Hf_choice = Label(window, text = "Heart failure patient? :").grid(column = 0, row = 30)
Calculate_Iron_Dosehf_button = Button(window, text = "YES", command = ironman)
Calculate_Iron_Dosehf_button.grid(column = 1, row = 30)

Calculate_Iron_dose_button = Button(window, text = "NO", command = ganzoni)
Calculate_Iron_dose_button.grid(column = 1, row = 35)



window.mainloop()
