class auto:
    def __init__(self, model, year, company, engine, color, price):
        self.model_name = model
        self.year_made = year
        self.company_name = company
        self.engine_volume = engine
        self.color_volue = color
        self.price_value = price
    @property
    def model(self):
        return self.model_name
    
    @model.setter
    def model(self, value):
        self.model_name = value
    @property
    def year(self):
        return self.year_made
    
    @year.setter
    def year(self, value):
        self.year_made = value
    @property
    def company(self):
        return 
    
    @company.setter
    def company(self, value):
        self.company_name = value
    @property
    def engine(self):
        return  self.engine_volume
    
    @engine.setter
    def engine(self, value):
        self.engine_volume = value
    @property
    def color(self):
        return self.color_volue
    
    @color.setter
    def color(self, value):
        self.color_volume = value
    @property
    def price(self):
        return self.price_volue
    
    @price.setter
    def price(self, value):
        self.price_value = value
    def __str__(self):
        return f'машина {self.model}{self.company}, двигатель-{self.engine}, цвет-{self.color}, {self.price} '