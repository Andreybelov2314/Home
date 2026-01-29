class database():
    def __init__(self,num, text):
        self.__num = num
        self.__text = text
    def __str__(self):
        return f'номер-{self.__num}, текст-{self.__text}'
    @property
    def number(self):
        return self.__num

    @number.setter
    def number(self, value):
        self.__num = value
    @property
    def data(self):
        return self.__text

    @data.setter
    def data(self, value):
        self.__text = value

