

out=open("demo","r")
lst=list()
for i in out:
    lst.append(i.rstrip("\n"))  # TO REMOVE \n from file
print(lst)

l=set(lst)   #set to remove duplicate from list
print(l)


