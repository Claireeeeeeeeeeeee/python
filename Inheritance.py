class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def speak(self):
        raise NotImplementedError("Child classes must implement this method")
class Dog(Animal):
    def speak(self):
        return "Woof"
class Cat(Animal):
    def speak(self):
        return "Meaw"
class Duck(Animal):
    def speak(self):
        return "Quaks"

dog =Dog("Bosco","Black")
print(dog.name)
print(dog.color)
print(dog.speak())

cat =Cat("Ginger","Brown")
print(cat.name)
print(cat.color)
print(cat.speak())

duck =Duck("Duckie","White")
print(duck.name)
print(duck.color)
print(duck.speak())