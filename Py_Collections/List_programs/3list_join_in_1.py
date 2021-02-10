lists=[
    [10,20,30,40],
    [50,60,70,80],
    [90,100,101,102]
]
new_list=[]
for list1 in lists:
    for list2 in list1:
        new_list.append(list2)
print(new_list)
