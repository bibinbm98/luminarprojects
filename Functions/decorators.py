# def my_div(fun):
#     def inner(num1,num2):
#         if num1<num2:
#             num1,num2=num2,num1
#         return fun(num1,num2)
#     return inner
#
# @my_div
# def div(num1,num2):
#     return (num1/num2)
# print(div(2,4))



def dec(fun):
    def inner_func(phno):
        if len(phno)<10:
            raise Exception("invalid phnone number")
        else:
            return fun(phno)
    return inner_func
@dec
def valphno(phno):
    return "valid "+phno
print(valphno("23341234"))

