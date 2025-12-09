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
