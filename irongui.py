import tkinter as tk
from tkinter import ttk
from tkinter import *

def iron():
    print('que pasa torpedo?')
    #calculates iron needed as per ganzoni equation
    def ganzoni():
        if actual_hb >= 120:
            dose = 500
            print("Parenteral Iron dose", dose,"mg")
            quit()
        if bmi > 30 and s == "Male":
            peso = 50 + 0.91 * (altura - 152)
            dose = ((120 - actual_hb) * peso * 0.24) + 500
            print("Parenteral Iron dose", round(dose, -2), "mg")
        elif bmi > 30 and s == "Female":
            peso = 45 + 0.91 * (altura - 152)
            dose = ((120 - actual_hb) * peso * 0.24) + 500
            print("Parenteral Iron dose", round(dose, -2), "mg")
        elif bmi <= 30 and s == "m" or s == "f":
            dose = ((120 - actual_hb) * peso * 0.24) + 500
            print("Parenteral Iron dose", round(dose, -2), "mg")

    #calculates iron needed for heart failure patinets
    def ironman():
        if peso < 50 and actual_hb >= 100:
            dose = 20 * peso
            print("Parenteral Iron dose", round(dose, -2), "mg")
        if peso < 50 and actual_hb < 100:
            dose = 20 * peso
            print("Parenteral Iron dose", round(dose, -2), "mg")
        if peso >= 50 and peso < 70 and actual_hb > 100:
            print("Parenteral Iron dose 1000mg")
        if peso >= 50 and peso < 70 and actual_hb < 100:
            dose = 20 * peso
            print("Parenteral Iron dose", round(dose, -2), "mg")
        if peso >= 70 and actual_hb >= 100:
            dose = 20 * peso
            if dose >= 1500:
                dose = 1500
            print("Parenteral Iron dose", round(dose, -2), "mg")
        if peso >= 70 and actual_hb < 100:
            dose = 20 * peso
            if dose >= 2000:
                dose = 2000
            print("Parenteral Iron dose", round(dose, -2), "mg")

#gets values from gui
    a = weight_entry.get()
    b = height_entry.get()
    c = Hb_entry.get()
    d = hf_state.get()
    s = sex.get()

    peso = float(a)
    altura = float(b)
    actual_hb = float(c)
    bmi = peso / ((altura * altura) / 10000)


    print('tocame los cojones')
    if hf_state == "1":
        ironman()
    if hf_state != "0":
        ganzoni()

    print('mamon')
 #sets window
window = tk.Tk()
window.title('Parenteral Iron Dose Calculator')
window.geometry('600x480')

#sets combobox 1
ttk.Label(window, text = "Select Sex :",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 5, padx = 10, pady = 25)
#sets combobox 2
ttk.Label(window, text = 'Heart Failure ?', font = ('Ubuntu, 10')).grid(column = 0, row = 10)
n = tk.StringVar()
sex = ttk.Combobox(window, width = 20, textvariable = n)
sex['values'] = ('Male', 'Female')
sex.grid(column = 1, row = 5)
h = tk.StringVar()
hf_state = ttk.Combobox(window, width = 20, textvariable = h)
hf_state['values'] = ('Yes', 'No')
hf_state.grid(column = 1, row = 10)





#data entry
height = Label(window, text = "Height in cm? :").grid(column = 0, row = 15)
weight = tk.Label(window, text = "weight in kg? :").grid(column = 0, row = 20)
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

Calculate_Iron_dose_button = Button(window, text = "Calculate!", command = iron)
Calculate_Iron_dose_button.grid(column = 0, row = 30)



window.mainloop()
