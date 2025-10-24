папка teest16.py

class BankAccount:

    def __init__(self, owner, balance=0):

        self.owner = owner

        self.balance = balance

  

    def deposit(self, amount):

        if amount > 0:

            self.balance += amount

  

    def withdraw(self, amount):

        if 0 < amount <= self.balance:

            self.balance -= amount

  

    def get_balance(self):

        return self.balance

  
  

class SavingsAccount(BankAccount):

    def __init__(self, owner, balance=0, interest_rate=0.01):

        super().__init__(owner, balance)

        self.interest_rate = interest_rate

  

    def apply_interest(self):

        interest = self.balance * self.interest_rate

        self.deposit(interest)


Разбор: 
1.  class BankAccount: - класс - банковский счёт
2.     def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance - функция init, owner имя владельца счёта, balance сумма на счёте, по умолчанию 0, self.balance сохраняет эту сумму внутри объекта.
3.     def deposit(self, amount):
        if amount > 0:
            self.balance += amount - **deposit** пополняет счёт, если сумма больше 0, она добавляется к балансу. попытка внести 0 или меньше проигнорируется.
4.     def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount - **withdraw** снимает деньги, проверяется: сумма больше 0 и не больше баланса, это защищает от **овердрафта** 
5.     def get_balance(self):
        return self.balance - get_banace просто возвращает баланс
6.    class SavingsAccount(BankAccount): - подкласс от BankAccount, он получает методы и свойства BankAccount
7.     def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate - процентная ставка interest_rate, super().__init__() вызывает init родителя BankAccount устанавливает владельца и баланс.
8.     def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest) - apply_interest начисляет проценты, считает, сколько процентов нужно добавить: баланс ставка, затем пополняет счёт этой суммой через deposit

Примечание: 
Функция называется get_balance, а не balancе. Потому что при написании balance в коде python возможно произошел бы конфликт из-за одинаковых имён. Сама приставка get означает действие, что упрощает чтение кода + при замены переменой это будет сделать куда проще. 



