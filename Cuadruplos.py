#   Guillermo Enrique Valles Villegas
#   A01561722
#   
#           DICCIONARIO CUADRUPLOS

from CuboSemantico import CuboSemantico


class cuadruplos:
    
    def __init__(self):
        self.cuadruplo = { }
        
    def add(self, iteracion, operador, termino1, termino2, asignar):
        self.cuadruplo[iteracion] = {
                'operador': operador,
                'termino1': termino1,
                'termino2': termino2,
                'asignar': asignar
            }
        # # FUNCION UTILIZANDO EL CUBO SEMANTICO PARA VERIFICACION
        # cubo = CuboSemantico()
        # if(cubo.obtenerTipo(termino1, termino2, operador) != 'error'):
        #     self.cuadruplo[iteracion] = {
        #         'operador': operador,
        #         'termino1': termino1,
        #         'termino2': termino2,
        #         'asignar': asignar
        #     }
        # else:
        #     print('ERROR: TYPE MISSMATCH WITH', termino1, 'AND', termino2)
    
    def search(self, iteracion):
        print(self.cuadruplo.get(iteracion))
    
    def updateCuad(self, iteracion, operador, termino1, termino2, asignar):
        if(self.cuadruplo.get(iteracion, None) == None):
            print('ERROR THAT ITERATION DOES NOT EXIST')
        # else:
        #     print(self.cuadruplo[iteracion])
        #     self.cuadruplo['operador'] = operador
        #     self.cuadruplo['termino1'] = termino1
        #     self.cuadruplo['termino2'] = termino2
        #     self.cuadruplo['asignar']= asignar
        #     print(self.cuadruplo[iteracion])
    
    def print(self):
        for key in self.cuadruplo:
            cuadList = list(self.cuadruplo[key].values())
            print(key, cuadList)
        # print(self.cuadruplo.pop(1))
        # for key in self.cuadruplo:
        #     print(key)

if __name__ == "__main__":
    cuadruplo = cuadruplos()
    cuadruplo.add(1, '+', 'int', 'int', 't1')
    cuadruplo.add(2, 'GOTO', 0, 0, '_')
    cuadruplo.add(3, '*', 't2', 'd', 't3')
    cuadruplo.add(4, '/', 't3', 'e', 't4')
    cuadruplo.add(5, 'print', 0, 0, 't4')
    cuadruplo.print()
    print('---------')
    cuadruplo.updateCuad(2,'GOTO', 0, 0, 5)
    cuadruplo.print()
    print('---------')
    cuadruplo.updateCuad(7,'print', 0, 0, 't4')
    
    