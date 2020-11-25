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
    
    def addArr(self, id, typeV, memory, size, m1, m2, L1, L2):            # AGREGA EL ARREGLO Y TIPO A LA TABLA
        self.variables[id] = {
            'typeV': typeV,
            'memory': memory,
            'size': size,
            'm1': m1,
            'm2': m2,
            'L1': L1,
            'L2': L2
        }
    
    def getM(self, id, num):            # AGREGA EL ARREGLO Y TIPO A LA TABLA
        if num ==1:
            return self.variables[id]['m1']

        else:
            return self.variables[id]['m2']
    
    def getLim(self, id, num):            # AGREGA EL ARREGLO Y TIPO A LA TABLA
        if num == 1:
            return self.variables[id]['L1']
        else:
            return self.variables[id]['L2']

    
    def checkArray(self, id):            # AGREGA EL ARREGLO Y TIPO A LA TABLA
        try:
            if 'size' in self.variables[id].keys():
                return True
            else:
                return False     
        except:
            print('ERROR: VAR',id, 'NOT DECLARED')
            exit()
    
    def initialValues(self):
        return self.variables   

        
    def print(self):                    # IMPRIME LA TABLA
        if(self.variables != {}):
            print('VARIABLES:')
            print(self.variables)