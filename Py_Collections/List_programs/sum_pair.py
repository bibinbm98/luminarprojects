lst=[2,3,4,5,6]
num=int(input("enter the element"))
for i in lst:
    for j in lst:
        if(i+j==num)&(i!=j)&(i<j):
            print(i,j)
