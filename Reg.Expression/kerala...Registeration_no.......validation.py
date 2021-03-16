
from re import *

rule = 'KL\s\d{2}\s[A-Z]{2}\s[0-9]{4}'
f = open("vechile...no.s")
lst=[]
for regno in f:
    regno=regno.rstrip("\n")
    var = fullmatch(rule, regno)
    if var != None:
       lst.append(regno)
print(lst)
