
# This part of the code imports the required features for Python
import re
ip = input("Enter IP address: ")
# Input is taken for IP address
# 
# This is then compared against a criteria to determine whether it is in #a valid format
valid = re.match("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]",ip)
# The code then checks to see whether the input met the criteria or not.
# The result is then printed for the user to see.
if valid:
   print("IP address OK")
else:
   print("IP address invalid")
