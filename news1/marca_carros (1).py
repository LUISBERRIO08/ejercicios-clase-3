class Vehiculo:
    
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        if self.velocidad_actual + incremento <= self.velocidad_maxima:
            self.velocidad_actual += incremento
        else:
            self.velocidad_actual = self.velocidad_maxima
        print("Velocidad actual:", self.velocidad_actual, "km/h")

    def frenar(self, decremento):
        if self.velocidad_actual - decremento >= 0:
            self.velocidad_actual -= decremento
        else:
            self.velocidad_actual = 0
        print("Velocidad actual:", self.velocidad_actual, "km/h")

    def verificar_limite(self, velocidad_limite):
        if self.velocidad_actual > velocidad_limite:
            print("⚠ Está superando el límite de velocidad.")
        else:
            print("✅ Está dentro del límite permitido.")



marca = input("Ingrese la marca del vehículo: ")
modelo = input("Ingrese el modelo: ")
velocidad_maxima = int(input("Ingrese la velocidad máxima: "))

carro = Vehiculo(marca, modelo, velocidad_maxima)


opcion = 0

while opcion != 4:
    print("\n--- MENÚ ---")
    print("1. Acelerar")
    print("2. Frenar")
    print("3. Verificar límite")
    print("4. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        incremento = int(input("¿Cuánto desea acelerar? "))
        carro.acelerar(incremento)
        
    elif opcion == 2:
        decremento = int(input("¿Cuánto desea frenar? "))
        carro.frenar(decremento)
        
    elif opcion == 3:
        limite = int(input("Ingrese el límite de velocidad: "))
        carro.verificar_limite(limite)
        
    elif opcion == 4:
        print("Saliendo del sistema...")
        
    else:
        print("Opción inválida.")