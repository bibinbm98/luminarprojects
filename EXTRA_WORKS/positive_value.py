
def sub(num1, num2):
    if num1>num2:
        ren =num1 - num2
    else:
        swap=num1
        num1=num2
        num2=swap
        ren=num1-num2
    print(ren)

sub(15,20)