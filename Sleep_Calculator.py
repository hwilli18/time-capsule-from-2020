# 2018

print("Welcome to the Sleep Calculator")
print("******************************************************")

print ("\n")

name = input("PLEASE ENTER YOUR NAME")

hourspentinbed = input("Hello " + name + "How many hours per night do you sleep? ")
print ("****************************************************************************")

hourspentinbedperweek = float(hourspentinbed) * 7
hourspentinbedpermonth = float(hourspentinbedperweek) * 4.35
dayspentinbedpermonth = float(hourspentinbedpermonth) / 24

dayspentinbedpermonth = round(dayspentinbedpermonth)
hourspentinbedpermonth = round(hourspentinbedpermonth,2)

print ("\nYou sleep",hourspentinbedperweek,"hours per week")
print ("You sleep",hourspentinbedpermonth,"hours per month")
print ("This equates to roughly",dayspentinbedpermonth,"days per month")
print ("****************************************************************")
input("\nPress ENTER to exit program")

