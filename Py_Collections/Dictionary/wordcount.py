text="hello hello hi hello hi hi hi hi hello yr"
words=text.split(" ")
print(text)
dict={}
for i in words:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
print(dict)
#print(max(dict)) #by key value
#print(dict.get("hello"))#get the valye
print(max(dict,key=dict.get))
data=sorted(dict,key=dict.get,reverse=True)
print(data)


pattern="ABAACC"  #first recursive character
dict={}
for char in pattern:
    if char not in dict:
        dict[char]=1
    else:
        print("first recusive char:",char)
        break
# print(dict)