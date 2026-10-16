from abc import ABC, abstractmethod

class Animal(ABC):
    def sound(self):
        pass

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Rio barks")

d = Dog()
d.speak()
