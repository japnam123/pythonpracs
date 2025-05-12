class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def increment(self):
        self.x += 1
        self.y += 1
        self.z += 1
    
    def decrement(self):
        self.x -= 1
        self.y -= 1
        self.z -= 1
    
    def add(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __lt__(self, other):
        return (self.x < other.x and self.y < other.y and self.z < other.z)
    
    def __gt__(self, other):
        return (self.x > other.x and self.y > other.y and self.z > other.z)
    
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)
    
    def quadrant(self):
        if self.x > 0 and self.y > 0:
            return "First Quadrant"
        elif self.x < 0 and self.y > 0:
            return "Second Quadrant"
        elif self.x < 0 and self.y < 0:
            return "Third Quadrant"
        elif self.x > 0 and self.y < 0:
            return "Fourth Quadrant"
        else:
            return "On axis"
    
    def is_collinear(self, p2, p3):
        # Check if three points are collinear
        x1, y1 = self.x, self.y
        x2, y2 = p2.x, p2.y
        x3, y3 = p3.x, p3.y
        
        return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)
    
    def __str__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

class Watch:
    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s
        self.alarm_hours = 0
        self.alarm_minutes = 0
        self.alarm_active = False
    
    def set_alarm(self, h, m):
        self.alarm_hours = h
        self.alarm_minutes = m
        self.alarm_active = True
    
    def stop_alarm(self):
        self.alarm_active = False
    
    def check_alarm(self):
        return (self.hours == self.alarm_hours and 
                self.minutes == self.alarm_minutes and 
                self.alarm_active)

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit_money(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw_money(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def show_balance(self):
        return self.__balance

class Vehicle:
    def __init__(self, color, capacity, engine_power, type):
        self.color = color
        self.capacity = capacity
        self.engine_power = engine_power
        self.type = type
    
    def start(self):
        print(f"{self.type} is starting")
    
    def stop(self):
        print(f"{self.type} is stopping")

class Car(Vehicle):
    def __init__(self, color, capacity, engine_power, type, airbags, gear, speed, fuel):
        super().__init__(color, capacity, engine_power, type)
        self.airbags = airbags
        self.gear = gear
        self.speed = speed
        self.fuel = fuel
    
    def accelerate(self):
        self.speed += 10
        print(f"Speed increased to {self.speed}")
    
    def fill_fuel(self, amount):
        self.fuel += amount
        print(f"Fuel level: {self.fuel}")
    
    def play_music(self):
        print("Playing music")
    
    def on_ac(self):
        print("AC turned on")

class ElectricCar(Car):
    def __init__(self, color, capacity, engine_power, type, airbags, gear, speed, fuel, battery):
        super().__init__(color, capacity, engine_power, type, airbags, gear, speed, fuel)
        self.battery = battery
    
    def charging(self):
        self.battery += 20
        print(f"Battery level: {self.battery}%")
    
    def battery_level(self):
        return self.battery

class Person:
    def get_gender(self):
        pass

class Male(Person):
    def get_gender(self):
        return "Male"

class Female(Person):
    def get_gender(self):
        return "Female"

# Pharmaceutical example
from abc import ABC, abstractmethod

class DrugFormulation(ABC):
    def __init__(self, name, active_ingredient, dosage):
        self.__name = name
        self.__active_ingredient = active_ingredient
        self.__dosage = dosage
    
    @abstractmethod
    def administer(self):
        pass
    
    def get_name(self):
        return self.__name
    
    def get_active_ingredient(self):
        return self.__active_ingredient
    
    def get_dosage(self):
        return self.__dosage

class Tablet(DrugFormulation):
    def administer(self):
        return f"Take {self.get_dosage()} of {self.get_name()} orally"

class Capsule(DrugFormulation):
    def administer(self):
        return f"Swallow {self.get_dosage()} of {self.get_name()} with water"

class Injection(DrugFormulation):
    def administer(self):
        return f"Administer {self.get_dosage()} of {self.get_name()} intramuscularly"

if __name__ == "__main__":
    # Test Point class
    p1 = Point(1, 2, 3)
    p2 = Point(4, 5, 6)
    print(p1)
    print(p1.quadrant())
    
    # Test Watch class
    watch = Watch(10, 30, 0)
    watch.set_alarm(10, 30)
    print(watch.check_alarm())
    
    # Test BankAccount class
    account = BankAccount("12345", 1000)
    account.deposit_money(500)
    print(account.show_balance())
    
    # Test Vehicle hierarchy
    car = Car("Red", 5, "2000cc", "Sedan", 6, "Manual", 0, 50)
    car.accelerate()
    car.play_music()
    
    electric_car = ElectricCar("Blue", 5, "Electric", "SUV", 8, "Automatic", 0, 0, 80)
    electric_car.charging()
    
    # Test Person hierarchy
    male = Male()
    female = Female()
    print(male.get_gender())
    print(female.get_gender())
    
    # Test Pharmaceutical example
    tablet = Tablet("Aspirin", "Acetylsalicylic acid", "500mg")
    capsule = Capsule("Amoxicillin", "Amoxicillin trihydrate", "250mg")
    injection = Injection("Insulin", "Human insulin", "100 units")
    
    print(tablet.administer())
    print(capsule.administer())
    print(injection.administer()) 