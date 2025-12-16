from зоопарк import zoo
class cats(zoo):
    def __init__(self,fam,name):
        super().__init__('', '','')
        self.cl='cats'
        self.fam=fam
        self.name = name
    def sound(self):
        return 'Roar'
    def eating(self):
        return 'all other animals'

obj1=cats('tiger', 'Leo')
print(obj1.passport())
print(obj1.eating())
print(obj1.sound())
