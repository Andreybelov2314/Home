from classes import *
def worker(name, balance, lock, history):
    acc=account(name, balance, lock, history)
    while True:
        com=input('введите команду:1-провести транзакцию, 2-посмотреть историю транзакций, 3-вывести всю информацию')
        if com=='1':
            com2=input('введите сумму перевода')
            try:
                if int(com2)<0:
                    raise NegativeAmountError(com2)
                elif int(balance)-int(com2)<0:
                    raise InsufficientFundsError(balance,com2)
                elif lock==True:
                    raise AccountLockedError(name)
                else:
                    acc.balance=balance-int(com2)
                    history.append(com2)
            except NegativeAmountError as e:
                print(e)
            except InsufficientFundsError as e:
                print(e)
            except AccountLockedError as e:
                print(e)
        elif com=='2':
            print(acc.history)
        elif com=='3':
            print(f'{acc.name}, {acc.balance}, {acc.lock}')
        else:
            break
worker('Andrey_belov',50000, False,[])