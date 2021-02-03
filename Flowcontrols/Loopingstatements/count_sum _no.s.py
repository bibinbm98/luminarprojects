num = int(input("enter the number"))
sum = 0
pattern = ""
for i in range(1, (num + 1)):
    pattern = str(num) * i
    print(pattern,end=" ")
    sum = sum + int(pattern)  # sum+=int pattern
print("\nsum is", sum)
