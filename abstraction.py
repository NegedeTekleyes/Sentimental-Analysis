# from abc import ABC,abstractmethod
# class User:
#     def __init__(self, name,email):
#         self.name= name
#         self.email = email

# class BankAccount(ABC):
#     def __init__(self, balance,user):
#         self.balance = balance
#         self.user = user
#     @abstractmethod
#     def deposite(self,amount):
#         pass
#     @abstractmethod
#     def withdraw(self,amount):
#         pass
# class SavingAccount(BankAccount):
#     def deposite(self,amount):
#         self.balance += amount
#         print(f"Your balance is {self.balance}")
#     def withdraw(self, amount):
#         self.balance -= amount

# user1 = User("Alice","Alice@gmail.com")
# bank_account1 = SavingAccount(150, user1)
# bank_account1.deposite(100)
# print(bank_account1)



# encapsulation
class Student:
    def __init__(self,grade):
        self._grade = grade  # protected
    def set_grade(self,value):
        if 0 <= value <= 100:
            self.__grade = value
        else:
            print("Invalid")
    def get_grade(self):
        return self._grade
gade1 = Student(45)
print(gade1.get_grade())


# inheritance
class Animal:
    def __init__(self,sound):
        self.sound=sound
    def make_sound(self):
        print(self.sound)

class Dog(Animal):
    def bark(self):
        print("Bark")
animal1 = Dog("Animal sound")
animal1.make_sound()
animal1.bark()

