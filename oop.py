class Car:
    # lets create a method
    def __init__(self, name, model, year):
        self.name =name
        self.model = model
        self.year = year
    def print_car(self):
        print("Name:", self.name)
        print("Model:", self.model)
        print("Year:", self.year)
    def start_engine(self):
        print(f"Engine has started for car {self.name}")
        # lets craete objetct
car1 = Car(name= "Toyota", model="Mercedes", year= 1999)
car2 = Car(name= "Ford", model="Ford", year= 2012)
car1.print_car()


# encapsulation means hideing the detaile for example when yiu drive
# car you can't see the engin that use to acclerate the car.
# class BankAccount:
#     def __init__(self, balance, pin):
#         self.balance = balance
#         self.__pin = pin
#         @property
#         def pin(self):
#             return self.__pin
#         @pin.setter
#         def pin(self, value):
#             self.__pin = value
#     def deposite(self, amount):
#         self.balance += amount
#         print(f'You have deposited {amount},')
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficent balance")
#             return 
#         self.balance -=amount
#         print(f"You have withdrawn {amount},")
# account1 = BankAccount(100, 2234)
# account1.__pin= 2234
# print(account1.__pin)

# inheritance in python
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

class CheckingAccount(BankAccount1):
    def withdraw(self, amount):
        credit = 100
        if amount > self.balance + credit:
            print("Insufficent balance")
            return
        self.balance -= amount
        print(f"You have withdrawn {amount}, now your balance is {self.balance}")
checking_account = CheckingAccount(500)
checking_account.withdraw(700)

# decorator in python
# Decorators in Python are a powerful and expressive tool that allows you to modify the behavior of a function or a method. They act as wrappers around a function, adding functionality before or after
#  the original function runs.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
    
@my_decorator
def say_hello():
    print("Hello")
say_hello()

