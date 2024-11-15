'''the word polymorphism means many forms and in programming it refers to methods\functions\operastors
with the same name that can be executed on many objects or classes
POLYMORPHISM CAN ACHEIVE THROUGH METHOD OVERRIDING AND OPERATROR OVER LOADING


"method overiding":the function name which ewe declare in the super class is implemented by the subclass with the same function name
"operator overloading":with in the same class the funtion was implemented with the different parameters and same name
'''

class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def start(self):
        print("vehicle is starting")

class train(vehicle):
    def start(self):
        print("starting")

class bike(vehicle):
    def start(self):
        print("bike is starting")

bike1=bike("ktm","duke")
train1=train("WAP-5","JANMABHUMI")

print(bike1.model)
for x in (train1,bike1):
    print(x.brand)
    print(x.model)
    x.start()
