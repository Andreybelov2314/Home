def main(filename):
    print('1-ввести новую задачу')
    print('2-посмотреть списко задач')
    print('3-выйти из программы')
    while True:
        command=input('введите команду')
        if command == '1':
            with open(filename, 'a', encoding='utf-8') as f:
                dec=input('введите текст задачи')
                f.write(dec+'\n')
            print('задача добавлена')
        elif command == '2':
            with open(filename, 'r', encoding='utf-8') as f:
                data=f.readlines()
                for i in data:
                    print(i)
        elif command == '3':
            break
    return ''
main('file.txt')

