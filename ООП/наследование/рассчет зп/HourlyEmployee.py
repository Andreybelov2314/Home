from Employee import *
class hourlyEmployee(Employee):
    def __init__(self, name, id, hours, h_rate):
        super().__init__(name, id)
        self.hours = hours
        self.name=name
        self.id=id
        self.h_rate=h_rate
    def calculate_salary(self):
        return int(self.hours) * int(self.h_rate)
obj1=hourlyEmployee('john', 1257645, '120', '12')
print(obj1.get_info())


