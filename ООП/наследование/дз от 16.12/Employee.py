from Person import *
class Employee(Person):
    def __init__(self,name,age,position):
        super().__init__(name,age)
        self.position=position
    def get_info(self):
        return f'name:{self.name}, {self.age} years old., position: {self.position}'

