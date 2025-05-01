class Vehículo():
    def__init__(self,modelo,marca,color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
    def mostrar_info(self):
        return f"Vehículo -- {self.modelo} -- {self.marca} -- {self.color}"