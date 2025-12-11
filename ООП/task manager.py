
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




obj1=task_manager()
obj1.tasks=[]
obj1.command()




