class stadium:
    def __init__(self, name, date, country, city, capacity):
        self.name_val = name
        self.date_val = date
        self.country_val = country
        self.city_val = city
        self.capacity_val = capacity
    @property
    def name(self):
        return self.name_val

    @name.setter
    def name(self, value):
        self.name_val = value
    @property
    def date(self):
        return self.date_val

    @date.setter
    def date(self, value):
        self.date_val = value
    @property
    def country(self):
        return self.country_val

    @country.setter
    def country(self, value):
        self.country_val = value
    @property
    def city(self):
        return self.city_val

    @city.setter
    def city(self, value):
        self.city_val = value
    @property
    def capacity(self):
        return self.capacity_val

    @capacity.setter
    def capacity(self, value):
        self.capacity_val = value
    def __str__(self):
        return f'{self.name}, {self.date}, {self.country}, {self.city}, {self.capacity}'
