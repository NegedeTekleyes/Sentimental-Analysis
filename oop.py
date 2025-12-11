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
class BankAccount:
    def __init__(self, balance, pin):
        self.balance = balance
        self.__pin = pin
        @property
        def pin(self):
            return self.__pin
        @pin.setter
        def pin(self, value):
            self.__pin = value
    def deposite(self, amount):
        self.balance += amount
        print(f'You have deposited {amount},')
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficent balance")
            return 
        self.balance -=amount
        print(f"You have withdrawn {amount},")
account1 = BankAccount(100, 2234)
account1.__pin= 2234
print(account1.__pin)
