from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

if __name__ == "__main__":
    bobby = Dog()
    garfield = Cat()

    print(bobby.sound())
    print(garfield.sound())

    # Trying to instantiate an Animal object will raise a TypeError
    # animal = Animal()
    # print(animal.sound())
