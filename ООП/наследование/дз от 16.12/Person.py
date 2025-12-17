class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_info(self):
        return f'name:{self.name}, {self.age} years old.'

