class bankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
                self.interestRate = int_rate
                self.balance = balance


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = bankAccount(int_rate = 0.02, balance = 0)

    def makeDeposit(self, amount):
        self.account.balance = self.account.balance + amount
        return self

    def makeWithdraw(self, amount):
        self.account.balance = self.account.balance - amount
        return self

    def displayUserBalance(self):
        print(self.account.balance)

user1 = User("Sam", "sam@email.com")
user1.makeDeposit(5000).makeWithdraw(500).displayUserBalance()

# I might come back and do the sensei bonuses. It's late and I wanted to finish and turn this in before going to bed.