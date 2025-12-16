from Employee import *
class ComisionEmployee(Employee):
    def __init__(self, name, id,sales, comission):
        super().__init__(name, id)
        self.sales = sales
        self.comission = comission
    def calculate_salary(self):
        return int(self.sales) * float(self.comission)


obj1=ComisionEmployee('Ivan', 1257645, '1200000', '0.10')
print(obj1.get_info())


