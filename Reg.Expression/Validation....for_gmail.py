from re import *

rule = '[a-z A-Z]+[0-9]*@gmail.com'

variable_name = input("Enter the variablr to be check")

var = fullmatch(rule, variable_name)
if var != None:
    print("Valid GMAIL ID")
else:
    print("OOPS! Invalid")

