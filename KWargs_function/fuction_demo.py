def add(*args):
    total=0
    print(args)
    for num in args:
        total+=num
    print(total)
add(10,20,30,40,50)


def print_emp_data(**args):
    print(args)
    for k,v in args.items():
        print(k,v)


print_emp_data(eid=100,job='kakkanad',resid='allapey')

