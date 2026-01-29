import random
from classes import *
def worker(nm,txt):
    db=database(nm,txt)
    txt_upd=['a','b','c','d','e',3]
    nm_upd=['a',1,2,3,4,5,6]
    versions=[]
    for i in range(10):
        ver_upd=database(db.number,db.data)
        versions.append(ver_upd)
        try:
            upd1=random.choice(txt_upd)
            upd2=random.choice(nm_upd)
            db.data+=upd1
            db.number+=upd2
        except ValueError:
            print('возникла ошибка при попытке обновить')
        except TypeError:
            print('возникла ошибка при попытке обновить')
    for i in versions:
        print(str(i))
        print()
worker(1,'l')