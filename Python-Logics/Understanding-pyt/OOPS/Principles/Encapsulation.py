class BankAccount:
    def __init__(self,balance):
        self.__balance = balance # private variable

    def amount_deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
acc = BankAccount(1000)
acc.amount_deposit(500)
print(acc.get_balance())
