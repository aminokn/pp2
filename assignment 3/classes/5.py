class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance = self.balance + money

    def withdraw(self, unmoney):
        if unmoney < 0: print('wrong number')
        elif self.balance - unmoney < 0: print('Недостаточно средств для снятия')
        else: self.balance = self.balance - unmoney

    def show_balance(self):
        print(self.balance)
        
# amina = Account("Amina", 15)
# amina.deposit(14)
# amina.withdraw(16)
# amina.show_balance()
