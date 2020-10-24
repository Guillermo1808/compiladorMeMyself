#   Guillermo Enrique Valles Villegas
#   A01561722
#   
#           TABLA DE FUNCIONES
#   Tabla con diccionario para guardar las variables del programa

from TablaVariables import tablaVariables
import sys

class tablaFunciones:
    def __init__(self):
        self.funciones = { }
        
    # DEVUELVE TRUE OR FALSE SI LA VARIABLE EXISTE
    def search(self, fid):              
        return fid in self.funciones
    
    # AGREGA LA FUNCION Y CREA SU TABLA
    def addFunction(self, fid, type, parametersType, parametersId):
        if fid in self.funciones.keys():
            print('ERROR:', fid, 'module is already declared')
        else:
            self.funciones[fid] = {
                'type': type,
                'parameterId': parametersId,
                'parameterType': parametersType,
                'variables': tablaVariables()
            }
        
    # AGREGA VARIABLES A LA TABLA
    def addVariable(self, fid, type, id):
        if(self.funciones[fid]['variables'].search(id)):
            print('ERROR:', id, 'variable is already declared')
        else:
            self.funciones[fid]['variables'].add(id, type)
        
    # IMPRIME LA TABLA DE FUNCIONES
    def printFunction(self):                    
        for fid in self.funciones:
            print('METOD ',fid, self.funciones[fid])
            
    # IMPRIME LA TABLA VARIABLES DE FUNCION
    def printFunctionVars(self, fid):                    
        for id in self.funciones:
            self.funciones[fid]['variables'].print()


if __name__ == "__main__":
    tablaFun = tablaFunciones()
    tablaFun.addFunction('metodo', 'int', ['int', 'float', 'char'], ['uno', 'dos', 'tres'])
    tablaFun.addVariable('metodo', 'int', 'smigle')
    tablaFun.addVariable('metodo', 'char', 'memo')
    tablaFun.addVariable('metodo', 'float', 'lotr')
    tablaFun.printFunction()
    
    # tablaFun.addFunction('sumar', 'int', ['int', 'float', 'char'], ['uno', 'dos', 'tres'])
    # tablaFun.addVariable('sumar', 'int', 'smigle')
    # tablaFun.addVariable('sumar', 'char', 'memo')
    # tablaFun.printFunction('sumar')
    
    # tablaFun.addFunction('sumar', 'int', ['int', 'float', 'char'], ['uno', 'dos', 'tres'])
