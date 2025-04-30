def decorator(func): 
    print("Decorating...") 
    return func 

@decorator 
def greet(): 
    print("Hi!") 

greet()

#Corregir: Mostrar cómo se aplica realmente un decorador con un wrapper. 
