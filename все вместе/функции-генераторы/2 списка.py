import random
def symb():
    for i in range(5):
        lst=['/','+','-','=']
        upd=random.choice(lst)
        yield upd
def num():
    for i in range(5):
        lst=[1,2,3,4,5]
        upd=random.choice(lst)
        yield upd
s=symb()
print(list(s))
n=num()
print(list(n))