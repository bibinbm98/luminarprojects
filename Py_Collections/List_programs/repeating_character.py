pattern="ABcDD"
flg=0
for char in pattern:
    if pattern.count(char)>1:
        flg=1
        print(char)
        break
