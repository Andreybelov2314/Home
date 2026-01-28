def batch(obt, num):
    upd=[]
    obj=str(obt)
    for i in obj:
        if len(upd)==num:
            yield upd
            upd=[]
            upd.append(i)
        else:
            upd.append(i)
    yield upd
o=batch('asdsfagaf', 3)
print(list(o))
o2=batch(123424556, 2)
print(list(o2))