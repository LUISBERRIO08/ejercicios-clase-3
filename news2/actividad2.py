class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")


class Perro(Animal):
    def __init__(self, nombre, especie, raza):
        super().__init__(nombre, especie)  # Hereda de Animal
        self.raza = raza

    def mostrar_raza(self):
        print(f"Raza: {self.raza}")


mi_perro = Perro(input("ingrese el nombre del perro: "), input("ingrese la especie del perro: "), input("ingrese la raza del perro: "))
mi_perro.mostrar_info()
mi_perro.mostrar_raza()