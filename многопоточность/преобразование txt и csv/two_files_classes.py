import csv
import threading
import time
class work_txt():
    def __init__(self, name, age, city):
        self.__name=name
        self.__age=age
        self.__city=city
    @property
    def give_name(self):
        return self.__name
    
    @give_name.setter
    def give_name(self, value):
        self.__name=value
    @property
    def birthday(self):
        return self.__age
    
    @birthday.setter
    def birthday(self, value):
        self.__age=value
    @property
    def home(self):
        return self.__city

    @home.setter
    def home(self, value):
        self.__city=value
class work_csv():
    def __init__(self, name,department,salary):
        self.__name=name
        self.__department=department
        self.__salary=salary
    @property
    def nm(self):
        return self.__name

    @nm.setter
    def nm(self, value):
        self.__name=value
    @property
    def work(self):
        return self.__department

    @work.setter
    def work(self, value):
        self.__department=value
    @property
    def sal_info(self):
        return self.__salary

    @sal_info.setter
    def sal_info(self, value):
        self.__salary=value


