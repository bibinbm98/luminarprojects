ft=open("teams","r")
fd=open("drop","r")
def get_team_set(f):
    st=set()
    for lines in f:
        st.add(lines.rstrip("\n"))
    return st
st1=get_team_set(ft)
st2=get_team_set(fd)




# ft=open("teams","r")
# st1=set()
# for i in ft:
#     st1.add(i.rstrip("\n"))  # TO REMOVE \n from file
# print(st1)
#
#
# fd=open("drop","r")
# st2=set()
# for j in fd:
#     st2.add(j.strip("\n"))
# print(st2)


qa=st1-st2
print(qa)