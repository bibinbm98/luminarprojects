lst=[2,3,4,5]
# num=int(input("enter the element"))
# for i in lst:
#     for j in lst:
#         if(i+j==num):
#             print(i,j)


low=0
num=6
upp=len(lst)-1
cnt=0
while(low<=upp):
    cnt+=1
    total=lst[low]+lst[upp]
    if num==total:
        print(lst[low],lst[upp])
        low+=1
        upp-=1
    elif total>num:
        upp-=1
    elif total<num:
        low+=1


print(cnt)