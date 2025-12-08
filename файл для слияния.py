maximum=lambda lst:  (min(lst), max(lst), sum(lst)/len(lst))
lst=[1,2,3,4,5,8,-1]
print(maximum(lst))
vowels=['a','e','i','o','u',]
text='asjdfauewygd'
vow=filter(lambda x: True if x in vowels else False, text)
print(list(vow))
print(list(filter(lambda x: True if x not in vowels else False, text)))

print('-=======-')
lst=["radar", "hello", "level", "world", "mam"]
lamda_palindrome=filter(lambda x: True if x[::-1] == x[::1] and len(x)>3 else False, lst)
print(list(lamda_palindrome))

students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
    {"name": "Bob", "age": 22, "grades": [70, 65, 80]},
    {"name": "Charlie", "age": 19, "grades": [95, 88, 92]},
    {"name": "David", "age": 21, "grades": [60, 72, 68]}
]
middle=list(filter(lambda student: True if sum(student['grades'])/len(student['grades']) > 75 else False, students))
print(middle)
print("-============-")
def arif(x):
    lst=[]
    signs='+-*/'
    num=''
    for i in x:
        if i not in signs:
            num+=i
        elif i in signs:
            lst.append(num)
            num=i
    if num not in lst:
        lst.append(num)
    result=int(lst[0])
    for l in lst[1:]:
        if l[0]=='+':
            result+=int(l[1:])
        elif l[0]=='-':
            result-=int(l[1:])
        elif l[0]=='*':
            result=result*int(l[1:])
        elif l[0]=='/':
            result=result/int(l[1:])
    return result
#alg=input("введите пример")
#print(arif(alg))
print('-=====-')
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
print(new_elem(total))
#def three_in_row(total):
def horisontale(total):
    if total[0]==total[1] and total[1]==total[2]:
        total[0:3]='_','_','_'
    if total[1]==total[2] and total[2]==total[3]:
        total[1:4]='_','_','_'
    if total[2]==total[3] and total[3]==total[4]:
        total[2:5]='_','_','_'
    return total
def verticale(total):
    if len(total)<3:
        return total
    else:
        for index in range(len(total[-1])):  # Итерируем по индексам
            if (total[-1][index] == total[-2][index] == total[-3][index]):
                total[-1][index] = '_'
                total[-2][index] = '_'
                total[-3][index] = '_'
        return total
