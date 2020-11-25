#   Guillermo Enrique Valles Villegas
#   A01561722
#   
#           DICCIONARIO CUADRUPLOS

from CuboSemantico import CuboSemantico


class cuadruplos:
    
    def __init__(self):
        self.cuadruplo = { }
        
    def add(self, iteracion, operador, termino1, termino2, asignar):  #AGREGA UN CUADRUPLO AL DICCIONARIO
        self.cuadruplo[iteracion] = {
                'operador': operador,
                'termino1': termino1,
                'termino2': termino2,
                'asignar': asignar
            }
    
    def search(self, iteracion):                #BUSCA UN CUADRUPLO Y LO IMPRIME
        if iteracion in self.cuadruplo:
            print(self.cuadruplo.get(iteracion))
        else:
            print("ERROR: QUADRUPLE DOES NOT EXIST")
    
    def updateCuad(self, iteracion, asignar):       #ACTUALIZA EL ULTIMO VALOR DE UN CUADRUPLO 
        if(self.cuadruplo.get(iteracion, None) == None):
            print('ERROR: ITERATION DOES NOT EXIST')
        else:
            self.cuadruplo[iteracion]['asignar']= asignar
    
    def print(self):                                #IMPRIME LOS CUADRUPLOS
        for key in self.cuadruplo:
            cuadList = list(self.cuadruplo[key].values())
            print(key, cuadList)

    def getValues(self):
        return self.cuadruplo
