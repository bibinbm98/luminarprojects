employees=[
    [100, 'bibin', 'developer',60],
    [101, 'tom', 'developer',25],
    [102, 'john', 'manager',40],
    [103, "tim", "bd", 40],
    [104, 'jims', 'developer',20]
]
total=0
for emp in employees:
    total = total + emp[3]
print("hih",total)



dtotal=0
for emp in employees:
    if (emp[2]=='developer'):
        dtotal = dtotal + emp[3]
print("dtotal",dtotal)




sallist=[]
for emp in employees:
    sallist.append(emp[3])
print("high sal=",max(sallist))


