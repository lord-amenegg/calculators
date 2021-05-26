import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *
import math

def inf_doseband():


        w3 = ([33, 37], [38, 45], [46, 54], [55, 62], [63, 74], [75, 79], [80, 90], [91, 95], [96, 111], [112, 125], [126, 147], [148, 159], [160, 185])
    db3 = [100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 400, 450, 500]
    w5 = ([40, 44], [45, 47], [48, 52], [53, 57], [58, 66], [67, 75], [76, 88], [89, 95], [66, 109], [110, 115], [116, 133], [134, 155], [156, 177])
    db5 = [200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600, 700, 800]
    w10 = ([40, 44], [45, 47], [48, 54], [55, 57], [58, 66], [67, 77], [78, 88], [89, 99], [100, 110], [111, 115], [116, 125], [126, 135], [136, 145], [146, 155], [156, 160])
    db10 = [400, 450, 500, 550, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]

    entries = ['Infliximab mL to draw', 'Number of inflximab vials', 'amount of saline to be drawn \n from 250mL bag']
    rbuttons = [' 3mg/kg', ' 5mg/kg', '10mg/kg']

    def dose_band():
        weight = float(weight_entry.get())
        dose = "n/a"
        peso = var.get()
        if peso == ' 3mg/kg':
            for index, bracket in enumerate(w3):
                if bracket[0] <= weight <= bracket[1]:
                    dose = db3[index]
                    inf_dose_entry.delete(0, tk.END)
                    inf_dose_entry.insert(0, dose)
                    inf_dose_entry.insert(tk.END, "mg")
                    dose_drawn.delete(0, tk.END)
                    dose_drawn.insert(0, (dose/10))
                    dose_drawn.insert(tk.END, 'mL')
                    inf_vial_num.delete(0, tk.END)
                    inf_vial_num.insert(0, math.ceil((dose/100)))
                    saline.delete(0, tk.END)
                    saline.insert(0, (dose/10))
                    saline.insert(tk.END, 'mL')


        if peso == ' 5mg/kg':
            for index, bracket in enumerate(w5):
                if bracket[0] <= weight <= bracket[1]:
                    dose = db5[index]
                    inf_dose_entry.delete(0, tk.END)
                    inf_dose_entry.insert(0, dose)
                    inf_dose_entry.insert(tk.END, "mg")
                    dose_drawn.delete(0, tk.END)
                    dose_drawn.insert(0, (dose/10))
                    dose_drawn.insert(tk.END, 'mL')
                    inf_vial_num.delete(0, tk.END)
                    inf_vial_num.insert(0, math.ceil((dose/100)))
                    saline.delete(0, tk.END)
                    saline.insert(0, (dose/10))
                    saline.insert(tk.END, 'mL')

        if peso == '10mg/kg':
            for index, bracket in enumerate(w10):
                if bracket[0] <= weight <= bracket[1]:
                    dose = db10[index]
                    inf_dose_entry.delete(0, tk.END)
                    inf_dose_entry.insert(0, dose)
                    inf_dose_entry.insert(tk.END, "mg")
                    dose_drawn.delete(0, tk.END)
                    dose_drawn.insert(0, (dose/10))
                    dose_drawn.insert(tk.END, 'mL')
                    inf_vial_num.delete(0, tk.END)
                    inf_vial_num.insert(0, math.ceil((dose/100)))
                    saline.delete(0, tk.END)
                    saline.insert(0, (dose/10))
                    saline.insert(tk.END, 'mL')


    #sets window
    window = Tk()
    window.title("Dose Banded Infliximab Calculator")

    #sets Frames
    content = ttk.Frame(window, borderwidth = 5, relief = "ridge", padding =(3, 3, 12, 12))
    content.grid(column = 0, row = 0, sticky = (N, S, E, W))
    results = ttk.Frame(window, borderwidth = 5, relief = "ridge", padding = (3, 3, 12, 12))
    results.grid(column=0, row=1, sticky= (N, S, E, W))
    msg = ttk.Frame(window, borderwidth = 5, relief = "ridge", padding = (3, 3, 12, 12))
    msg.grid(column = 0, row = 2, sticky = (N, S, E, W))

    weight = ttk.Label(content, text = "Weight in kg?    ", font = ('Arial', 15, 'bold')).grid(column = 0, row = 0, sticky = (N, W), padx = 5, pady = 5)
    weight_entry = tk.StringVar()
    weight_entry = ttk.Entry(content, font = ('Arial', 15), width = 10)
    weight_entry.grid(column = 2, row = 0, sticky = (N, S, E, W), padx = 5, pady = 5)

    var = tk.StringVar()
    for r in range(len(rbuttons)):
        tk.Radiobutton(content, text = rbuttons[r], font = (15), variable = var, value = rbuttons[r]).grid(row = (r + 2), column = 2, sticky = (N, S, E, W))

    inf_dose = tk.Button(results, text = "Infliximab dose", font = ('Arial', 15, 'bold'), command = dose_band).grid(column = 0, row = 20,sticky = (N, W), padx = 5, pady = 5)
    inf_dose_entry = ttk.Entry(results, font = ('Arial', 15), width = 10)
    inf_dose_entry.grid(column = 2, row = 20, sticky = (N, S, E, W), padx = 5, pady = 5)


    for i in range(len(entries)):
        lab = ttk.Label(msg, text = entries[i], font = ('Arial', 15)).grid(row = i, column = 0, sticky = (N, S, E, W))
    dose_drawn = ttk.Entry(msg, font = ('Arial', 15))
    dose_drawn.grid(row = 0, column = 1, sticky = (N, S, E, W))
    inf_vial_num = ttk.Entry(msg, font = ('Arial', 15))
    inf_vial_num.grid(row = 1, column = 1, sticky = (N, S, E, W))
    saline = ttk.Entry(msg, font = ('Arial', 15))
    saline.grid(row = 2, column = 1, sticky = (N, S, E, W))





    window.columnconfigure(0, weight = 3)
    window.columnconfigure(1, weight = 3)
    content.columnconfigure(0, weight = 3)
    content.columnconfigure(1, weight = 3)
    content.columnconfigure(2, weight = 3)
    results.columnconfigure(0, weight = 3)
    results.columnconfigure(1, weight = 3)
    results.columnconfigure(2, weight = 3)
    msg.columnconfigure(0, weight = 3)
    msg.columnconfigure(1, weight = 3)






    window.mainloop()


