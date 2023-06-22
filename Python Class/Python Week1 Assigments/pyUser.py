class user:
    def __init__(self, firstName, lastName, email, age):
        # args
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.age = age

        # atts
        self.isRewardsMember = False
        self.goldCardPoints = 0

    # method display
    def dislpayInfo(self):
        print(f"First Name: {self.firstName}")
        print(f"Last Name: {self.lastName}")
        print(f"Email Address: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards member: {self.isRewardsMember}")
        print(f"Gold Card Points: {self.goldCardPoints}")

    # method enroll
    def enroll(self):
        if self.isRewardsMember == False:
            self.isRewardsMember = True
        else:
            print("User is already a member.")
            return
        self.goldCardPoints = 200

    # method spend points
    def spendPoints(self, amount):
        if self.goldCardPoints - amount <= 0:
            print("User does not have enough points!")
        else:
            self.goldCardPoints = self.goldCardPoints - amount

# calling the class to ouput
userSam = user("Sam", "Dalrymple", "SamDalrympe@email.com", 24)
userJohn = user("John", "Smith", "JohnnySmith@email.com", 32)
userJake = user("Jake", "Espana", "ChromeJake@email.com", 99)

# callign methods to update the information in the class
userSam.enroll()
userSam.spendPoints(50)
userSam.dislpayInfo()

print("\n")

userJake.enroll()
userJake.spendPoints(80)
userJake.dislpayInfo()

print("\n")

userJohn.enroll()
userJohn.spendPoints(40)
userJohn.dislpayInfo()


# BONUS SECTION
print("\n")

userSam.enroll()
userSam.spendPoints(500)
userSam.dislpayInfo()