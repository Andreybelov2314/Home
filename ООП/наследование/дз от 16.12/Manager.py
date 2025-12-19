from Employee import *
class Manager(Employee):

    def __init__(self,name,age, position):
        super().__init__(name,age, position)
        self.team=''

    def add_team(self, new_emp):
        self.team+=new_emp
    def get_info(self):
        return f'name:{self.name}, {self.age} years old., position: {self.position}, team: {self.team}'
    @property
    def name_m(self):
        return self.name

    @name_m.setter
    def name_m(self, value):
        pass
    @property
    def team_m(self):
        return self.team

    @team_m.setter
    def team_m(self, value):
        pass