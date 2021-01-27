# swapping of two numbers

# using temp

num1 = 10
num2 = 20
temp = num1
num1 = num2
num2 = temp
print(num1)
print(num2)
# *****************************************

# without using temp
num1 = 10
num2 = 20
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("num1=", num1, "num2=", num2)
