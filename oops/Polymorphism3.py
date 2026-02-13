from abc import ABC , abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#
# class Dog(Animal):
#     def sound(self):
#         print("Dog Barks")
#
# c = Dog()
# c.sound()





class Vehical(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehical):
    pass

c = Car()
c.start()
