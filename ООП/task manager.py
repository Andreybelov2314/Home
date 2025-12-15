
from task import *




obj1=task_manager()
obj1.tasks=[]
obj1.command()
obj2=Task()
obj2.title='сделать дз'
obj2.task_status()
obj2.task_dct()
print(obj2.dct_title)
obj3=Task()
obj3.title='поспать'
obj3.task_dct()
print(Task.all_tasks)

vector1=Vector2D(5,7)
vector2=Vector2D(3,8)
print(vector1+vector2)
print(vector1-vector2)
print(vector1.length())

