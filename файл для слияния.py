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

print('-=======-')
def str_info(str):
    result= {}
    count1=0
    for i in str:
        if i=='.' or i=='!' or i=='?':
            count1=count1+1
    a1={'количество предложений':count1}
    result.update(a1)
    count2=len(str.split())
    a2={'количество слов':count2}
    result.update(a2)
    count3=0
    for i in str.split():
        if i.isalpha():
            count3+=int(len(i))
    count4=count3/count2
    a3={'средняя длина слова':count4}
    result.update(a3)
    return result
str="В 2023 году было продано 1500 iPhone 14 Pro и 2000 Samsung Galaxy S23. Цены варьировались от 79990 до 129990 рублей. Клиенты оставили 4.5 звезд из 5!"
print(str_info(str))

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
alg=input("введите пример")
print(arif(alg))

print('-=====-')

print('-=============-')
def code(x, str):
    lst1=[]
    update=''
    result=''
    for i in str:
        if len(update)<len(x):
            if i.isalpha():
                update+=i
            else:
                pass
        elif len(update)==len(x):
            lst1.append(update)
            update=i
    if update not in lst1:
        if len(update)==len(x):
            lst1.append(update)
        else:
            while len(update)!=len(x):
                update+='_'
            lst1.append(update)
    quanity=0
    for i in lst1:
        quanity+=1
        if quanity%len(x)==0:
            result+=' '
        result+=''.join(sorted(i))
    return result

text='Andrey'
keyword='lam'
print(code(keyword,text))
print('-============')
















