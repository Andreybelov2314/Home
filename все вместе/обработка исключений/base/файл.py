from sys import exception


def of(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data=f.readlines()
            for i in data:
                print(i)
    except FileNotFoundError:
        print('файл не найден')
    except exception():
        print('ошибка чтения файла')
of('C:\\Users\\andre\\Documents\\Py_files\\Текстовый документ.txt')
of('C:\\Users\\andre\\Documents\\Py_files\\Текстовый.txt')
of("C:\\Users\\andre\\Documents\\Py_files\\my_data.json")