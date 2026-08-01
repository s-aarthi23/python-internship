class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        self.__balance=balance
account=BankAccount(1000)
print(account.get_balance())    
account.set_balance(1500)
print(account.get_balance())    