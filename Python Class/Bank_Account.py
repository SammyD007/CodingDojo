class bankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, name, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
                self.name = name
                self.interestRate = int_rate
                self.balance = balance

    def deposit(self, amount):
        # your code here
        self.balance = amount
        return self

    def withdraw(self, amount):
        # your code here
        self.balance = self.balance - amount
        return self

    def display_account_info(self):
        # your code here
        print(self.name)
        print(self.balance)
        print(self.interestRate)
        print(self.yieldInterest)
        print("\n")

    def yield_interest(self):
        # your code here
        self.yieldInterest = self.balance * self.interestRate
        return self

account1 = bankAccount("account1", .01, 5000)
account1.deposit(500).deposit(1000).deposit(1000).withdraw(450).yield_interest().display_account_info()

account2 = bankAccount("account2", .03, 5000)
account2.deposit(500).deposit(10000).withdraw(1000).withdraw(400).withdraw(450).withdraw(450).yield_interest().display_account_info()