employees=[
    [100,'tom','developer',20000,1998,2000],
    [101,'john','developer',30000,1989,2000],
    [102,'tim','mean stack',40000,1997,2000],
    [102,'jims','hr',40000,1989,2000],
    [102,'tony','backend',40000,1995,2000]
]
# a=["EMP_NO","NAME","J.D","SALARY","JOIN.DT","RETD.DT"]
# print(a[0]," ",a[1]," ",a[2]," ",a[3]," ",a[4]," ",a[5])
diff=0
detail=0
for emp in employees:
    # print(diff)
    if(diff<(emp[5]-emp[4])):
        diff = emp[5] - emp[4]
        detail=emp
        continue
print(detail,"\nHe has got",diff,"of job experience.")
