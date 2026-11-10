class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} говорит: Гав"
dog1 = Dog("Рекс", 3)
dog2 = Dog("Арчи", 4)
print(dog1.name)
print(dog1.bark())
print(dog2.name)
print(dog2.bark())