#   Guillermo Enrique Valles Villegas
#   A01561722
#   
#           TABLA DE VARIABLES
#   Tabla con diccionario para guardar las variables del programa
import sys

class tablaVariables:
    def __init__(self):
        self.variables = { }
        
    def search(self, id):               # DEVUELVE TRUE OR FALSE SI LA VARIABLE EXISTE
        return id in self.variables
    
    def add(self, id, type):            # AGREGA LA VARIABLE Y TIPO A LA TABLA
        self.variables[id] = {
            'type': type
        }
        
    def print(self):                    # IMPRIME LA TABLA
        #print(self.variables)
        for i in self.variables:
            print( i, 'esta en lista de variables')


# if __name__ == "__main__":
#     tablaVar = tablaVariables()
#     tablaVar.add('x', 'int')
#     tablaVar.add('y', 'float')
#     tablaVar.print()