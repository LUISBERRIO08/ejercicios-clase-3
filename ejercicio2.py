class rectangulo:
    def __init__(self, largo, ancho):
        if largo <=  0 or ancho <= 0:
            raise ValueError("las dimensiones deben ser mayores que cero")
        self.largo = largo
        self.ancho = ancho
        
    def cambiar_dimensiones(self, largo, ancho):
        if largo <= 0 or ancho <= 0:
            raise ValueError("las dimensiones deben ser mayores que cero")  
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
         return self.largo * self.ancho
     
    def calcular_perimetro(self):
         return 2 * (self.largo + self.ancho)
    
    def obtener_dimensiones(self):
         return self.largo, self.ancho

largo = float(input("ingrese el largo del rectangulo: "))
ancho = float(input("ingrese el ancho del rectangulo: "))
rectangulo1 = rectangulo(largo, ancho)

print("dimensiones actuales:", rectangulo1.obtener_dimensiones())
print("área:", rectangulo1.calcular_area())
print("perímetro:", rectangulo1.calcular_perimetro())
 
nuevo_largo = float(input("ingrese el nuevo largo del rectangulo: "))
nuevo_ancho = float(input("ingrese el nuevo ancho del rectangulo: "))
rectangulo1.cambiar_dimensiones(nuevo_largo, nuevo_ancho)
print("dimensiones actualizadas:", rectangulo1.obtener_dimensiones())
print("área actualizada:", rectangulo1.calcular_area())
print("perímetro actualizado:", rectangulo1.calcular_perimetro())