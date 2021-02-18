employee = {
    1000: {"eid": 1000, "ename": 'BIBIN', "desig": 'developer', "salary": 30000},
    1001: {"eid": 1001, "ename": 'FEBIN', "desig": 'CEO', "salary": 60000},
    1002: {"eid": 1002, "ename": 'JIBIN', "desig": 'B.E.D', "salary": 56000},
    1003: {"eid": 1003, "ename": 'JIMMY', "desig": 'HR', "salary": 25000}
}
def details(**kwargs):
    id = kwargs["eid"]
    if id in employee:
        print(employee[id]["ename"])
        if property in kwargs:
            pro = kwargs["property"]
            print(employee[id][pro])
    else:
        print("id dont exist")
id = int(input("ENTER THE EMPLOYEE ID:"))
property = input("ENTER THE DETAILS TO BE SEARCHED:").lower()
details(eid=id, property=property)
