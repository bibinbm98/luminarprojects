arr = [10, 11, 12, 13, 14, 15, 16]
elem = int(input("Enter the element to be found:"))
flg = 0
for num in arr:
    if elem == arr:
        flg = 1
        break
    else:
        flg = 0

if flg == 1:
    print("element  found")
else:
    print("element not found")
