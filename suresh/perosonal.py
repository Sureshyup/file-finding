class person:
    def person_details(self,**kwargs):
        if "name" in kwargs and "age" in kwargs:
            print(f"name is: {kwargs['name']},age is: {kwargs['age']}")
        elif "name" in kwargs:
            print(f"name is: {kwargs['name']}")
        else:
            print(f"name is: {kwargs['age']}")
p=person()
p.person_details(name="suresh",age=20)
p.person_details(name="suresh")
p.person_details(age=20)


            
    
