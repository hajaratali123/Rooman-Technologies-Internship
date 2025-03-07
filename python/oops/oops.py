class Encapsulated:
    def __init__(self, value):
        self.__private_value = value  # Private attribute

    def get_value(self):
        return self.__private_value
    
    def set_value(self, new_value):
        self.__private_value = new_value

obj = Encapsulated(10)
print(obj.get_value())  # Output: 10



class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!")  # Overriding the parent method

dog = Dog()
dog.speak()  # Output: Woof!



class Cat(Animal):
    def speak(self):
        print("Meow!")

# Using polymorphism: different objects respond to the same method call.
for animal in [Dog(), Cat()]:
    animal.speak()
# Output:
# Woof!
# Meow!


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

car = Car()
car.start()  # Output: Car started


class Example:
    class_var = 0  # Class variable
    
    def __init__(self, value):
        self.instance_var = value  # Instance variable




class Utility:
    @staticmethod
    def add(a, b):
        return a + b
print(Utility.add(5, 3))  # Output: 8




class Person:
    species = "Homo sapiens"
    
    @classmethod
    def get_species(cls):
        return cls.species

print(Person.get_species())  # Output: Homo sapiens
