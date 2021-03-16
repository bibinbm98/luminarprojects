from re import *
# pattern="[abc]"
# source="ababavjg&^%$bab"
pattern="[A-Z]"
source="ababavjgDF&^%$bab"

matcher=finditer(pattern,source)
for match in matcher:
    print(match.start())
    print(match.group())