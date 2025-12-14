class BankAccount1:
    def __init__(self, balance):
        self.balance = balance
    def deposite(self, amount):
        self.balance +=amount
        print(f"You have deposited {amount},now your balance is {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficent balance")
            return
        self.balance -= amount
        print(f"You have withdraw {amount} your remaning balance {self.balance}")
# Now lets create another saving account that inherits from bank account class in the above
class SavingAccount(BankAccount1):
    def __init__(self, balance, interest=0.01):
        BankAccount1.__init__(self,balance)
        self.interest= interest
    def deposite(self, amount):
        super().deposite(amount)
        self.balance += amount*self.interest + amount
        print(f"With interest, your new balance is: {self.balance}")
    def report(self):
        print(f"Your balan is {self.balance}")
# saving_account1= SavingAccount(300, 0.01)
# # saving_account1.withdraw(50)
# saving_account1.deposite(50)
# saving_account1.report()
# print(saving_account1)

# Python Magic methods are the methods starting and ending with double underscores '__'. They are defined by built-in classes in Python and commonly used for operator overloading. 

# They are also called Dunder methods, Dunder here means "Double Under (Underscores)".
class CheckingAccount(BankAccount1):
    def __add__(self,other): # __add__ dounder method means double underscore
        return self.balance + other.balance
    def withdraw(self, amount):
        credit = 100
        if amount > self.balance + credit:
            print("Insufficent balance")
            return
        self.balance -= amount
        print(f"You have withdrawn {amount}, now your balance is {self.balance}")
checking_account1 = CheckingAccount(500)
checking_account2 = CheckingAccount(500)
# checking_account.withdraw(700)
joint_account = checking_account1 + checking_account2
print(joint_account)
print(dir(int))