class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id=id
    def calculate_salary(self):
        return 0
    def get_info(self):
        return f'name: {self.name}, id: {self.id} salary: {self.calculate_salary()}'