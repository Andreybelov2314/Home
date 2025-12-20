from .classes import *
class frigate(Units):
    def __init__(self, name, unit="frigate", attack=15, defend=5, vision=5, speed=2 ):
        super().__init__(unit, attack, defend, vision, speed)
        self.__unit_val = unit
        self.__attack_val = attack
        self.__speed_val = speed
        self.name_val = name
        self.vision_val = vision
        self.defend_val = defend
        self.field_index_val = None

    @property
    def name(self):
        return self.name_val

    @name.setter
    def name(self, value):
        self.name_val = value
    @property
    def unit(self):
        return self.__unit_val
    @unit.setter
    def unit(self, value):
        self.__unit_val = value
    @property
    def attack(self):
        return self.__attack_val

    @attack.setter
    def attack(self, value):
        self.__attack_val=value
    @property
    def defend(self):
        return self.defend_val

    @defend.setter
    def defend(self, value):
        self.defend_val = value
    @property
    def vision(self):
        return self.vision_val

    @vision.setter
    def vision(self, value):
        self.vision_val = value
    @property
    def speed(self):
        return self.__speed_val

    @speed.setter
    def speed(self, value):
        self.__speed_val = value
    @property
    def index(self):
        return self.field_index_val


    @index.setter
    def index(self, value):
        self.field_index_val = value