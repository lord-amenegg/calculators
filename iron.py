def ganzoni():
    if actual_hb >= 120:
        dose = 500
        print("Parenteral Iron dose", dose,"mg")
        quit()
    if bmi > 30 and s == "m":
        peso = 50 + 0.91 * (altura - 152)
        dose = ((120 - actual_hb) * peso * 0.24) + 500
        print("Parenteral Iron dose", round(dose, -2), "mg")
    elif bmi > 30 and s == "f":
        peso = 45 + 0.91 * (altura - 152)
        dose = ((120 - actual_hb) * peso * 0.24) + 500
        print("Parenteral Iron dose", round(dose, -2), "mg")
    elif bmi <= 30 and s == "m" or s == "f":
        dose = ((120 - actual_hb) * peso * 0.24) + 500
        print("Parenteral Iron dose", round(dose, -2), "mg")
    else:
        print("Error, please enter sex as m or f")
        quit()
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

a = input("Enter weight: ")
b = input("Enter height: ")
c = input("Enter current Hb: ")
d = input("Heart Failure patient? yes(y), no(n):")
s = input("Enter sex: male(m), female(f) ")

try:
    peso = float(a)
    altura = float(b)
    actual_hb = float(c)
    bmi = peso / ((altura * altura) / 10000)
except ValueError:
    print("Error, please enter numeric value")
    quit()


if d == "y":
    ironman()
elif d == "n":
    ganzoni()
else:
    print("Error, please enter y or n or m or f as values")
