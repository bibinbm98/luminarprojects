st = open("words", "r")
w = []
dict={}
for word in st:
    w = word.rstrip("\n").split(" ")
    for i in w:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
# print(dict)
for k,v in dict.items():
    print(k,':',v)
