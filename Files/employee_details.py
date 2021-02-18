employee={
    1000:{"eid":1000,"ename":'BIBIN',"desig":'developer',"salary":30000},
    1001:{"eid":1001,"ename":'FEBIN',"desig":'CEO',"salary":60000},
    1002:{"eid":1002,"ename":'jibin',"desig":'B.E.D',"salary":56000},
    1003:{"eid":1003,"ename":'jimmy',"desig":'HR',"salary":25000}
}
id=int(input("ENTER THE EMPLOYEE ID:"))
property=input("ENTER THE DETAILS TO BE SEARCHED:").lower()
# property.lower()
if id in employee:
    print("NAME OF EMPLOYEE :",employee[id]["ename"])
    if property in employee[id]:
        print(property,':',employee[id][property])
    else:
        print("INVALID PROPERTY!")
else:
    print("INVALID ID!")



