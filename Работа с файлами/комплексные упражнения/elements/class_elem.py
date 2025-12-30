class elements():
    def __init__(self, number, name, title, mass):
        self.number = number
        self.name = name
        self.title = title
        self.mass = mass
    @property
    def element_name(self):
        return self.name

    @element_name.setter
    def element_name(self, value):
        self.name = value
    @property
    def element_title(self):
        return self.title

    @element_title.setter
    def element_title(self, value):
        self.title = value
    @property
    def element_mass(self):
        return self.mass
    @property
    def element_number(self):
        return self.number

    @element_number.setter
    def element_number(self, value):
        self.number = value

    @element_mass.setter
    def element_mass(self, value):
        self.mass = value
    def get_info(self):
        return f'{self.element_number}-{self.element_name}:{self.element_title}-{self.element_mass}'
