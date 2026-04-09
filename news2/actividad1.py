class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  # Hereda de Persona
        self.grado = grado

    def mostrar_grado(self):
        print(f"Grado: {self.grado}")



est = Estudiante (input("ingrese el nombre del estudiante: "), int(input("ingrese la edad del estudiante: ")), input("ingrese el grado del estudiante: "))

est.mostrar_datos()
est.mostrar_grado()

