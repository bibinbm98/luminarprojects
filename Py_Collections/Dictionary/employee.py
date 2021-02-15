#keys id,name, desig ,salry
#print employee name
#employee salary
#chk for gender key is there if not add gender key value pair
#iterate all key pairs


employee={'id':100,'name':"bibin",'desig':"developer",'salry':"40000"}

print("Employee Name is:",employee['name'])

print("Salary:",employee['salry'])

if "gender" in employee:
    print("gender exiist")
else:
    employee['gender']="male"
print(employee)

for k,v in employee.items():
    print(k,':',v)


employee[salry]+=25
print(employee['salry'])