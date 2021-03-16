from re import *


# pattern='a+'#chk for one or more a

# pattern='a*'#a+ + zero number of a

# pattern='a{2}'

pattern='a{2,3}'

matcher=finditer(pattern,'aaabbbaaacaaaqaa')
for match in matcher:
    print(match.start())
    print(match.group())
