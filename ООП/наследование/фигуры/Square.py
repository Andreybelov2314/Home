from ООП.наследование.фигуры.figure import figure


class circle(figure):
    def __init__(self,radius,center):
        self.radius=radius
        super().__init__(5,3,(2,5))
        self.center=center
    def __str__(self):
        return f'{self.radius},{self.center}'

obj=circle(2,center=(1,1))
print(str(obj))
