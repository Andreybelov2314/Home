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
def five_or_zero(total):
    total1=total.copy()
    if '_' not in total1[-1]:
        new=['_','_','_','_','_']
        total1.append(new)
    if total1[-1]==['_','_','_','_','_']:
        if '_' in total1[-2]:
            total1.pop()
    return total1
def three_in_row(total):
    total1=horisontale(total.copy())
    total2=verticale(total.copy())
    total3=[]
    index=0
    for i in total1:
        if total1.count('_')==total2[index].count('_') or total1.count('_')>total2[index].count('_'):
            total3.append(i)
        elif total1.count('_')<total2[index].count('_'):
            total3.append(total2[index])
        index+=1
    return total3
game=[['a','a','b','c','c'], ['a','a','b','c','c'],['a','b','c','c','c']]
print(three_in_row(game))