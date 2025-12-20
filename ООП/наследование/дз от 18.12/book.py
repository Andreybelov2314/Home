#Реализуйте класс «Книга». Необходимо хранить в
#полях класса: название книги, год выпуска, издателя,
#жанр, автора, цену. Реализуйте методы класса для ввода
#данных, вывода данных, реализуйте доступ к отдельным
#полям через методы класса.
class book:
    def __init__(self, name, year, publisher, genre, autor, price):
        self.name_book = name
        self.year_writted = year
        self.publisher_company = publisher
        self.genre_type = genre
        self.autor_name= autor
        self.price = price
    @property
    def name(self):
        return self.name_book

    @name.setter
    def name(self, value):
        self.name_book = value
    @property
    def year(self):
        return self.year_writted

    @year.setter
    def year(self, value):
        self.year_writted = value
    @property
    def publisher(self):
        return self.publisher_company

    @publisher.setter
    def publisher(self, value):
        self.publisher_company = value
    @property
    def genre(self):
        return self.genre_type

    @genre.setter
    def genre(self, value):
        self.genre_type = value
    @property
    def autor(self):
        return self.autor_name

    @autor.setter
    def autor(self, value):
        self.autor_name = value
    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        self.price = value
    def __str__(self):
        return f'{self.autor}-{self.name}, {self.year}, {self.publisher}, {self.genre}, {self.price}'
