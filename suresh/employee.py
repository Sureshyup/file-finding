class employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
        self.salary=0

    def set_salary(self,salary):
        if salary>0:
            self.salary=salary
        else:
            print("invalid salary")

    def get_salary(self):
        return self.salary
