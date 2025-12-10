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


obj1=Task()
obj1.title='сделать дз'
obj1.task_status()
obj1.task_dct()
print(obj1.dct_title)
obj2=Task()
obj2.title='поспать'
obj2.task_dct()
print(Task.all_tasks)



