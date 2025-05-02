class Vehiculo:
    def __init__(self,modelo:str,marca:str,color:str):
        self._modelo = modelo
        self._marca = marca
        self._color = color
        
    def get_modelo(self):
        return self._modelo
        
    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color
        
    def mostrar_info(self):
        return f"Vehículo -- {self._modelo} -- {self._marca} -- {self._color}."

class Moto(Vehiculo):
    def __init__(self,modelo:str,marca:str,color:str,ruedas:int,luces:int):
        super().__init__(modelo,marca,color)
        self._ruedas = ruedas
        self._luces = luces

    def get_ruedas(self):
        return self._ruedas
        
    def set_ruedas(self, ruedas):
        self._ruedas = ruedas

    def get_luces(self):
        return self._luces

    def set_luces(self, luces):
        self._luces = luces
    
    def mostrar_info(self):
        return f"Moto -- {super().mostrar_info()} -- ruedas: {self._ruedas} -- luces: {self._luces}."

class Auto(Vehiculo):

    def __init__(self,modelo:str,marca:str,color:str,ruedas:int,luces:int):
        super().__init__(modelo,marca,color)
        self._ruedas = ruedas
        self._luces = luces

    def get_ruedas(self):
        return self._ruedas

    def set_ruedas(self, ruedas):
        self._ruedas = ruedas

    def get_luces(self):
        return self._luces

    def set_luces(self, luces):
        self._luces = luces
        
    def mostrar_info(self):
        return f"Auto -- {super().mostrar_info()} -- ruedas: {self._ruedas} -- luces: {self._luces}."

def mostrar_informacion(vehiculo):
    print(vehiculo.mostrar_info())

