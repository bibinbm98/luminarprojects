i=int(input("enter NUmber"))
sum=0
while(i!=0):
    dig=i%10
    print(dig,end="^3 ")
    cube=dig**3
    sum=sum+cube
    i=i//10
print("\n")
print("sum is =",sum)

