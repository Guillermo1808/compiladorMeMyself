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
                                                
    def search(self, fid):              # DEVUELVE TRUE OR FALSE SI LA VARIABLE EXISTE
        return fid in self.funciones
                                        
    def getVarType(self, id):                 # DEVUELVE EL TYPE DE LA VARIABLE          
        for fid in self.funciones.keys():
            if self.funciones[fid]['variables'].search(id):
                if(self.funciones[fid]['variables'].getType(id) == None):
                    print('ERROR: VAR NOT FOUND')
                    exit()
                else:
                    return self.funciones[fid]['variables'].getType(id)
            #     return self.funciones[fid]['variables'].getType(id)
            
    def getVarDir(self, id):                # DEVUELVE EL TYPE DE LA VARIABLE    
        for fid in self.funciones.keys():
            if self.funciones[fid]['variables'].search(id):
                if(self.funciones[fid]['variables'].getDir(id) == None):
                    print('ERROR: VAR NOT FOUND')
                    exit()
                else:
                    # print(id,'DIR:',self.funciones[fid]['variables'].getDir(id))
                    return self.funciones[fid]['variables'].getDir(id)
        # for fid in self.funciones.keys():
        #     if self.funciones[fid]['variables'].search(id):
        #         return self.funciones[fid]['variables'].getDir(id)
            #     return self.funciones[fid]['variables'].getType(id)
        
    def getParType(self, fid, num):                 # DEVUELVE EL TYPE DE PARAMETRO          
        return self.funciones[fid]['parametros'].getType(num)
            #     return self.funciones[fid]['variables'].getType(id)
    def getParCount(self, fid):
        if(fid in self.funciones.keys()):
            count = self.funciones[fid]['parametros'].numPar()
            if count > 0:
                return count
            
    def getJump(self, fid):
        if(fid in self.funciones.keys()):
            return self.funciones[fid]['QuadCont']

    # AGREGA LA FUNCION Y CREA SU TABLA
    def addFunction(self, fid, typeF, FScope, QuadCont):
        if fid in self.funciones.keys():
            print('ERROR:', fid, 'module is already declared')
        else:
            self.funciones[fid] = {
                'type': typeF,
                'FScope': FScope,
                'QuadCont': QuadCont,
                'variables': tablaVariables(),
                'parametros': tablaParametros(),
                'cantidad':[]
            }
    def addVarCant(self,fid, ints,floats, chars, temps):
        self.funciones[fid]['cantidad'].append(ints)
        self.funciones[fid]['cantidad'].append(floats)
        self.funciones[fid]['cantidad'].append(chars)
        self.funciones[fid]['cantidad'].append(temps)
       

    
    # AGREGA VARIABLES A LA TABLA
    def searchVar(self, fid, id):
        return self.funciones[fid]['variables'].search(id)
        
        
    # AGREGA VARIABLES A LA TABLA
    def addVariable(self, fid, id, typeV, memory):
        #print('fid', fid, 'id',id,'type', typeV,'memory', memory)
        if(self.funciones[fid]['variables'].search(id)):
            if(fid != 'globales'):
                print('ERROR:', id, 'VARIABLE IS ALREADY DECLARED')
                exit()
        else:
            self.funciones[fid]['variables'].add(id, typeV, memory)
    
    # AGREGA ARREGLOS A LA TABLA
    def addArray(self, fid, id, typeV, memory, size, m1, m2, L1, L2):
        #print('fid', fid, 'id',id,'type', typeV,'memory', memory)
        if(self.funciones[fid]['variables'].search(id)):
            if(fid != 'globales'):
                print('ERROR:', id, 'VARIABLE IS ALREADY DECLARED')
                exit()
        else:
            self.funciones[fid]['variables'].addArr(id, typeV, memory, size, m1, m2, L1, L2)
    
    def addParametros(self, fid, ParCont, typeP):
        self.funciones[fid]['parametros'].add(ParCont, typeP)
    
    def checkIfArray(self, fid, id):
        return self.funciones[fid]['variables'].checkArray(id)
    
    def getArrM(self, id, num):
        for fid in self.funciones.keys():
            if self.funciones[fid]['variables'].search(id):
                if(self.funciones[fid]['variables'].getDir(id) == None):
                    print('ERROR: VAR NOT FOUND')
                    exit()
                else:
                    # print(id,'DIR:',self.funciones[fid]['variables'].getDir(id))
                    return self.funciones[fid]['variables'].getM(id, num)
    
    def getArrL(self, id, num):
        for fid in self.funciones.keys():
            if self.funciones[fid]['variables'].search(id):
                if(self.funciones[fid]['variables'].getDir(id) == None):
                    print('ERROR: VAR NOT FOUND')
                    exit()
                else:
                    # print(id,'DIR:',self.funciones[fid]['variables'].getDir(id))
                    return self.funciones[fid]['variables'].getLim(id, num)
        
        
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
    
    def getInitialValues(self):
        # self.funciones['globales']['variables'].print()
        resultado = self.funciones['globales']['variables'].initialValues()
        # print(type(resultado))
        return resultado
    def getFunctionInitialValues(self,fid):
        # self.funciones['globales']['variables'].print()
        return self.funciones[fid]['cantidad']

        # print(type(resultado))
        
    
    def getGlobalVarsValues(self):
        # self.funciones['globales']['variables'].print()
        
        for keys in self.funciones:
            if(self.funciones[keys]['FScope'] == 'global'):
                resultado = self.funciones[keys]['variables'].initialValues()
        # print(type(resultado))
        return resultado

# if __name__ == "__main__":
#     tablaFun = tablaFunciones()
#     tablaFun.addFunction('metodo', 'int', 'global')
#     # tablaFun.addParametros('metodo', 'int')
#     # tablaFun.addParametros('metodo', 'char')
#     # tablaFun.printFunction()
#     tablaFun.addFunction('suma', 'int', 'funsuma')
#     tablaFun.addVariable('suma', 'smigle', 'char', 100)
#     tablaFun.addVariable('suma', 'memo', 'char', 101)
#     print(tablaFun.search('suma'))
#     x = tablaFun.getVarType('memo')
#     print(x)
# #     tablaFun.addVariable('suma', 'float', 'lotr')
    
#     tablaFun.printFunction()
    
    # tablaFun.addFunction('sumar', 'int', ['int', 'float', 'char'], ['uno', 'dos', 'tres'])
    # tablaFun.addVariable('sumar', 'int', 'smigle')
    # tablaFun.addVariable('sumar', 'char', 'memo')
    # tablaFun.printFunction('sumar')
    
    # tablaFun.addFunction('sumar', 'int', ['int', 'float', 'char'], ['uno', 'dos', 'tres'])
