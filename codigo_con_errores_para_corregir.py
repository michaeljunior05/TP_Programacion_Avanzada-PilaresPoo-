class Dog:
    def __init__(self, name): #corregir asignar el valor al atributo de la instancia
        self.name = name      #del método __init__, para que name quede almacenado en el objeto.

    def speak(self):
        return "woof"

dog = Dog("Bobby")
print(dog.name)
