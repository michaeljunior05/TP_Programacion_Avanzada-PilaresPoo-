class Vehiculo:
    def __init__(self,modelo:str,marca:str,color:str):
        self.modelo = modelo
        self.marca = marca
        self.color = color
    def mostrar_info(self):
        return f"Vehículo -- {self.modelo} -- {self.marca} -- {self.color}."

class Moto(Vehiculo):
    def __init__(self,modelo:str,marca:str,color:int,ruedas:int,luces:int):
        super().__init__(modelo,marca,color)
        self.ruedas = ruedas
        self.luces = luces
    
    
    def mostrar_info(self):
        return f"Moto -- {super().mostrar_info(self)} -- {self.ruedas} -- {self.luces}."

class Auto(Vehiculo):

    def __init__(self,modelo:str,marca:str,color:str,ruedas:int,luces:int):
        super().__init__(modelo,marca,color)
        self.ruedas = ruedas
        self.luces = luces
    
    def mostrar_info(self):
        return f"Auto -- {super().mostrar_info(self)} -- {self.ruedas} -- {self.luces}."


