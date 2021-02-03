num=int(input("enter the no to be checked:"))
flg=0
for i in range (2,num):
    if(num%i==0):
        flg=1
        break
    else:
        flg=0
if(flg==0):
    print(num,"is Prime no.")
else:
    print(num,"is not a Prime no.")
