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
    
    def addArr(self, id, typeV, memory, size, m1, m2):            # AGREGA EL ARREGLO Y TIPO A LA TABLA
        self.variables[id] = {
            'typeV': typeV,
            'memory': memory,
            'size': size,
            'm1': m1,
            'm2': m2
        }
    def checkArray(self, id):            # AGREGA EL ARREGLO Y TIPO A LA TABLA
        if 'size' in self.variables[id].keys():
            return True
        else:
            return False      
    
    def initialValues(self):
        return self.variables    
        
    def print(self):                    # IMPRIME LA TABLA
        # for key in self.variables:
        if(self.variables != {}):
            print('VARIABLES:')
            print(self.variables)
                # print(self.variables[key]['tabla'])
                # if(self.variables[key]['tabla'] != {}):
                #     self.variables[key]['tabla']
            


# if __name__ == "__main__":
#     tablaVar = tablaVariables()
#     tablaVar.add('x', 'int', 10002)
#     tablaVar.add('y', 'float', 3001)
#     tablaVar.print()
#     x = tablaVar.getType('x')
#     print(x)