from re import *

rule = '(3[01]|[12][0-9]|0?[1-9])[/.-](1[0-2]|0?[1-9])[/.-](?:[0-9]{2})?[0-9]{2}'

variable_name = input("Enter the DATE OF BIRTH to be check")

var = fullmatch(rule, variable_name)
if var != None:
    print("Valid DATE OF BIRTH",variable_name)
else:
    print("OOPS! Invalid DATE OF BIRTH")

