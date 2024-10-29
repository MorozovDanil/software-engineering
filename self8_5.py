class Animal:
    def sound(self):
        return "*Какой-то звук"

class Dog(Animal):
    def sound(self):
        return "Гав"

dog = Dog()
print(dog.sound())