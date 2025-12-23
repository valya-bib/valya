class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.__balance = 0
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("счет пополнен на " + str(amount) + " новый баланс: " + str(self.__balance))
        else:
            print("сумма пополнения должна быть положительной")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("недостаточно средств")
        else:
            self.__balance -= amount
            print("со счета снято " + str(amount) + (" новый баланс: ") + str(self.__balance))

    def get_balance(self):
        return self.__balance

if __name__ == "__main__":
    account = BankAccount("6473846")

    print("баланс: " + str(account.get_balance()))

    print(account.deposit(10000))  
    print(account.withdraw(500))
   

    
                  