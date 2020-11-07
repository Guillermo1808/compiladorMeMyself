#   Guillermo Enrique Valles Villegas
#   A01561722
#   
#           TABLA DE FUNCIONES
#   Tabla con diccionario para guardar las variables del programa

from TablaVariables import tablaVariables
from TablaParametros import tablaParametros
import sys



class tablaFunciones:
    def __init__(self):
        self.funciones = { }
        
        
        
    # DEVUELVE TRUE OR FALSE SI LA VARIABLE EXISTE
    def search(self, fid):              
        return fid in self.funciones
    
    
    
    # AGREGA LA FUNCION Y CREA SU TABLA
    def addFunction(self, fid, typeF, FScope):
        if fid in self.funciones.keys():
            print('ERROR:', fid, 'module is already declared')
        else:
            self.funciones[fid] = {
                'type': typeF,
                'FScope': FScope,
                'variables': tablaVariables(),
                'parametros': tablaParametros()
            }
        
        
        
    # AGREGA VARIABLES A LA TABLA
    def addVariable(self, fid, id, typeV, memory):
        #print('fid', fid, 'id',id,'type', typeV,'memory', memory)
        if(self.funciones[fid]['variables'].search(id)):
            print('ERROR:', id, 'variable is already declared')
        else:
            self.funciones[fid]['variables'].add(id, typeV, memory)
    
    def addParametros(self, fid, typeP):
        self.funciones[fid]['parametros'].add(typeP)
        
        
    # IMPRIME LA TABLA DE FUNCIONES
    def printFunction(self):
        print('------ FUNCIONES -----')               
        for fid in self.funciones:
            print('-----------')
            print('MODULE',fid, self.funciones[fid])
            self.funciones[fid]['variables'].print()
            self.funciones[fid]['parametros'].print()
            print('-----------')
        print('----------------------') 
        

# if __name__ == "__main__":
#     tablaFun = tablaFunciones()
#     tablaFun.addFunction('metodo', 'int', 'global')
#     tablaFun.addVariable('metodo', 'int', 'smigle')
#     tablaFun.addVariable('metodo', 'char', 'memo')
#     tablaFun.addVariable('metodo', 'float', 'lotr')
    
#     tablaFun.addFunction('suma', 'int', 'funsuma')
#     tablaFun.addVariable('suma', 'int', 'smigle')
#     tablaFun.addVariable('suma', 'char', 'memo')
#     tablaFun.addVariable('suma', 'float', 'lotr')
    
#     tablaFun.printFunction()
    
    # tablaFun.addFunction('sumar', 'int', ['int', 'float', 'char'], ['uno', 'dos', 'tres'])
    # tablaFun.addVariable('sumar', 'int', 'smigle')
    # tablaFun.addVariable('sumar', 'char', 'memo')
    # tablaFun.printFunction('sumar')
    
    # tablaFun.addFunction('sumar', 'int', ['int', 'float', 'char'], ['uno', 'dos', 'tres'])
