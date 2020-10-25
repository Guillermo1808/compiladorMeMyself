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
    def addFunction(self, fid, type, parametersType, parametersId, FScope):
        if fid in self.funciones.keys():
            print('ERROR:', fid, 'module is already declared')
        else:
            self.funciones[fid] = {
                'type': type,
                'parameterId': parametersId,
                'parameterType': parametersType,
                'FScope': FScope,
                'variables': tablaVariables()
            }
        
        
        
    # AGREGA VARIABLES A LA TABLA
    def addVariable(self, fid, type, id):
        if(self.funciones[fid]['variables'].search(id)):
            print('ERROR:', id, 'variable is already declared')
        else:
            self.funciones[fid]['variables'].add(id, type, self.funciones[fid]['FScope'])
        
        
        
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
    tablaFun.addFunction('metodo', 'int', ['int', 'float', 'char'], ['uno', 'dos', 'tres'], 'global')
    tablaFun.addVariable('metodo', 'int', 'smigle')
    tablaFun.addVariable('metodo', 'char', 'memo')
    tablaFun.addVariable('metodo', 'float', 'lotr')
    
    tablaFun.addFunction('suma', 'int', ['int', 'float', 'char'], ['uno', 'dos', 'tres'], 'funsuma')
    tablaFun.addVariable('suma', 'int', 'smigle')
    tablaFun.addVariable('suma', 'char', 'memo')
    tablaFun.addVariable('suma', 'float', 'lotr')
    
    tablaFun.printFunction()
    
    # tablaFun.addFunction('sumar', 'int', ['int', 'float', 'char'], ['uno', 'dos', 'tres'])
    # tablaFun.addVariable('sumar', 'int', 'smigle')
    # tablaFun.addVariable('sumar', 'char', 'memo')
    # tablaFun.printFunction('sumar')
    
    # tablaFun.addFunction('sumar', 'int', ['int', 'float', 'char'], ['uno', 'dos', 'tres'])
