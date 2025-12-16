class zoo():
    cl=''
    fam=''
    name=''
    def __init__(self,cl, fam, name):
        self.cl=cl
        self.fam=fam
        self.name = name
    def passport(self):
        return f'{self.cl},{self.fam}, {self.name}'
    def eating(self):
        return None
    def sound(self):
        return None