'''when an unwanted event occurs which stops the normal flow of the program which we can handle an exception
try: a try block will handle the exception which occurs
else: the else block lets you execute code when there is no error
finally: the finally block execute code whether the result of try and except block executed or not



try:
    expression
except:
    expression
else:
    expression
finally:
    expression
'''

try:
    number=int(input("enter a positive value"))
    if number<0:
        raise ValueError("enter the positive value")
    print(number)
except ValueError as e:
    print("error",e)
