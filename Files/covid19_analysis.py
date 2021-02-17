f=open("covid_19_india.csv")
dict={}
for line in f:
    w=line.rstrip("\n").split(",")
    #print(w)
    state=w[3]
    confirm_case=int(w[-1])
    dict[state]=confirm_case
    if state not in dict:
        dict[state]=confirm_case
    else:
        dict[state] = confirm_case


for k,v in dict.items():
    print(k,':----->',v)
w=max(dict,key=dict.get)
# print("Max confirmed cases reported in",max(dict,key=dict.get))
print("Max confirmed cases reported in",w,dict[w])