# Definimos la clase padre (Base)
class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año

    def imprimir_detalles(self):
        print(f"Vehículo: Marca {self.marca}, Año {self.año}")

# Definimos la clase hija (Hereda de Vehiculo)
class Coche(Vehiculo):
    def __init__(self, marca, año, modelo):
        # Usamos super() para reutilizar el constructor de la clase padre
        super().__init__(marca, año)
        self.modelo = modelo

    def imprimir_modelo(self):
        print(f"Modelo del coche: {self.modelo}")
        
mi_carro = Coche(input("ingrese la marca del carro: "), int(input("ingrese el año del carro: ")), input("ingrese el modelo del carro: "))
mi_carro.imprimir_detalles()
mi_carro.imprimir_modelo()
