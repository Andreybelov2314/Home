class InsufficientFundsError(ValueError):
    def __init__(self, balance, transfer):
        massage=f'недостаточно средств на балансе:{balance}, {transfer}'
        super().__init__(massage)
        self.balance=balance
        self.transfer=transfer
class NegativeAmountError(ValueError):
    def __init__(self, operation):
        message='сумма перевода не может быть отрицательной'
        super().__init__(message)
        self.operation=operation
class AccountLockedError(RuntimeError):
    def __init__(self, account):
        message=f'аккаунт {account} был заблокирован'
        super().__init__(message)
        self.account=account
class account():
    def __init__(self, name, balance, lock,history):
        self.name=name
        self.balance=balance
        self.lock=lock
        self.history=history
    @property
    def nm(self):
        return self.name

    @nm.setter
    def nm(self, value):
        self.name=value
    @property
    def bl(self):
        return self.balance

    @bl.setter
    def bl(self, value):
        self.balance=value
    @property
    def lc(self):
        return self.lock

    @lc.setter
    def lc(self, value):
        self.lock=value
    @property
    def ht(self):
        return self.history

    @ht.setter
    def ht(self, value):
        self.history.append(value)