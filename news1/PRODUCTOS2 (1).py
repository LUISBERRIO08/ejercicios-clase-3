class Producto:
    
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        if self.stock >= cantidad:
            print(f"Sí hay {cantidad} unidades disponibles.")
        else:
            print(f"No hay suficiente stock. Disponible: {self.stock}")

    def vender(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            print(f"Venta realizada. Stock restante: {self.stock}")
        else:
            print("No se puede realizar la venta. Stock insuficiente.")

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Producto reabastecido. Nuevo stock: {self.stock}")


# Crear el producto
nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
stock = int(input("Ingrese el stock inicial: "))

producto1 = Producto(nombre, precio, stock)

# Menú interactivo
opcion = 0

while opcion != 4:
    print("\n--- MENÚ ---")
    print("1. Verificar disponibilidad")
    print("2. Vender producto")
    print("3. Reabastecer producto")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        cantidad = int(input("Ingrese la cantidad a verificar: "))
        producto1.verificar_disponibilidad(cantidad)

    elif opcion == 2:
        cantidad = int(input("Ingrese la cantidad a vender: "))
        producto1.vender(cantidad)

    elif opcion == 3:
        cantidad = int(input("Ingrese la cantidad a reabastecer: "))
        producto1.reabastecer(cantidad)

    elif opcion == 4:
        print("Saliendo del sistema...")

    else:
        print("Opción inválida. Intente nuevamente.")