maximum=lambda lst:  (min(lst), max(lst), sum(lst)/len(lst))
lst=[1,2,3,4,5,8,-1]
print(maximum(lst))
vowels=['a','e','i','o','u',]
text='asjdfauewygd'
vow=filter(lambda x: True if x in vowels else False, text)
print(list(vow))
print(list(filter(lambda x: True if x not in vowels else False, text)))
students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
    {"name": "Bob", "age": 22, "grades": [70, 65, 80]},
    {"name": "Charlie", "age": 19, "grades": [95, 88, 92]},
    {"name": "David", "age": 21, "grades": [60, 72, 68]}
]
middle=list(filter(lambda student: True if sum(student['grades'])/len(student['grades']) > 75 else False, students))
print(middle)
