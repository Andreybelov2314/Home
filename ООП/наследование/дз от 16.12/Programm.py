from Person import *
from Employee import *
from Manager import *
employees=[]
managers=[]
while True:
    dec=input('введите номер команды: 1-добавить работника, 2-добавить менеджера, 3-добавить работника в команд к менеджеру, 4-просмотр списка сотрудников')
    if dec=='1':
        name=input('enter name: ')
        age=input('enter age: ')
        position=input('enter position: ')
        obj=Employee(name,age,position)
        employees.append(obj.get_info())
    elif dec=='2':
        name=input('enter name: ')
        age=input('enter age: ')
        position=input('enter position: ')
        obj=Manager(name,age,position)
        managers.append(obj.get_info())
    elif dec=='3':
        em_name=input('enter employees name: ')
        m_name=input('enter managers name: ')
        for i in managers:
            if i.name==m_name:
                i.team.append(em_name)
                break
        print(f'работник {em_name} добавлен в команду к менеджеру {m_name}')
    elif dec=='4':
        print(employees)
    else:
        break

