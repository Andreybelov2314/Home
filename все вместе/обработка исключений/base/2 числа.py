from sys import exception


def worker(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        print(f'{num1}/{num2}={num1/num2}')
    except ZeroDivisionError:
        print('ошибка-на ноль делить нельзя')
    except ValueError:
        print('неверный тип данных')
    except exception():
        print('ошибка')
worker(5, 2)
worker(5, 0)
worker(5, 'три')