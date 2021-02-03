num=int(input("enter the number:"))
flg=0
for i in range(20,30):
    if(num==i):
        flg=1
        break                                 #1 way
    else:
        flg=0
if(flg==0):
    print(" is not range ")
else:
    print("is in the range")

#---------------------------
# num=20
# if(num>20)&(num<30):
#     print("true")                       #2 way
# else:
#     print("true")
#
# #-------------------------------
# if num in range(20,30):
#     print("true")
# else:                                     #3 way
#     print("false")
