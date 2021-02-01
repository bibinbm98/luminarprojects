i = 1
n = int(input("Enter the Limit to be sum:"))
ototal = 0
etotal = 0
while i <= n:
    if i % 2 == 0:
        etotal = etotal + i
    else:
        ototal = ototal + i

    i += 1
print("Total of Even No.s:", etotal)
print("Total of Odd No.s:", ototal)