def gent():
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

        elif s == "Female" :
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
def cg():
    fields = ['Weight', 'Age', 'Serum Creatinine', 'Creatinine Clearance']
    def c_g(entries):
        peso = float(entries['Weight'].get())
        edad = float(entries['Age'].get())
        creatinina = float(entries['Serum Creatinine'].get())
        s = sex.get()


        if s == "Male" :
                Crcl = ((140 - edad) * peso * 1.23) / creatinina
                entries['Creatinine Clearance'].delete(0, tk.END)
                entries['Creatinine Clearance'].insert(0, Crcl)

        elif s == "Female" :
                Crcl = ((140 - edad) * peso * 1.04) / creatinina
                entries['Creatinine Clearance'].delete(0, tk.END)
                entries['Creatinine Clearance'].insert(0, Crcl)




    def makeform(window, fields):
        entries = {}
        for field in fields:
            #print(field)
            row = tk.Frame(window)

            lab = tk.Label(row, width=22, text=field+": ", anchor='w', font = ('Arial', 15, 'bold'))
            ent = tk.Entry(row, font = ('Arial', 15))
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

     #sets window

    if __name__ == '__main__':

     window = tk.Tk()
     window.title('Glomerular Filtration Rate calculator')
     sex_fr = tk.Frame(window)
     sex_fr.pack(side = tk.TOP, fill = tk.X, padx = 5, pady = 5, expand = tk.YES)
     ttk.Label(sex_fr, text = "Sex :                ",
             font = ("Arial", 15, 'bold'), anchor = 'w').pack(side = tk.LEFT)
     n = tk.StringVar()
     sex = ttk.Combobox(sex_fr, textvariable = n, font = ('Arial', 15))
     sex['values'] = ('Male', 'Female')
     sex.pack(side = tk.RIGHT, expand = tk.YES, fill = tk.X)


     ents = makeform(window, fields)


     Calculate_Crcl_btn = Button(window, text = "Calculate!", font =('Arial', 15, 'bold'), command = (lambda e=ents: c_g(e)))
     Calculate_Crcl_btn.pack(anchor = 'center')



    window.mainloop()

