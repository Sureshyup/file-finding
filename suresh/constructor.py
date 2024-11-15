class person:
    def run(self):
        print("running")

class childclass(person):
    def eat(self):
        print("eating")
obj=childclass()
obj.run()
obj.eat()
