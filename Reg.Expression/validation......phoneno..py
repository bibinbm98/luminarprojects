from re import *

rule = '(91)?[0-9]{10}'

variable_name = input("Enter the variablr to be check")

var = fullmatch(rule, variable_name)
if var != None:
    print("Valid variable Name")
else:
    print("OOPS! Invalid")

