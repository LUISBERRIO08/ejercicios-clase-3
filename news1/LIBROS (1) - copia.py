# Crear la clase Libro
class Libro:
    
    # Constructor
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
    
    # Método para mostrar información
    def mostrar_informacion(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Número de páginas:", self.numero_paginas)
    
    # Método para actualizar número de páginas
    def actualizar_paginas(self, nuevas_paginas):
        self.numero_paginas = nuevas_paginas
        print("Número de páginas actualizado correctamente.")


 
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)

 libro1.mostrar_informacion()

print("\nActualizando páginas...\n")

 libro1.actualizar_paginas(500)

 libro1.mostrar_informacion()