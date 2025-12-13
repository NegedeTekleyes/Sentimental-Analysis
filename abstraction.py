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

# polymorphism
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat(),Animal()]
for a in animals:
    a.speak()

class Payment:
    def Pay(self):
        print("Payment through")
class Telebir(Payment):
    def Pay(self):
        
        print("Payment through Telebir")

class Bank(Payment):
    def Pay(self):
        print("Payment through Bank")

Payment1 =[Payment(),Telebir(),Bank()]
for P in Payment1:
    P.Pay()

# Absracctions
from abc import ABC, abstractmethod
#
# abstract class
class Superhero(ABC):
    def __init__(self,name,power):
        self.name= name
        self.power = power
    @abstractmethod
    def fight_crime(self):
        pass
    @abstractmethod
    def use_power(self):
        pass
# concrete class
class FlyingHero(Superhero):
    def fight_crime(self):
        print(f"{self.name} soars into the sky to fight crime!")
    def use_power(self):
        print(f"{self.name} soars into the sky to fight crime!")
class StregthHero(Superhero):
    def fight_crime(self):
        print(f"{self.name} soars into the sky to fight crime!")
    def use_power(self):
        print(f"{self.name} soars into the sky to fight crime!")
hero1 = FlyingHero("SkyWing","WindBlast")
hero_list = [hero1]

for hero in hero_list:
    hero.fight_crime()
