class parent:
    def func1(self):
        print("the function in the parent class")
class child1:
    def func2(self):
        print("this function is in child1 class")
class child2:
    def func3(self):
        print("the function is in child2 class")
class chilld3(parent,child1):
    def func4(self):
        print("the function is in child4 class")
obj=child1()
obj.func1()
obj.func2()


    
