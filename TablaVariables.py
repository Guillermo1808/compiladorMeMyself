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
    
    def getType(self, id):                      #DEVUELVE EL TIPO DE VARIABLE
        return self.variables[id]['typeV']
    
    def getDir(self, id):                      #DEVUELVE LA DIRECCION DE VARIABLE
        return self.variables[id]['memory']
    
    def add(self, id, typeV, memory):            # AGREGA LA VARIABLE Y TIPO A LA TABLA
        self.variables[id] = {
            'typeV': typeV,
            'memory': memory
        }
        
        
    def print(self):                    # IMPRIME LA TABLA
        if(self.variables != {}):
            print('VARIABLES:')
            print(self.variables)


# if __name__ == "__main__":
#     tablaVar = tablaVariables()
#     tablaVar.add('x', 'int', 10002)
#     tablaVar.add('y', 'float', 3001)
#     tablaVar.print()
#     x = tablaVar.getType('x')
#     print(x)