# try:
#     doubtful codes

# except:
#     handling code
# finally:
#     cleanup processing code



# no1=int(input("enter no1..."))
# no2=int(input("enter no2..."))
#
# try:
#     res=no1/no2
#     print(res)
#
# except Exception as e:
#     no2 = int(input("enter no2..."))
#     res=no1/no2
#     print(res)
#
# finally:
#     print("database")
#     print("file write")
#
#
no=int(input("no:"))
try:
    if no<=0:
        raise Exception("invalid no:")    #user customise exception.......\
    else:
        print(no)
except Exception as e:
    print(e.args)
