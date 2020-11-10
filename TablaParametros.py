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
    
    
    def add(self,parNum ,typeExpected):            # AGREGA LA VARIABLE Y TIPO A LA TABLA
        self.parametros[parNum]= {
            'type': typeExpected,
        }
        
        
    def print(self):                    # IMPRIME LA TABLA
        if(self.parametros != {}):
            print('PARAMETROS:')
            print(self.parametros)


# if __name__ == "__main__":
#     tablaPar = tablaParametros()
#     tablaPar.add(1,'int')
#     tablaPar.add(2,'float')
#     tablaPar.print()