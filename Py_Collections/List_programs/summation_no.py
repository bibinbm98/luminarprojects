num = [2, 4, 6]
print("Input value is :")
for i in range(len(num)):
    print(num[i], end=" ")
print(" ")
sum = 0
for n in num:
    sum += n
print("sum is ", sum)
print("Output is :")
for n in num:
    out = sum - n
    print(out, end="  ")
