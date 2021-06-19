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
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')


    if bmi > 30 and s == "Male":
        peso = 50 + 0.91 * (altura - 152)
        dose = ((120 - actual_hb) * peso * 0.24) + 500
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')
    elif bmi > 30 and s == "Female":
        peso = 45 + 0.91 * (altura - 152)
        dose = ((120 - actual_hb) * peso * 0.24) + 500
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')
    elif bmi <= 30 and s == "Male" or s == "Female":
        dose = ((120 - actual_hb) * peso * 0.24) + 500
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')

#calculates iron need as per ironman trial
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
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')
    if peso < 50 and actual_hb < 100:
        dose = 20 * peso
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')
    if peso >= 50 and peso < 70 and actual_hb > 100:
        dose = 1000
        print("Parenteral Iron dose 1000mg")
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')
    if peso >= 50 and peso < 70 and actual_hb < 100:
        dose = 20 * peso
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')
    if peso >= 70 and actual_hb >= 100:
        dose = 20 * peso
        if dose >= 1500:
            dose = 1500
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')
    if peso >= 70 and actual_hb < 100:
        dose = 20 * peso
        if dose >= 2000:
            dose = 2000
        print("Parenteral Iron dose", round(dose, -2), "mg")
        PI_Dose.delete(0, tk.END)
        PI_Dose.insert(0, round(dose, -2))
        PI_Dose.insert(tk.END, 'mg')

def calculate_iron_dose():
    option = var.get()
    if option == 'ganzoni':
        ganzoni()
    if option == 'ironman':
        ironman()

#sets window
window = Tk()
window.title('Parenteral Iron Dose Calculator')

#sets Frames
content = ttk.Frame(window, borderwidth = 5, relief = "ridge", padding =(3, 3, 12, 12))
content.grid(column = 0, row = 0, sticky = (N, S, E, W))
results = ttk.Frame(window, borderwidth = 5, relief = "ridge")
results.grid(column=0, row=1, sticky=(N, S, E, W))

#sets combobox sex
ttk.Label(content, text = "Select Sex :",
        font = ("Arial", 15, 'bold')).grid(column = 0,
        row = 5, sticky = (N, W), padx = 5, pady = 5)

n = tk.StringVar()
sex = ttk.Combobox(content, width = 10, textvariable = n, font = ('Arial', 15), justify = 'right')
sex['values'] = ('Male', 'Female')
sex.grid(column = 1, row = 5, sticky = (N, E), padx = 5, pady = 5)


#data entry
height = ttk.Label(content, text = "Height in cm? :", font = ('Arial', 15, 'bold')).grid(column = 0, row = 15, sticky = (N, W), padx = 5, pady = 5)
weight = ttk.Label(content, text = "Weight in kg? :", font = ('Arial', 15, 'bold')).grid(column = 0, row = 20,sticky = (N, W), padx = 5, pady = 5)
Hb = ttk.Label(content, text = "Current Hb? :", font = ('Arial', 15, 'bold')).grid(column = 0, row = 25, sticky = (N, W), padx = 5, pady = 5)

height_entry = IntVar()
height_entry = ttk.Entry(content, font = ('Arial', 15), width = 10, justify = 'right')
height_entry.grid(column = 1, row = 15, sticky = (N, E), padx = 5, pady = 5)

weight_entry = IntVar()
weight_entry = ttk.Entry(content, font = ('Arial', 15), width = 10, justify = 'right')
weight_entry.grid(column = 1, row = 20, sticky = (N, E), padx = 5, pady = 5)

Hb_entry = IntVar()
Hb_entry = ttk.Entry(content, font = ('Arial', 15), width = 10, justify = 'right')
Hb_entry.grid(column = 1, row = 25, sticky = (N, E), padx = 5, pady = 5)

Iron_Dose = tk.Button(results, text = 'Iron Dose = ', font = ('Arial', 15, 'bold'), command = calculate_iron_dose).grid(column = 0, row = 40, sticky = (N, W), padx = 5, pady = 5)

PI_Dose = ttk.Entry(results, width = 10, font = ('Arial', 15), justify = 'right')
PI_Dose.grid(column = 1, row = 40, sticky = (N, E), padx = 5, pady = 5)

var = tk.StringVar()
tk.Radiobutton(content, text = 'Heart failure patient?', font = ('Arial', 15, 'bold'), var = var, value = 'ironman').grid(column = 0, row = 40, columnspan = 2, sticky = (W), padx = 5, pady = 5)
tk.Radiobutton(content, text = 'Any other condition?', font = ('Arial', 15, 'bold'), var = var, value = 'ganzoni').grid(column = 0, row = 41, columnspan = 2, sticky = (W), padx = 5, pady = 5)
#quit button
btn = Button(window, text = "Exit", font = ('Arial', 15, 'bold'), command = window.destroy).grid(column = 0, row = 35, sticky = (N, W), padx = 5, pady = 5)
#rowspan
window.columnconfigure([0, 1], weight = 1)
window.rowconfigure(0, weight = 1)
content.columnconfigure([0, 1, 2], weight = 1)
results.columnconfigure([0, 1, 2], weight = 1)

window.mainloop()
