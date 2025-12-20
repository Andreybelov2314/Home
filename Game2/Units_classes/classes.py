class Units:
    unit=''
    attack=0
    defend=0
    vision=0
    speed=0
    def __init__(self, unit, attack, defend, vision, speed):
        self.unit=unit
        self.attack=attack
        self.defend=defend
        self.vision=vision
        self.speed=speed

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, value):
        self.__unit = value

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        self.__attack = value

    @property
    def defend(self):
        return self.__defend

    @defend.setter
    def defend(self, value):
        self.__defend = value

    @property
    def vision(self):
        return self.__vision

    @vision.setter
    def vision(self, value):
        self.__vision = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value