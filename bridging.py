#calculates prophylactic enoxaparin dose
def enoxaparin():
    if Crcl < 15 and peso > 0 :
        print("Administer unfractionated Heparin by continuous intravenous infusion")
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
#calculates medium risk dose
def enox_medium_risk():
    if Crcl < 15 and peso > 0:
        print("Administer unfractionated Heparin by continuous intravenous infusion")
    if peso >= 40 and peso < 50:
        print("Enoxaparin dose 40mg SC OD")
    if peso >= 50 and peso < 60:
        print("Enoxaparin dose 60mg SC OD")
    if peso >= 60 and peso < 75:
        print("Enoxaparin dose 60mg SC OD")
    if peso >= 75 and peso < 90:
        print("Enoxaparin dose 80mg SC OD")
    if peso >= 90 and peso < 110:
        print("Enoxaparin dose 100mg SC OD")
    if peso >= 110 and peso < 125:
        print("Enoxaparin dose 120mg SC OD")
    if peso > 125 and Crcl >= 15:
        print("Contact consultant haematologist")
#calculates high risk dose
def enox_high_risk():
    if Crcl >= 15 and Crcl < 30:
        enox_medium_risk()
    if Crcl < 15 and peso > 0:
        print("Administer unfractionated Heparin by continuous intravenous infusion")
    if peso > 125 and Crcl >= 15:
        print("Contact consultant haematologist")

    if Crcl >= 30 and peso > 39 and peso < 50:
        print("Enoxaparin dose 60mg SC OD")
    if Crcl >= 30 and peso >= 50 and peso < 60:
        print("Enoxaparin dose 80mg SC OD")
    if Crcl >= 30 and peso >= 60 and peso < 75:
        print("Enoxaparin dose 100mg SC OD")
    if Crcl >= 30 and peso >= 75 and peso < 90:
        print("Enoxaparin dose 120mg SC OD")
    if Crcl >= 30 and peso >= 90 and peso < 110:
        print("Enoxaparin dose 150mg SC OD")
    if Crcl >= 30 and peso >= 110 and peso < 125:
        print("Enoxaparin dose 180mg SC OD")
#calculates mech valve dose
def mech_valve_enox():
    if Crcl >= 15 and Crcl < 30:
        enox_medium_risk()
    if Crcl < 15 and peso > 0:
        print("Administer unfractionated Heparin by continuous intravenous infusion")
    if peso > 125 and Crcl >= 15:
        print("Contact consultant haematologist")
    while Crcl >= 30:
        if peso >= 40 and peso < 50:
            print("Enoxaparin dose 40mg SC BD")
        if peso >= 50 and peso < 75:
            print("Enoxaparin dose 60mg SC BD")
        if peso >= 75 and peso < 90:
            print("Enoxaparin dose 80mg SC BD")
        if peso >= 90 and peso < 110:
            print("Enoxaparin dose 100mg SC BD")
        if peso >= 110 and peso < 125:
            print("Enoxaparin dose 120mg SC BD")
        quit()


#enter anticoagulant type and indication
medicine = input("enter anticoagulant, (w, warfarin, d, DOAC): ")
indication = input("Enter indication for anticoagulation, (AF (a), VTE (v), mechanical valve (m): ")
a = input("Enter age: ")
w = input("Enter weight in kg: ")
c = input("Enter Serum Creatinine: ")
s = input("Enter sex (m, f): ")
try :
    edad = float(a)
    peso = float(w)
    creatinina = float(c)
except ValueError:
    print("Error, please enter numeric value")
    quit()
if s == "m" :
        Crcl = ((140 - edad) * peso * 1.23) / creatinina
        print("Creatinine clearance:" , Crcl, "mL/min")
elif s == "f" :
        Crcl = ((140 - edad) * peso * 1.04) / creatinina
        print("Creatinine clearance:" , Crcl, "mL/min")
else:
        print("Error, please enter sex as m or f: ")
        quit()

#calculates risk and bridging dose if on warfarin
if medicine == "w" and indication == "a":
    option = input("TIA or stroke within less than 12 months?, (y, n): ")

    try:
        if option == "n" :
            enoxaparin()
        if option == "y" :
            enox_medium_risk()
    except:
        print("please enter a valid numeric value")
        quit()
if medicine == "w" and indication == "m":
    mech_valve_enox()
if medicine == "w" and indication == "v":
    option = input("Choose, single VTE > 12 months (1),\n VTE 3-12 months or multiple. large volume PE or active cancer (2),\n VTE < 3 months or known antithrombin deficiency or \n antiphospholipid syndrome (3): ")

    try:
        if option == "1":
            enoxaparin()
        if option == "2":
            enox_medium_risk()
        if option == "3":
            enox_high_risk()
    except:
            print("please enter a valid numeric value")
            quit()
#calculates risk and bridging dose if on a DOAC
if medicine == "d" and indication == "v" :
    option = input("Choose, single VTE > 12 months (1),\n VTE 3-12 months or multiple. large volume PE or active cancer (2),\n VTE < 3 months or known antithrombin deficiency or \n antiphospholipid syndrome (3): ")
    try:
        if option == "1":
            enoxaparin()
        if option == "2":
            enox_medium_risk()
        if option == "3":
            enox_high_risk()
    except:
        print("please enter a valid numeric value")
        quit()
if medicine == "d" and indication == "a" :
    option = input("TIA or stroke within less than 12 months?, (y, n): ")
    try:
        if option == "n" :
            enoxaparin()
        if option == "y":
            enox_medium_risk()
    except:
        print("please enter a valid numeric value")
        quit()
if medicine == "d" and indication == "m":
    print("DOAs usually not indicated for mechanical heart valves, contact consultant haematologist")
