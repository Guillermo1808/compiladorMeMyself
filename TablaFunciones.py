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
                    print('ERROR: VAR',id, 'NOT DECLARED')
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
                    return self.funciones[fid]['variables'].getDir(id)
        
    def getParType(self, fid, num):                 # DEVUELVE EL TYPE DE PARAMETRO          
        return self.funciones[fid]['parametros'].getType(num)
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
            exit()
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
        if(self.funciones[fid]['variables'].search(id)):
            if(fid != 'globales'):
                print('ERROR:', id, 'VARIABLE IS ALREADY DECLARED')
                exit()
        else:
            self.funciones[fid]['variables'].add(id, typeV, memory)
    
    # AGREGA ARREGLOS A LA TABLA
    def addArray(self, fid, id, typeV, memory, size, m1, m2, L1, L2):
        if(self.funciones[fid]['variables'].search(id)):
            if(fid != 'globales'):
                print('ERROR:', id, 'VARIABLE IS ALREADY DECLARED')
                exit()
        else:
            self.funciones[fid]['variables'].addArr(id, typeV, memory, size, m1, m2, L1, L2)
    
    def addParametros(self, fid, ParCont, typeP):
        self.funciones[fid]['parametros'].add(ParCont, typeP)
    
    def checkIfArray(self, fid, id):
        print('FID',fid)
        return self.funciones[fid]['variables'].checkArray(id)
    
    def getArrM(self, id, num):
        for fid in self.funciones.keys():
            if self.funciones[fid]['variables'].search(id):
                if(self.funciones[fid]['variables'].getDir(id) == None):
                    print('ERROR: VAR NOT FOUND')
                    exit()
                else:
                    return self.funciones[fid]['variables'].getM(id, num)
    
    def getArrL(self, id, num):
        for fid in self.funciones.keys():
            if self.funciones[fid]['variables'].search(id):
                if(self.funciones[fid]['variables'].getDir(id) == None):
                    print('ERROR: VAR NOT FOUND')
                    exit()
                else:
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
        resultado = self.funciones['globales']['variables'].initialValues()
        return resultado
    def getFunctionInitialValues(self,fid):
        return self.funciones[fid]['cantidad']

    
    def getGlobalVarsValues(self):        
        for keys in self.funciones:
            if(self.funciones[keys]['FScope'] == 'global'):
                resultado = self.funciones[keys]['variables'].initialValues()
        return resultado

