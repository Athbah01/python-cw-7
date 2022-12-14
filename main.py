
class Person:
#    name= "athba"
#    age=21

    def __init__(self,name,age):
        self.name= name
        self.age=age
    
    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old '

    def is_adult(self):
        if self.age>=18:
            print(f'you have too much responsibilities')
        else:
            print(f'lucky you')
   
   

first_person=Person('athba',21)
print(first_person.name)
print(first_person.age)
first_person.is_adult()
print(first_person)
