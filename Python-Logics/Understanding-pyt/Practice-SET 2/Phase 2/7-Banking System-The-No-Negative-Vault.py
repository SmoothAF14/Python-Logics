class bank:
    def balance(self, balance):
        self.__balance = balance # private variable
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("InSufficientFundsError.")
    def get_balance(self):
        return self.__balance
acc = bank()
acc.balance(1000)
print("Enter amount to deposit:")
x = int(input())
acc.deposit(x)
print("Enter amount to withdraw:")
y = int(input())
acc.withdraw(y)
print(f"Your current balance is: {acc.get_balance()}")
