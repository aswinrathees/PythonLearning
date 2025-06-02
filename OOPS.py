# Introduction to OOPs

class Person:
    def __init__(self, name, experience):
        self.name = name                # Instance variable for name
        self.experience = experience    # Instance variable for experience

    def greet(self):
        print(f"Hello, my name is {self.name} and I am having {self.experience} years of experience.")

    def getName(self):
        return self.name
    
    def getExperience(self):
        return self.experience

p = Person("Aswin", "8")  # Create an instance of the Person class
print(p)
print(p.name)             # Accessing instance variable directly
print(p.experience)       # Accessing instance variable directly

# Inheritance

class Car:
    def __init__(self):
        self.wheel = 4
        self.seat = 5

    def drive(self):
        print("Driving the car")


class SportsCar(Car):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.engine = "V8"
        self.seats = 2

    def drive(self):
        print("Driving the sports car at high speed")


sportsCar = SportsCar()  # Create an instance of the SportsCar class
sportsCar.drive()  # Call the overridden method
