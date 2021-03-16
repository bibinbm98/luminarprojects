from re import *
pattern="ab"
source="ababababababbbbabab"

match=finditer(pattern,source)
cnt=0
for mat in match:
    print(mat.start())
    print(mat.group())
    cnt+=1
print("count",cnt)
