import copy
import random#создаем начало игры. Рандомная строка+пустая строка
update=[]
total=[]
elements=['a','b','c']
while len(update)!=5:
    update.append(random.choice(elements))
total.append(update)
total.append(['_','_','_','_', '_'])
def new_elem(total):#функция для добавления элемента
    new=random.choice(elements)
    for i in total:
        print(i)
    print(new)
    dec=int(input('введите номер клетки(1-5), на которую хотите поставить элемент'))
    total1=total.copy()
    total1[-1][dec-1]=new
    return total1
def horisontale(total):
    total_last=total[-1]
    if total_last[0]==total_last[1] and total_last[1]==total_last[2]:
        total_last[0:3]='_','_','_'
    if total_last[1]==total_last[2] and total_last[2]==total_last[3]:
        total_last[1:4]='_','_','_'
    if total_last[2]==total_last[3] and total_last[3]==total_last[4]:
        total_last[2:5]='_','_','_'
    total[-1]=total_last
    return total
game1=[['a','a','c','c','b'],['a','a','b','c','b'],['a','a','c','c','c']]
horis=horisontale(game1)
print(horis)
def verticale(total):
    if len(total)<3:
        return total
    else:
        for index in range(len(total[-1])):
            if (total[-1][index] == total[-2][index] == total[-3][index]):
                total[-1][index] = '_'
                total[-2][index] = '_'
                total[-3][index] = '_'
        return total
game2=[['a','a','c','c','b'],['a','a','b','c','b'],['a','a','c','c','c']]
vert=verticale(game2)
print(vert)
def five_or_zero(total):
    total1=total.copy()
    if '_' not in total1[-1]:
        new=['_','_','_','_','_']
        total1.append(new)
    if total1[-1]==['_','_','_','_','_']:
        if '_' in total1[-2]:
            total1.pop()
    return total1
def three_in_row(verticale, horisontale):
    total1=[]
    update=[]
    index=0
    for i in verticale:
        now_str=horisontale[index]
        update.append(i[0]) if i[0]==now_str[0] else update.append('_')
        update.append(i[1]) if i[1]==now_str[1] else update.append('_')
        update.append(i[2]) if i[2]==now_str[2] else update.append('_')
        update.append(i[3]) if i[3]==now_str[3] else update.append('_')
        update.append(i[4]) if i[4]==now_str[4] else update.append('_')
        total1.append(update)
        index+=0
        update=[]
    return total1

