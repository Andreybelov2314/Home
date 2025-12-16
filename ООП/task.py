class Task:
    """класс для работы с задачами:просмотра и изменения статуса заадч"""
    'поля'
    title=''
    status='не завершена'
    dct_title={}
    all_tasks=[]
    def task_status(self):
        self.status='завершена'
        return self.status
    def task_dct(self):
        self.dct_title={self.title:self.status}
        Task.all_tasks.append(self.dct_title)


class task_manager():
    """менеджер по работе с задачами"""
    tasks=[{'сделать дз': 'завершена'}, {'поспать': 'не завершена'}]
    def add_task(self):
        task=input('введите название задачи')
        self.tasks.append({task:'не завершена'})
        print(f'задача {task} успешно добавлена')
    def mark_task_done(self):
        task=input('введите название задачи')
        for i in self.tasks:
            index=self.tasks.index(i)
            if i.keys() == task:
                self.tasks[index]={task:'выполнено'}
        print(f'задача {task} отмечена как выполненная')
    def show_tasks(self):
        print(self.tasks)
    def save_to_file(self):
        task_manager.tasks=self.tasks
        print('файл с списком задач успешно обновлен')
    def load_from_file(self):
        self.tasks=task_manager.tasks
        print('список задач успешно загружен')
    def command(self):
        while True:
            command=input('введите команду:1-add, 2-done, 3-show, 4-load, 5-exit  ')
            if command=='1':
                self.add_task()
            elif command=='2':
                self.mark_task_done()
            elif command=='3':
                self.show_tasks()
            elif command=='4':
                self.load_from_file()
            elif command=='5':
                self.save_to_file()
                break
class Vector2D():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector2D(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector2D(self.x-other.x,self.y-other.y)
    def __str__(self):
        return f'(Vector({self.x},{self.y}))'
    def  length(self):
        return (self.x**2 + self.y**2)**0.5
class Triangle():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def is_triangle(self):
        if self.a<0 or self.b<0 or self.c<0:
            return f'с отрицательными числами ничего не получится'
        elif self.a>self.b+self.c or self.b>self.c+self.a or self.c>self.b+self.a:
            return f'такой треугольник построить нельзя'
        else:
            return 'такой треугольник построить можно'





