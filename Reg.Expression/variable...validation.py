from re import *

rule = '[a-k A-K][3 6 9][A-Z a-z 0-9]*'

variable_name=input("Enter the variablr to be check")

var=fullmatch(rule,variable_name)
if var!=None:
    print("Valid variable Name")
else:
    print("OOPS! Invalid")

