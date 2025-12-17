from Employee import *
class Manager(Employee):

    def __init__(self,name,age, position):
        super().__init__(name,age, position)
        self.team=[]

    def add_team(self, new_emp):
        self.team.append(new_emp)
    def get_info(self):
        return f'name:{self.name}, {self.age} years old., position: {self.position}, team: {self.team}'
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_position(self):
        return self.position
