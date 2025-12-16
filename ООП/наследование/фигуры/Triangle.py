from ООП.наследование.фигуры.figure import *
class Triangle(figure):
    def __init__(self, a, b, c, h):
        self.a=a
        self.b=b
        self.c=c
        super().__init__(3,4,3)
        self.hight=h
    def __str__(self):
        return f'Triangle({self.a},{self.b},{self.c}, {self.hight})'
    def __area__(self):
        area=(int(self.a)*int(self.hight))/2
        return area

obj=Triangle(2,6,5,3)
print(obj.__area__())
