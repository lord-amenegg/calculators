import tkinter as tk
import math
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *

w3 = ([33, 37], [38, 45], [46, 54], [55, 62], [63, 74], [75, 79], [80, 90], [91, 95], [96, 111], [112, 125], [126, 147], [148, 159], [160, 185])
db3 = [100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 400, 450, 500]
w5 = ([40, 44], [45, 47], [48, 52], [53, 57], [58, 66], [67, 75], [76, 88], [89, 95], [96, 109], [110, 115], [116, 133], [134, 155], [156, 177])
db5 = [200, 225, 250, 275, 300, 350, 400, 450, 500, 550, 600, 700, 800]
w10 = ([40, 44], [45, 47], [48, 54], [55, 57], [58, 66], [67, 77], [78, 88], [89, 99], [100, 110], [111, 115], [116, 125], [126, 135], [136, 145], [146, 155], [156, 160])
db10 = [400, 450, 500, 550, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]

entries = ['Infliximab mL to draw', 'Number of inflximab vials', 'amount of saline to be drawn \n from 250mL bag']
rbuttons = [' 3mg/kg', ' 5mg/kg', '10mg/kg']

def dose_band():
    weight = int(round(float(weight_entry.get())))
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

#sets entries and buttons
weight = ttk.Label(content, text = "Weight in kg?    ", font = ('Arial', 15, 'bold')).grid(column = 0, row = 0, sticky = (N, W), padx = 5, pady = 5)
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




#configures resizing
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
