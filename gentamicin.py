import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *


fields = [ 'Age', 'Height', 'Weight', 'Serum Creatinine', 'Creatinine Clearance', 'Gentamicin dose', 'Dose interval (hours)']
def gent_dose(entries):
    w = float(entries['Weight'].get())
    Crcl = float(entries['Creatinine Clearance'].get())
    if Crcl < 21:
            gent = 2.5 * w
            dose_int = 24
            if gent >= 180:
                gent = 180
        #dose range for 40-49kg
    if Crcl >= 21 and Crcl < 31 and w >= 40 and w < 50:
            gent = 180
            dose_int = 48
    if Crcl >= 31 and Crcl < 41 and w >= 40 and  w < 50:
            gent = 200
            dose_int = 48
    if Crcl >= 41 and Crcl < 51 and w >= 40 and  w < 50:
            gent = 240
            dose_int = 48
    if Crcl >= 51 and Crcl < 61 and w >= 40 and  w < 50:
            gent = 200
            dose_int = 24
    if Crcl > 60 and w >= 40 and w < 50:
            gent = 240
            dose_int = 24
        #dose range for 50-59kg
    if Crcl >= 21 and Crcl < 31 and w >= 50 and w < 60:
            gent = 200
            dose_int = 48
    if Crcl >= 31 and Crcl < 41 and w >= 50 and  w < 60:
            gent = 240
            dose_int = 48
    if Crcl >= 41 and Crcl < 51 and w >= 50 and  w < 60:
            gent = 280
            dose_int = 48
    if Crcl >= 51 and Crcl < 61 and w >= 50 and  w < 60:
            gent = 240
            dose_int = 24
    if Crcl > 60 and w >= 50 and w < 60:
            gent = 280
            dose_int = 24
        #dose range for 60-69kg
    if Crcl >= 21 and Crcl < 31 and w >= 60 and w < 70:
            gent = 240
            dose_int = 48
    if Crcl >= 31 and Crcl < 41 and w >= 60 and  w < 70:
            gent = 280
            dose_int = 48
    if Crcl >= 41 and Crcl < 51 and w >= 60 and  w < 70:
            gent = 320
            dose_int = 48
    if Crcl >= 51 and Crcl < 61 and w >= 70 and  w < 70:
            gent = 280
            dose_int = 24
    if Crcl > 60 and w >= 60 and w < 70:
            gent = 320
            dose_int = 24
        #dose range for 70-80kg
    if Crcl >= 21 and Crcl < 31 and w >= 70 and w <= 80:
            gent = 240
            dose_int = 48
    if Crcl >= 31 and Crcl < 41 and w >= 70 and  w <= 80:
            gent = 300
            dose_int = 48
    if Crcl >= 41 and Crcl < 51 and w >= 70 and  w <= 80:
            gent = 360
            dose_int = 48
    if Crcl >= 51 and Crcl < 61 and w >= 70 and  w <= 80:
            gent = 300
            dose_int = 24
    if Crcl > 60 and w >= 70 and w <= 80:
            gent = 360
            dose_int = 24
        #dose range for weight over 80kg
    if Crcl >= 21 and Crcl < 31 and w > 80:
            gent = 260
            dose_int = 48
    if Crcl >= 31 and Crcl < 41 and w > 80:
            gent = 320
            dose_int = 48
    if Crcl >= 41 and Crcl < 51 and w > 80:
            gent = 400
            dose_int = 48
    if Crcl >= 51 and Crcl < 61 and w > 80:
            gent = 320
            dose_int = 24
    if Crcl > 60 and w > 80:
            gent = 400
            dose_int = 24

    entries['Gentamicin dose'].delete(0, tk.END)
    entries['Gentamicin dose'].insert(0, gent)
    entries['Dose interval (hours)'].delete(0, tk.END)
    entries['Dose interval (hours)'].insert(0, dose_int)

def c_g(entries):
    altura = float(entries['Height'].get())
    peso = float(entries['Weight'].get())
    edad = float(entries['Age'].get())
    creatinina = float(entries['Serum Creatinine'].get())
    s = sex.get()


    if s == "Male" :
        ibw =  50 + 0.91 * (altura - 152)
        if ibw / peso < 0.7:
            peso = ibw + (0.2 * ibw)
            GFR = ((140 - edad) * peso * 1.23) / creatinina
            entries['Creatinine Clearance'].delete(0, tk.END)
            entries['Creatinine Clearance'].insert(0, GFR)

    if s == "Female" :
        ibw = 45 + 0.91 * (altura - 152)
        if ibw / peso < 0.7:
            peso = ibw + (0.2 * ibw)
            GFR = ((140 - edad) * peso * 1.04) / creatinina
            entries['Creatinine Clearance'].delete(0, tk.END)
            entries['Creatinine Clearance'].insert(0, GFR)

def makeform(window, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(window)

        lab = tk.Label(row, width=22, text=field+": ", anchor='w', font = ('Arial', 15, 'bold'))
        ent = tk.Entry(row, font = ('Arial', 15), relief = "ridge")
        ent.insert(0, "0")
        row.pack(side=tk.TOP,
                     fill=tk.X,
                     padx=5,
                     pady=5, expand = tk.YES)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT,
                     expand=tk.YES,
                     fill=tk.X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    window = tk.Tk()
    window.title('Gentamicin dose calculator')
    sex_fr = tk.Frame(window)
    sex_fr.pack(side = tk.TOP, fill = tk.X, padx = 5, pady = 5, expand = tk.YES)
    ttk.Label(sex_fr, text = "Sex :                ",
                font = ("Arial", 15, 'bold'), anchor = 'w').pack(side = tk.LEFT)
    n = tk.StringVar()
    sex = ttk.Combobox(sex_fr, textvariable = n, font = ('Arial', 15))
    sex['values'] = ('Male', 'Female')
    sex.pack(side = tk.RIGHT, expand = tk.YES, fill = tk.X)


    ents = makeform(window, fields)
        #results frame
    results = tk.Frame(window)
    results.pack(side = tk.TOP, fill = tk.X, padx = 5, pady = 5, expand = tk.YES)
    Calculate_Crcl_btn = Button(results, text = "Crcl", font =('Arial', 15, 'bold'), command = (lambda e=ents: c_g(e)))
    Calculate_Crcl_btn.pack(side = tk.LEFT)
    Gent_dose_btn = Button(results, text = "Gentamicin dose", font = ('Arial', 15, 'bold'), command = (lambda e=ents: gent_dose(e)))
    Gent_dose_btn.pack(side = tk.LEFT)



window.mainloop()
