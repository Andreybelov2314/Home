import csv
data=[
    ['id','name','age','grade','subjects','attendance','scores'],
    [1,'Иван Иванов','16','10A',"math,physics,chemistry",95,"90,85,88"],
    [2,'Мария Петрова','17','11B',"math,biology,english",87,"92,78,95"],
    [3,'Алексей Сидоров',16,'10A',"physics,chemistry,informatics",92,"87,89,91"],
    [4,'Елена Кузнецова',17,'11B',"math,chemistry,english",88,"94,86,92"],
    [5,'Дмитрий Волков',16,'10B',"biology,geography,english",91,"79,88,94"],
    [6,'Анна Смирнова',17,'11A',"math,physics,informatics",96,"96,92,93"],
    [7,'Сергей Попов',16,'10A',"chemistry,biology,geography",83,"85,82,87"],
    [8,'Ольга Орлова',17,'11B',"math,english,informatics",90,"91,96,88"],
    [9,'Павел Новиков',16,'10B',"physics,informatics,geography",94,"89,94,85"],
    [10,'Татьяна Морозова',17,'11A',"math,chemistry,physics",89,"93,87,90"]
]
with open('C:\\Users\\andre\\Documents\\Py_files\\employees.csv', 'w', encoding='utf-8', newline='') as f:
    writer=csv.writer(f)
    writer.writerows(data)

def file_update(filename):
    while True:
        dec=input('введите команду:1-посмотреть данные студента, 2-добавить студента, 3-посмотреть список всех студентов')
        if dec=='-1':
            break
        elif dec=='1':
            with open(filename, 'r', encoding='utf-8', newline='') as f:
                reader = csv.DictReader(f)
                name=input('введите имя студента')
                for i in reader:
                    if i['name'] == name:
                        print(i)
        elif dec=='2':
            with (open(filename, 'a', encoding='utf-8', newline='') as f):
                upd=[]
                id=input('введите номер студента')
                upd.append(id)
                name=input('имя')
                upd.append(name)
                age=input('возраст')
                upd.append(age)
                grade=input('класс')
                upd.append(grade)
                subjects=input('предметы')
                upd.append(subjects)
                attendance=input('процент посещений')
                upd.append(attendance)
                scores=input('оценки')
                upd.append(scores)
                writer=csv.writer(f)
                writer.writerow(upd)
        elif dec=='3':
            with open(filename, 'r', encoding='utf-8', newline='') as f:
                reader = csv.DictReader(f)
                students=[]
                for i in reader:
                    students.append(i['name'])
                print(students)
file_update('C:\\Users\\andre\\Documents\\Py_files\\employees.csv')

