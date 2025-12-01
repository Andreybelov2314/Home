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
