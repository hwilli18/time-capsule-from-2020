'''import re
import time

def check_ask():
    code = input("Enter your postcode: ")
    valid = re.match("[A-Z][A-Z][0-9]",code)
    if valid:
        time.sleep(0.5)
        print("That looks OK")
    else:
        time.sleep(1.5)
        print("Erm, try again!")
        check_ask()

check_ask()'''



#Worksheet 1 Qu 3: Program tests postcodes according to the rule,
#"starts with 2 capital letters then a number"

import re
print ("Test as many postcodes as you like.. press Enter to end.")
anotherGo = True
while anotherGo:
    postcode = input("Please input your postcode: ")
    valid = re.match("[A-Z]+[0-9]+[0-9][A-Z]+",postcode)
    if len(postcode)==0:
        exit()
    else:
        if valid:
            print("Valid Postcode")
        else:
            print("Invalid Postcode")

















