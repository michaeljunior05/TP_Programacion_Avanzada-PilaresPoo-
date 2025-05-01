class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "woof"

dog = Dog("Bobby")
print(dog.name)
