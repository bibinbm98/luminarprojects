lst1 = [10, 11, 12, 13,77,66]
lst2 = [10, 12, 13, 77,11]
# for i in lst1:
#     for j in lst2:
#         if i == j:
#             print(i, j)
#             break
#complexity reduce
pos1=0
pos2=0
while((pos1<=len(lst1))&(pos2<=len(lst2))):
    if (lst1[pos1]==lst2[pos2]):
        print(lst1[pos1])
        pos1+=1
        pos2+=1
    elif(lst1[pos1]>=lst2[pos2]):
        pos2+=1
    else:
        pos1+=1