def irongui():

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
    window = Tk()
    window.title('Parenteral Iron Dose Calculator')


    #sets Frames
    content = ttk.Frame(window, borderwidth = 5, relief = "ridge", padding =(3, 3, 12, 12))
    content.grid(column = 0, row = 0, sticky = (N, S, E, W))
    results = ttk.Frame(window, borderwidth = 5, relief = "ridge")
    results.grid(column=0, row=1, sticky=(N, S, E, W))

    #sets combobox 1d
    ttk.Label(content, text = "Select Sex :",
    		font = ("Arial", 15, 'bold')).grid(column = 0,
    		row = 5, sticky = (N, W), padx = 5, pady = 5)

    n = tk.StringVar()
    sex = ttk.Combobox(content, width = 20, textvariable = n, font = ('Arial', 15))
    sex['values'] = ('Male', 'Female')
    sex.grid(column = 1, row = 5, sticky = (N, W), padx = 5, pady = 5)


    #data entry
    height = ttk.Label(content, text = "Height in cm? :", font = ('Arial', 15, 'bold')).grid(column = 0, row = 15, sticky = (N, W), padx = 5, pady = 5)
    weight = ttk.Label(content, text = "Weight in kg? :", font = ('Arial', 15, 'bold')).grid(column = 0, row = 20,sticky = (N, W), padx = 5, pady = 5)
    Hb = ttk.Label(content, text = "Current Hb? :", font = ('Arial', 15, 'bold')).grid(column = 0, row = 25, sticky = (N, W), padx = 5, pady = 5)

    height_entry = IntVar()
    height_entry = ttk.Entry(content, font = ('Arial', 15), width = 20)
    height_entry.grid(column = 1, row = 15, sticky = (N, W), padx = 5, pady = 5)

    weight_entry = IntVar()
    weight_entry = ttk.Entry(content, font = ('Arial', 15), width = 20)
    weight_entry.grid(column = 1, row = 20, sticky = (N, W), padx = 5, pady = 5)

    Hb_entry = IntVar()
    Hb_entry = ttk.Entry(content, font = ('Arial', 15), width = 20)
    Hb_entry.grid(column = 1, row = 25, sticky = (N, W), padx = 5, pady = 5)

    Iron_Dose = ttk.Label(results, text = 'Parenteral Iron Dose = ', font = ('Arial', 15, 'bold')).grid(column = 0, row = 40, sticky = (N, W), padx = 5, pady = 5)

    PI_Dose = ttk.Entry(results, width = 20, font = ('Arial', 15))
    PI_Dose.grid(column = 1, row = 40, sticky = (N, W), padx = 5, pady = 5)

    Hf_choice = ttk.Label(content, text = "Heart failure patient? :", font = ('Arial', 15, 'bold')).grid(column = 0, row = 30, sticky = (N, W), padx = 5, pady = 5)

    Calculate_Iron_Dosehf_button = Button(content, text = "YES", font = ('Arial', 15, 'bold'), command = ironman, width = 5)
    Calculate_Iron_Dosehf_button.grid(column = 1, row = 30, sticky = (N, W), padx = 5, pady = 5)

    Calculate_Iron_dose_button = Button(content, text = "NO", font = ('Arial', 15, 'bold'), command = ganzoni, width = 5)
    Calculate_Iron_dose_button.grid(column = 1, row = 35, sticky = (N, W), padx = 5, pady = 5)

    #rowspan
    window.columnconfigure(0, weight = 3)
    window.columnconfigure(1, weight = 3)
    content.columnconfigure(0, weight = 3)
    content.columnconfigure(1, weight = 3)
    content.columnconfigure(2, weight = 3)
    results.columnconfigure(0, weight = 3)
    results.columnconfigure(1, weight = 3)
    results.columnconfigure(2, weight = 3)

    window.mainloop()

window = Tk()
window.title('Pharmaceutical calculator')

content = ttk.Frame(window, borderwidth = 5, relief = 'ridge', padding = (3, 3, 12, 12))
content.grid(column = 0, row = 0, sticky = (N, S, E, W))

ttk.Label(content, text = 'Select Calculator :', font = ('Arial', 15, 'bold')).grid(column = 0, row = 0, sticky = (N, W), padx = 5, pady = 5)


C_G_button = Button(content, text = "Cockroft and Gault", font = ('Arial', 15, 'bold'), command = cg, width = 20)
C_G_button.grid(column = 0, row = 30, sticky = (N, W), padx = 5, pady = 5)
Calculate_Iron_dose_button = Button(content, text = "Parenteral Iron", font = ('Arial', 15, 'bold'), command = irongui, width = 20)
Calculate_Iron_dose_button.grid(column = 0, row = 35, sticky = (N, W), padx = 5, pady = 5)
Calculate_Gent_dose_button = Button(content, text = "Gentamicin", font = ('Arial', 15, 'bold'), command = gent, width = 20)
Calculate_Gent_dose_button.grid(column = 0, row = 40, sticky = (N, W), padx = 5, pady = 5)
Inf_db_button = Button(content, text = "Infliximab dose", font = ('Arial', 15, 'bold'), command = inf_doseband, width = 20)
Inf_db_button.grid(column = 0, row = 45, sticky = (N, W), padx = 5, pady = 5)
btn = Button(window, text = "Exit", font = ('Arial', 10, 'bold'), command = window.destroy).grid(column = 0, row = 35, sticky = (N, W), padx = 5, pady = 5)

window.mainloop()
