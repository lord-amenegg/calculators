def enoxaparin():
    if Crcl < 15 and peso > 0 :
        print("Consider Heparin 5000 units SC BD")
    if Crcl  > 15 and Crcl < 30  and peso > 0:
        print("Enoxaparin dose 20mg SC OD")
    if peso < 50 and Crcl > 30 :
        print("Enoxaparin dose 20mg SC OD")
    if peso >= 50 and peso <= 100 and Crcl >= 30 :
        print("Enoxaparin dose 40mg SC OD")
    if peso > 100 and peso < 151 and Crcl > 30:
        print ("Enoxaparin dose 40mg SC BD")
    if peso > 150 and Crcl > 30 :
        print("Enoxaparin dose 60mg SC BD")

def zoledronate():
    if Crcl < 30 :
        print("zoledronate contraindicated, only use if treating hypercalcaemia")
    if Crcl >= 30 and Crcl < 40 :
        print("zoledronate dose 3mg")
    if Crcl >= 40 and Crcl < 50 :
        print("zoledronate dose 3.3mg")
    if Crcl >= 50 and Crcl < 61 :
        print("zoledronate dose 3.5mg")
    if Crcl > 60 :
        print("zoledronate dose 4mg")

a = input("Enter age: ")
w = input("Enter weight in kg: ")
c = input("Enter Serum Creatinine: ")
s = input("Enter sex (m, f): ")
d = input("Enter drug: (enoxaparin, zoledronate) ")
#ensures correct data is entered
try :
    edad = float(a)
    peso = float(w)
    creatinina = float(c)
except ValueError:
    print("Error, please enter numeric value")
    quit()


#ensures only m or f are entered, returns creatinine clearance
if s == "m" :
        Crcl = ((140 - edad) * peso * 1.23) / creatinina
        print("Creatinine clearance:" , Crcl, "mL/min")
elif s == "f" :
        Crcl = ((140 - edad) * peso * 1.04) / creatinina
        print("Creatinine clearance:" , Crcl, "mL/min")
else:
        print("Error, please enter sex as m or f: ")
        quit()
#calculates enoxaparin dose
if d == "enoxaparin" :
    enoxaparin()
#calculates zoledronate dose
elif d == "zoledronate":
    zoledronate()
#returns error message if incorrect drug entered
else:
    print("Error, please enter drug name as enoxaparin or zoledronate")
