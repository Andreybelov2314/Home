#Базовый уровень
lambda_plus=lambda x,y:x+y
print(lambda_plus(1,2))
print('-=========-')
lst=[-5, 0, 3, 10]
lambda_pos=lambda x: True if x > 0 else False
print(list(filter(lambda_pos, lst)))
print('-=========-')
lst= [12, 45, 23, 67, 89, 34]
lambda_thrt=lambda x: True if x<30 else False
print(list(filter(lambda_thrt, lst)))
print('-=========-')
lst=["red", "green", "blue"]
lamda_uppper=lambda x: x.upper()
print(list(map(lamda_uppper, lst)))
print('-========-')
lst=[2, 5, 10, 15]
print(list(filter(lambda x:True if x%2==0 else False, lst)))
print('-========-')
lst=["apple", "banana", "cherry", "date", "fig"]
print(list(filter(lambda x: True if len(x)>5 else False, lst)))
print('-========-')
lst=[0, 10, 20, 30, 40]
print(list(map(lambda x: x*9/5+32, lst)))
print('-========-')
lst=["hello", "world", "python"]
print(list(map(lambda x:len(x), lst)))
print('-========-')
#Cредний уровень
lst=["hello", "world", "python"]
lambda_rev=lambda x:x[::-1]
print(list(map(lambda_rev, lst)))
print('-========-')
lst=[2,4,5,6]
lst2=[2,3,5,3]
print(list(map(lambda x, y:x**y, lst, lst2)))
print('-========-')
lst=[-5, 10, -3, 0, 7, -1, 15]
print(list(filter(lambda x: True if x>0 and x%5==0 else False, lst)))
print('-========-')
lst=["Python", "java", "C++", "JavaScript", "go", "Rust"]
print(list(filter(lambda x: True if x[0].isupper() and len(x)>3 else False, lst)))
print('-========-')
first=[(1, 2), (3, 4), (5, 6)]
print(list(map(lambda x:x[0]+x[1], first)))
print('-========-')
lst=[1,2,3,4,5]
print(list(map(lambda x: f'число: {x}', lst)))
print('-========-')

