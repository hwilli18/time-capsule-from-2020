# Inch and cm conversion program


def convertInchToCm():
    inch = int(input("Enter inches: "))
    cm = inch * 2.54
    print(cm, "cm")
    cm, unit = convertInchToCm()
    print("Conversion =", value, unit)

def convertCmToInch():
    cm = int(input("Enter cm: "))
    inch = cm / 2.54
    print(inch, "inch")
    inch, unit = convertInchToCm()
    print("Conversion =", value, unit)


m_choice = int(input("(1) Convert inches to cm.\n(2) Convert cm to inches\n(3) Exit Program\n"))


if m_choice == 1:
    print("You have selected: Convert inches to cm... \n'")
    convertInchToCm()
    
if m_choice == 2:
    print("You have selected: Convert cm to inches")
    convertCmToInch()

if m_choice == 3:
    print("You have selected: Exit Program \n")
    print("Goodbye!")



