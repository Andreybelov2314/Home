class worker():
    def __init__(self,example):
        self.__example=example
    @property
    def exs(self):
        return self.__example

    @exs.setter
    def exs(self, value):
        self.__example=value

    def complete(self):
        start = 0
        num=''
        signs='+-*/'
        sign=''
        for i in self.exs:
            if i not in signs:
                num+=i
            else:
                start+=int(num)
                num=''
                sign=i
        if sign=='+':
            res=start+int(num)
        elif sign=='-':
            res=start-int(num)
        elif sign=='*':
            res=start*int(num)
        elif sign=='/':
            res=start/int(num)
        return f'{self.exs}={res}'

