#   Guillermo Enrique Valles Villegas
#   A01561722
#   
#           TABLA DE PARAMETROS
#   Tabla con diccionario para guardar los parametros que necesita la funcion
import sys


class tablaParametros:
   
    
    def __init__(self):
        self.parametros = { }
        
        
    def search(self, id):               # DEVUELVE TRUE OR FALSE SI LA VARIABLE EXISTE
        return id in self.parametros
    
    
    def add(self, typeExpected):            # AGREGA LA VARIABLE Y TIPO A LA TABLA
        self.parametros= {
            'type': typeExpected,
        }
        
        
    def print(self):                    # IMPRIME LA TABLA
        if(self.parametros != {}):
            print('PARAMETROS:')
            print(self.parametros)


# if __name__ == "__main__":
#     tablaPar = tablaParametros()
#     tablaPar.add('int')
#     tablaPar.add('float')
#     tablaPar.print()