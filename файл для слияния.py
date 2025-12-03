maximum=lambda lst:  (min(lst), max(lst), sum(lst)/len(lst))
lst=[1,2,3,4,5,8,-1]
print(maximum(lst))
vowels=['a','e','i','o','u',]
text='asjdfauewygd'
vow=filter(lambda x: True if x in vowels else False, text)
print(list(vow))
print(list(filter(lambda x: True if x not in vowels else False, text)))
