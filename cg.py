import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *


window = tk.Tk()
window.title('Renal function calculator')
window.geometry('600x480')


def c_g():
    peso = float(weight_entry.get())
    edad = float(Age_entry.get())
    creatinina = float(Serum_Creat_Entry.get())
    s = sex.get()


    if s == "Male" :
            Crcl = ((140 - edad) * peso * 1.23) / creatinina
            Creat_clerance.insert(0, Crcl)

    elif s == "Female" :
            Crcl = ((140 - edad) * peso * 1.04) / creatinina
            Creat_clerance.insert(0, Crcl)


ttk.Label(window, text = "Select Sex :",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 5, padx = 10, pady = 25)

n = tk.StringVar()
sex = ttk.Combobox(window, width = 20, textvariable = n)
sex['values'] = ('Male', 'Female')
sex.grid(column = 1, row = 5)

weight = tk.Label(window, text = 'weight in kg? :').grid(column = 0, row = 10, padx = 10, pady = 25)
serum_creatinine = tk.Label(window, text = 'serum Creatinine? :').grid(column = 0, row = 15, padx = 10, pady = 25)
age = tk.Label(window, text = 'Age? :').grid(column = 0, row = 20, padx = 10, pady = 25)
weight_entry = IntVar()
weight_entry = Entry(window, width = 20)
weight_entry.grid(column = 1, row = 10)
Serum_Creat_Entry = IntVar()
Serum_Creat_Entry = Entry(window, width = 20)
Serum_Creat_Entry.grid(column = 1, row = 15)
Age_entry = IntVar()
Age_entry = Entry(window, width = 20)
Age_entry.grid(column = 1, row = 20)
Calculate_Crcl_btn = Button(window, text = "Calculate!", font =('Ubuntu', 14, 'bold'), command = c_g).grid(column = 0, row = 25)
Creat_clerance = tk.Label(window, text = 'Creatinine Clearance = ').grid(column = 0, row = 30)
Creat_clerance = Entry(window, width = 20)
Creat_clerance.grid(column = 1, row = 30)


window.mainloop()
