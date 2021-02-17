f=open("covid_19_india.csv")
dict={}
for line in f:
    w=line.rstrip("\n").split(",")
    state = w[3]
    cure=w[-3]
    death=w[-2]
    confirm_case = w[-1]
    dict[state]={"state":state,"confirm_case":confirm_case,"cure":cure,"death":death}
print(dict)
