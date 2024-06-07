class StudentAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        if amount <= 50000:
            super().deposit(amount)
        else:
            print("Deposit limit exceeded for Student Account!")

    def withdraw(self, amount):
        if amount <= 2000:
            super().withdraw(amount)
        else:
            print("Withdrawal limit exceeded for Student Account!")
