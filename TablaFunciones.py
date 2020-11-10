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
    
    def getVarType(self, id):
        for fid in self.funciones.keys():
            if self.funciones[fid]['variables'].search(id):
                return self.funciones[fid]['variables'].getType(id)
            #     return self.funciones[fid]['variables'].getType(id)
    
    
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
            print('ERROR:', id, 'VARIABLE IS ALREADY DECLARED')
            exit()
        else:
            self.funciones[fid]['variables'].add(id, typeV, memory)
    
    def addParametros(self, fid, ParCont, typeP):
        self.funciones[fid]['parametros'].add(ParCont, typeP)
        
        
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
    
    def deleteFunction(self, fid):
        self.funciones[fid]['variables'] = {}
        

# if __name__ == "__main__":
#     tablaFun = tablaFunciones()
#     tablaFun.addFunction('metodo', 'int', 'global')
#     # tablaFun.addParametros('metodo', 'int')
#     # tablaFun.addParametros('metodo', 'char')
#     # tablaFun.printFunction()
#     tablaFun.addFunction('suma', 'int', 'funsuma')
#     tablaFun.addVariable('suma', 'smigle', 'char', 100)
#     tablaFun.addVariable('suma', 'memo', 'char', 101)
#     x = tablaFun.getVarType('memo')
#     print(x)
# #     tablaFun.addVariable('suma', 'float', 'lotr')
    
#     tablaFun.printFunction()
    
    # tablaFun.addFunction('sumar', 'int', ['int', 'float', 'char'], ['uno', 'dos', 'tres'])
    # tablaFun.addVariable('sumar', 'int', 'smigle')
    # tablaFun.addVariable('sumar', 'char', 'memo')
    # tablaFun.printFunction('sumar')
    
    # tablaFun.addFunction('sumar', 'int', ['int', 'float', 'char'], ['uno', 'dos', 'tres'])
