add=lambda a,b:a+b
print(add(3,5))

def myfunc(n):
    return lambda a:a*n
my=(myfunc(2))
print(my(3))


max_value=lambda x,y: x if x>y else y
print(max_value(3,7))


tax=lambda salary:salary*20/100
salary=int(input("enter the salary"))
print(tax(salary))


doublenum=lambda x: x*2
x=int(input("a:"))
print(doublenum(x))
