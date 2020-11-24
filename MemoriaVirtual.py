# Guillermo Enrique Valles Villegas
# A01561722
# Maquina Virtual

from TablaFunciones import tablaFunciones
from Cuadruplos import cuadruplos
import turtle
import sys

class MaquinaVirtual: 
    arrInt = []
    arrFloats = []
    arrChars = []
    arrTemps = []
    arrCtes = []
    
    functions = {}

    IntBaseF     = 11000
    FloatBaseF   = 16000
    CharsBaseF   = 19000
    TempsBaseF   = 21000
    
    IntBase     = 10000
    FloatBase   = 15000
    CharsBase   = 18000
    TempsBase   = 20000
    CtesBase    = 22000
    CurrentFunction = 0
    CurrentIteration = 1
    gosub = 0
    t = turtle.Turtle()
    isArray = False
    
    def __init__(self, cuadruplosD, funcionesD, cantTemps):
        self.cuadruplosF = cuadruplos()
        self.DirFunc = tablaFunciones()
        self.cuadruplosF = cuadruplosD
        self.DirFunc = funcionesD
        self.Quad = self.cuadruplosF.getValues()
        self.Temporales = cantTemps
        
    def initialFunctionValues(self, fid):
        valores = self.DirFunc.getFunctionInitialValues(fid)
        # print(valores)
        self.functions[self.CurrentFunction] = {
            0: [],
            1: [],
            2: [],
            3: []
        }
        for x in range(valores[0]):
            self.functions[self.CurrentFunction][0].append(0)
        for x in range(valores[1]):
            self.functions[self.CurrentFunction][1].append(0)
        for x in range(valores[2]):
            self.functions[self.CurrentFunction][2].append(0)
        for x in range(valores[3]):
            self.functions[self.CurrentFunction][3].append(0)
        # print(self.functions)
        
        
    def initialValues(self):
        print('---- INITIAL VALUES ----')
        valores = self.DirFunc.getInitialValues()
        # print(valores)
        for keys in valores:
            var = keys
            typeV = valores[keys]['typeV']
            if(typeV == 'int'):
                try:
                    var = int(var)
                except:
                    var = 0
                self.arrCtes.append(var)
            if(typeV == 'float'):
                try:
                    var = float(var)
                except:
                    var = 0
                self.arrCtes.append(var)
            if(typeV == 'char'):
                lenght = len(var)-1
                var = var[1:lenght]
                self.arrCtes.append(var)
            if(typeV == 'letrero'):
                lenght = len(var)-1
                var = var[1:lenght]
                self.arrCtes.append(var)
                
        # print(self.arrCtes)
        valoresVars = self.DirFunc.getGlobalVarsValues()
        # print(valoresVars)
        for keys in valoresVars:
            direccion = valoresVars[keys]['memory']
            if(direccion >= 10000 and direccion <= 11000):
                # print('int')
                if 'size' in valoresVars[keys].keys():
                    for x in range(valoresVars[keys]['size']):
                        self.arrInt.append(0)
                else:
                    self.arrInt.append(0)
            if(direccion >= 15000 and direccion <= 16000):
                # print('floats')
                self.arrFloats.append(0)
            if(direccion >= 18000 and direccion <= 19000):
                # print('chars')
                self.arrChars.append(0)
            # if(direccion >= 20000 and direccion <= 21000):
            #     print('temps')
            #     self.arrTemps[direccion-self.TempsBase] = 0
            # if(direccion >= 22000 and direccion <= 23999):
            #     print('ctes')
            #     self.arrCtes[direccion-self.CtesBase] = 0
        # print('INTS',self.arrInt, 'FLOATS',self.arrFloats, 'CHARS',self.arrChars)
        for i in range(self.Temporales):
            self.arrTemps.append(0)
        
        # print('TEMPS', self.arrTemps)
    
    def getValue(self,direccion):
        # print(direccion)
        if(type(direccion) == str):
            direccion = int(direccion)
            return direccion
        else:
            if(direccion >= 10000 and direccion < 11000):
                return self.arrInt[direccion-self.IntBase]
            if(direccion >= 15000 and direccion < 16000):
                return self.arrFloats[direccion-self.FloatBase]
            if(direccion >= 18000 and direccion < 19000):
                return self.arrChars[direccion-self.CharsBase]
            if(direccion >= 20000 and direccion < 21000):
                return self.arrTemps[direccion-self.TempsBase]
            if(direccion >= 22000 and direccion <= 23999):
                return self.arrCtes[direccion-self.CtesBase]
            
            if(direccion >= 11000 and direccion <= 14999):
                print('separadorrrrrr')
                print(self.CurrentIteration)
                print(direccion)
                print(self.IntBaseF)
                try:
                    return self.functions[self.CurrentFunction][0][direccion-self.IntBaseF]
                except:
                    return self.functions[self.CurrentFunction][0][direccion-self.IntBaseF-1]
                else:
                    return self.functions[self.CurrentFunction][0][direccion-self.IntBaseF]
            if(direccion >= 16000 and direccion <= 17999):
                return self.functions[self.CurrentFunction][1][direccion-self.FloatBaseF]
            if(direccion >= 19000 and direccion <= 19999):
                return self.functions[self.CurrentFunction][2][direccion-self.CharsBaseF]
            if(direccion >= 21000 and direccion <= 21999):
                return self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF]
            # if(direccion >= 20000 and direccion <= 21000):
            #     return self.arrTemps[direccion-self.TempsBase]
        
    def readQuadruples(self, iteration):
        # print('---- READ QUADS ----')
        # print(iteration,self.Quad[iteration])
        operador = self.Quad[iteration]['operador']
        terminoL = self.Quad[iteration]['termino1']
        terminoR = self.Quad[iteration]['termino2']
        asignar = self.Quad[iteration]['asignar']
        # print(operador,terminoL,terminoR,asignar)
        self.switch_case(operador, terminoL, terminoR, asignar)
    
    def assign(self, operador, terminoL, terminoR, asignar):
        # print('-----ASSIGN----', self.CurrentIteration)
        # print(operador, terminoL, terminoR, asignar)
        
        if(not self.isArray):
            terminoL = self.getValue(terminoL)
            if(asignar >= 10000 and asignar < 11000):
                self.arrInt[asignar-self.IntBase]= terminoL
            if(asignar >= 15000 and asignar < 16000):
                self.arrFloats[asignar-self.FloatBase]= terminoL
            if(asignar >= 18000 and asignar < 19000):
                self.arrChars[asignar-self.CharsBase]= terminoL
            if(asignar >= 20000 and asignar < 21000):
                self.arrTemps[asignar-self.TempsBase] = terminoL
            if(asignar >= 22000 and asignar < 23999):
                self.arrCtes[asignar-self.CtesBase] = terminoL
            
            if(asignar >= 11000 and asignar <= 14999):
                self.functions[self.CurrentFunction][0][asignar-self.IntBaseF] = terminoL
            if(asignar >= 16000 and asignar <= 17999):
                self.functions[self.CurrentFunction][1][asignar-self.FloatBaseF] = terminoL
            if(asignar >= 19000 and asignar <= 19999):
                self.functions[self.CurrentFunction][2][asignar-self.CharsBaseF] = terminoL
            if(asignar >= 21000 and asignar <= 21999):
                self.functions[self.CurrentFunction][3][asignar-self.TempsBaseF] = terminoL
        else:
            # print('ARRAY')
            # print(operador, terminoL, terminoR, asignar)
            aux = asignar
            aux = self.getValue(aux)
            aux = self.getValue(aux)
            # print(aux)
            if(aux == None):
                terminoL = self.getValue(terminoL)
                terminoL = self.getValue(terminoL)
            else:
                terminoL = self.getValue(terminoL)
                asignar = self.getValue(asignar)
            # print('terminoL', terminoL)
            # print('asignar', asignar)
            if(asignar >= 10000 and asignar < 11000):
                self.arrInt[asignar-self.IntBase]= terminoL
            if(asignar >= 15000 and asignar < 16000):
                self.arrFloats[asignar-self.FloatBase]= terminoL
            if(asignar >= 18000 and asignar < 19000):
                self.arrChars[asignar-self.CharsBase]= terminoL
            if(asignar >= 20000 and asignar < 21000):
                self.arrTemps[asignar-self.TempsBase] = terminoL
            if(asignar >= 22000 and asignar < 23999):
                self.arrCtes[asignar-self.CtesBase] = terminoL
            if(asignar >= 11000 and asignar <= 14999):
                self.functions[self.CurrentFunction][0][asignar-self.IntBaseF] = terminoL
            if(asignar >= 16000 and asignar <= 17999):
                self.functions[self.CurrentFunction][1][asignar-self.FloatBaseF] = terminoL
            if(asignar >= 19000 and asignar <= 19999):
                self.functions[self.CurrentFunction][2][asignar-self.CharsBaseF] = terminoL
            if(asignar >= 21000 and asignar <= 21999):
                self.functions[self.CurrentFunction][3][asignar-self.TempsBaseF] = terminoL
            # else:
            #     terminoL = self.getValue(terminoL)
            #     print('dir if 2', terminoL)
            #     if(asignar >= 10000 and asignar < 11000):
            #         self.arrInt[asignar-self.IntBase]= terminoL
            #     if(asignar >= 15000 and asignar < 16000):
            #         self.arrFloats[asignar-self.FloatBase]= terminoL
            #     if(asignar >= 18000 and asignar < 19000):
            #         self.arrChars[asignar-self.CharsBase]= terminoL
            #     if(asignar >= 20000 and asignar < 21000):
            #         self.arrTemps[asignar-self.TempsBase] = terminoL
            #     if(asignar >= 22000 and asignar < 23999):
            #         self.arrCtes[asignar-self.CtesBase] = terminoL
            #     if(asignar >= 11000 and asignar <= 14999):
            #         self.functions[self.CurrentFunction][0][asignar-self.IntBaseF] = terminoL
            #     if(asignar >= 16000 and asignar <= 17999):
            #         self.functions[self.CurrentFunction][1][asignar-self.FloatBaseF] = terminoL
            #     if(asignar >= 19000 and asignar <= 19999):
            #         self.functions[self.CurrentFunction][2][asignar-self.CharsBaseF] = terminoL
            #     if(asignar >= 21000 and asignar <= 21999):
            #         self.functions[self.CurrentFunction][3][asignar-self.TempsBaseF] = terminoL
            self.isArray = False
        self.CurrentIteration+=1
        # print(self.CurrentIteration)
        # print('ASSIGN END')
                
    def addition(self, operador, terminoL, terminoR, asignar):
        # print('ADDITION')
        terminoL = self.getValue(terminoL)
        terminoR = self.getValue(terminoR)
        # print('varlor L: ',terminoL,'varlor R: ',terminoR)
        if(asignar >= 10000 and asignar < 11000):
            self.arrInt[asignar-self.IntBase]= terminoL+terminoR
        if(asignar >= 15000 and asignar < 16000):
            self.arrFloats[asignar-self.FloatBase]= terminoL+terminoR
        if(asignar >= 20000 and asignar < 21000):
            self.arrTemps[asignar-self.TempsBase] = terminoL+terminoR
        
        if(asignar >= 11000 and asignar <= 14999):
            self.functions[self.CurrentFunction][0][asignar-self.IntBaseF] = terminoL+terminoR
        if(asignar >= 16000 and asignar <= 17999):
            self.functions[self.CurrentFunction][1][asignar-self.FloatBaseF] = terminoL+terminoR
        if(asignar >= 19000 and asignar <= 19999):
            self.functions[self.CurrentFunction][2][asignar-self.CharsBaseF] = terminoL+terminoR
        if(asignar >= 21000 and asignar <= 21999):
            self.functions[self.CurrentFunction][3][asignar-self.TempsBaseF] = terminoL+terminoR
            
        self.CurrentIteration+=1

        
    def substraction(self, operador, terminoL, terminoR, asignar):
        # print('SUBSTRACTION')
        terminoL = self.getValue(terminoL)
        terminoR = self.getValue(terminoR)
        # print('varlor L: ',terminoL,'varlor R: ',terminoR)
        if(asignar >= 10000 and asignar < 11000):
            self.arrInt[asignar-self.IntBase]= terminoL-terminoR
        if(asignar >= 15000 and asignar < 16000):
            self.arrFloats[asignar-self.FloatBase]= terminoL-terminoR
        if(asignar >= 20000 and asignar < 21000):
            self.arrTemps[asignar-self.TempsBase] = terminoL-terminoR
        
        if(asignar >= 11000 and asignar <= 14999):
            self.functions[self.CurrentFunction][0][asignar-self.IntBaseF] = terminoL-terminoR
        if(asignar >= 16000 and asignar <= 17999):
            self.functions[self.CurrentFunction][1][asignar-self.FloatBaseF] = terminoL-terminoR
        if(asignar >= 19000 and asignar <= 19999):
            self.functions[self.CurrentFunction][2][asignar-self.CharsBaseF] = terminoL-terminoR 
        if(asignar >= 21000 and asignar <= 21999):
            self.functions[self.CurrentFunction][3][asignar-self.TempsBaseF] = terminoL-terminoR
               
        self.CurrentIteration+=1
        
    def times(self, operador, terminoL, terminoR, asignar):
        # print('TIMES')
        
        terminoL = self.getValue(terminoL)
        terminoR = self.getValue(terminoR)
        # print('varlor L: ',terminoL,'varlor R: ',terminoR)
        if(asignar >= 10000 and asignar < 11000):
            self.arrInt[asignar-self.IntBase]= terminoL*terminoR
        if(asignar >= 15000 and asignar < 16000):
            self.arrFloats[asignar-self.FloatBase]= terminoL*terminoR
        if(asignar >= 20000 and asignar < 21000):
            self.arrTemps[asignar-self.TempsBase] = terminoL*terminoR
        
        if(asignar >= 11000 and asignar <= 14999):
            self.functions[self.CurrentFunction][0][asignar-self.IntBaseF] = terminoL*terminoR
        if(asignar >= 16000 and asignar <= 17999):
            self.functions[self.CurrentFunction][1][asignar-self.FloatBaseF] = terminoL*terminoR
        if(asignar >= 19000 and asignar <= 19999):
            self.functions[self.CurrentFunction][2][asignar-self.CharsBaseF] = terminoL*terminoR
        if(asignar >= 21000 and asignar <= 21999):
            self.functions[self.CurrentFunction][3][asignar-self.TempsBaseF] = terminoL*terminoR
              
        self.CurrentIteration+=1
        
        
    def divide(self, operador, terminoL, terminoR, asignar):
        # print('DIVIDE')
        terminoL = self.getValue(terminoL)
        terminoR = self.getValue(terminoR)
        # print('varlor L: ',terminoL,'varlor R: ',terminoR)
        if(asignar >= 10000 and asignar < 11000):
            self.arrInt[asignar-self.IntBase]= terminoL/terminoR
        if(asignar >= 15000 and asignar < 16000):
            self.arrFloats[asignar-self.FloatBase]= terminoL/terminoR
        if(asignar >= 20000 and asignar < 21000):
            self.arrTemps[asignar-self.TempsBase] = terminoL/terminoR
        
        if(asignar >= 11000 and asignar <= 14999):
            self.functions[self.CurrentFunction][0][asignar-self.IntBaseF] = terminoL/terminoR
        if(asignar >= 16000 and asignar <= 17999):
            self.functions[self.CurrentFunction][1][asignar-self.FloatBaseF] = terminoL/terminoR
        if(asignar >= 19000 and asignar <= 19999):
            self.functions[self.CurrentFunction][2][asignar-self.CharsBaseF] = terminoL/terminoR
        if(asignar >= 21000 and asignar <= 21999):
            self.functions[self.CurrentFunction][3][asignar-self.TempsBaseF] = terminoL/terminoR
                   
        self.CurrentIteration+=1
    
    def goto(self,asignar):
        # print('GOTO')
        self.CurrentIteration = asignar
        # print('CURRENT ITERATION:', self.CurrentIteration)
        # self.readQuadruples(asignar)
    
    def gotof(self,operador, terminoL, terminoR, asignar):
        # print('GOTOF')
        terminoL = self.getValue(terminoL)
        # print('valor', terminoL)
        
        if(terminoL != 1):
            self.CurrentIteration = asignar
        else:
            self.CurrentIteration+=1
    
    def write(self,asignar):
        # print('WRITE')

        if self.isArray:
            x = self.getValue(asignar)
            x = self.getValue(x)
            print(x)
        else:
            print(self.getValue(asignar))
        self.CurrentIteration+=1
    
    def read(self,operador, terminoL, terminoR, direccion):
        # print('READ')
        var = input()
        if(direccion >= 10000 and direccion < 11000):
            # print('int')
            var = int(var)
            self.arrInt[direccion-self.IntBase] = var
        if(direccion >= 15000 and direccion < 16000):
            # print('floats')
            var = float(var)
            self.arrFloats[direccion-self.FloatBase] = var
        if(direccion >= 18000 and direccion < 19000):
            # print('chars')
            self.arrChars[direccion-self.CharsBase] = var
        
        if(direccion >= 11000 and direccion <= 14999):
            self.functions[self.CurrentFunction][0][direccion-self.IntBaseF] = var
        if(direccion >= 16000 and direccion <= 17999):
            self.functions[self.CurrentFunction][1][direccion-self.FloatBaseF] = var
        if(direccion >= 19000 and direccion <= 19999):
            self.functions[self.CurrentFunction][2][direccion-self.CharsBaseF] = var
        self.CurrentIteration+=1
    
    def line(self, operador, terminoL, terminoR, asignar):
        terminoR = self.getValue(terminoR)
        asignar = self.getValue(asignar)
        self.t.goto(terminoR,asignar)
        self.CurrentIteration+=1
        
    def point(self, operador, terminoL, terminoR, asignar):
        self.t.dot(5)
        self.CurrentIteration+=1
        
    def circle(self, operador, terminoL, terminoR, asignar):
        asignar = self.getValue(asignar)
        self.t.circle(asignar)
        self.CurrentIteration+=1
    
    def arc(self, operador, terminoL, terminoR, asignar):
        asignar = self.getValue(asignar)
        self.t.circle(asignar, 180)
        self.CurrentIteration+=1
    
    def penup(self,operador, terminoL, terminoR, asignar):
        self.t.penup()
        self.CurrentIteration+=1
        
    def pendown(self,operador, terminoL, terminoR, asignar):
        self.t.pendown()
        self.CurrentIteration+=1 
    
    def color(self,operador, terminoL, terminoR, asignar):
        asignar = self.getValue(asignar)
        terminoR = self.getValue(terminoR)
        terminoL = self.getValue(terminoL)
        self.t.screen.colormode(255)
        self.t.color(terminoL,terminoR,asignar)
        self.CurrentIteration+=1
    
    def size(self,operador, terminoL, terminoR, asignar):
        asignar = self.getValue(asignar)
        self.t.pensize(asignar)
        self.CurrentIteration+=1
    
    def clear(self,operador, terminoL, terminoR, asignar):
        self.t.clear()
        self.CurrentIteration+=1
    
    def equal(self,operador, terminoL, terminoR, direccion):
        # print('EQUAL')
        valorL = self.getValue(terminoL)
        valorR = self.getValue(terminoR)
        if(valorL == valorR):
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 1
            else:
                self.arrTemps[direccion-self.TempsBase] = 1
        else:
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 2
            else:
                self.arrTemps[direccion-self.TempsBase] = 2
        self.CurrentIteration+=1
    
    def different(self,operador, terminoL, terminoR, direccion):
        # print('EQUAL')
        valorL = self.getValue(terminoL)
        valorR = self.getValue(terminoR)
        if(valorL != valorR):
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 1
            else:
                self.arrTemps[direccion-self.TempsBase] = 1
        else:
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 2
            else:
                self.arrTemps[direccion-self.TempsBase] = 2
        self.CurrentIteration+=1
        
    def lte(self,operador, terminoL, terminoR, direccion):
        # print('EQUAL')
        valorL = self.getValue(terminoL)
        valorR = self.getValue(terminoR)
        if(valorL <= valorR):
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 1
            else:
                self.arrTemps[direccion-self.TempsBase] = 1
        else:
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 2
            else:
                self.arrTemps[direccion-self.TempsBase] = 2
        self.CurrentIteration+=1
     
    def lt(self,operador, terminoL, terminoR, direccion):
        # print('ENTRA LT')
        valorL = self.getValue(terminoL)
        # print(terminoR)
        valorR = self.getValue(terminoR)
        # print(valorR,valorL)
        # print('comparacion ',valorL, valorR)
        # print('valorL',valorL,'valorR', valorR)
        if(valorL < valorR):
            # print(direccion)
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 1
            else:
                self.arrTemps[direccion-self.TempsBase] = 1
        else:
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 2
            else:
                self.arrTemps[direccion-self.TempsBase] = 2
        self.CurrentIteration+=1
        # print('SALE LT')
    
    def gte(self,operador, terminoL, terminoR, direccion):
        # print('EQUAL')
        valorL = self.getValue(terminoL)
        valorR = self.getValue(terminoR)
        if(valorL >= valorR):
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 1
            else:
                self.arrTemps[direccion-self.TempsBase] = 1
        else:
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 2
            else:
                self.arrTemps[direccion-self.TempsBase] = 2
        self.CurrentIteration+=1
    
    def gt(self,operador, terminoL, terminoR, direccion):
        # print('EQUAL')
        # print('valorL', terminoL)
        valorL = self.getValue(terminoL)
        # print('valorR', terminoR)
        valorR = self.getValue(terminoR)
        if(valorL > valorR):
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 1
            else:
                self.arrTemps[direccion-self.TempsBase] = 1
        else:
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 2
            else:
                 self.arrTemps[direccion-self.TempsBase] = 2
        self.CurrentIteration+=1
    
    def andF(self,operador, terminoL, terminoR, direccion):
        # print('EQUAL')
        valorL = self.getValue(terminoL)
        valorR = self.getValue(terminoR)
        if(valorL == 1 and valorR == 1):
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 1
            else:
                self.arrTemps[direccion-self.TempsBase] = 1
        else:
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 2
            else:
                 self.arrTemps[direccion-self.TempsBase] = 2
        self.CurrentIteration+=1
    
    def orF(self,operador, terminoL, terminoR, direccion):
        # print('EQUAL')
        valorL = self.getValue(terminoL)
        valorR = self.getValue(terminoR)
        if(valorL == 1 or valorR == 1):
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 1
            else:
                self.arrTemps[direccion-self.TempsBase] = 1
        else:
            if direccion >= 21000:
                self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = 2
            else:
                self.arrTemps[direccion-self.TempsBase] = 2
        self.CurrentIteration+=1
    
    def eraF(self,operador, terminoL, terminoR, direccion):
        self.CurrentFunction +=1
        # print('ERA')
        self.initialFunctionValues(direccion)
        self.CurrentIteration+=1
    
    def paramF(self,operador, terminoL, terminoR, direccion):
        asignar = terminoL
        terminoL = self.getValue(terminoL)
        # print(asignar, terminoL)
        if(asignar >= 10000 and asignar < 11000):
            self.functions[self.CurrentFunction][0][terminoR-1] = terminoL
        if(asignar >= 15000 and asignar < 16000):
            self.functions[self.CurrentFunction][1][terminoR-1] = terminoL
        if(asignar >= 18000 and asignar < 19000):
            self.functions[self.CurrentFunction][2][terminoR-1] = terminoL
        if(asignar >= 20000 and asignar < 21000):
            self.functions[self.CurrentFunction][3][terminoR-1] = terminoL
        if(asignar >= 22000 and asignar < 23999):
            self.functions[self.CurrentFunction][4][terminoR-1] = terminoL
        
        if(asignar >= 11000 and asignar <= 14999):
            self.functions[self.CurrentFunction][0][[terminoR-1]] = terminoL
        if(asignar >= 16000 and asignar <= 17999):
            self.functions[self.CurrentFunction][1][terminoR-1] = terminoL
        if(asignar >= 19000 and asignar <= 19999):
            self.functions[self.CurrentFunction][2][terminoR-1] = terminoL
        if(asignar >= 21000 and asignar <= 21999):
            self.functions[self.CurrentFunction][3][terminoR-1] = terminoL
        self.CurrentIteration+=1
        
    def gosubF(self,operador, terminoL, terminoR, direccion):
        # print('EQUAL')
        # print(self.arrInt)
        self.gosub = self.CurrentIteration
        self.CurrentIteration = direccion

    def endF(self,operador, terminoL, terminoR, direccion):
        # print('EQUAL')
        self.CurrentIteration = self.gosub
        self.currentFunction = 0
        self.CurrentIteration+=1
    
    def verify(self,operador, terminoL, terminoR, direccion):

        terminoL = self.getValue(terminoL)
        # print(self.arrInt)
        if(terminoL < direccion and terminoL >= terminoR):
            self.CurrentIteration+=1
        else:
            print('ERROR: ARRAY INDEX OUT OF BOUNDS')
            print(terminoL)
            exit()
    
    def memoria(self,operador, terminoL, terminoR, direccion):
        terminoL = self.getValue(terminoL)
        result = terminoR + terminoL
        if direccion >= 21000:
            self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = result
        else:
            self.arrTemps[direccion-self.TempsBase] = result
        self.isArray = True
        self.CurrentIteration+=1
        
    def memoria2(self,operador, terminoL, terminoR, direccion):
        
        terminoL = self.getValue(terminoL)
        terminoR = self.getValue(terminoR)
  
        
        result = terminoL + terminoR

        if direccion >= 21000:
            self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = result
        else:
            self.arrTemps[direccion-self.TempsBase] = result
        self.isArray = True
        self.CurrentIteration+=1
        
        
    def timesm(self,operador, terminoL, terminoR, direccion):
        terminoL = self.getValue(terminoL)
        result = terminoL*terminoR
        if(direccion >= 21000 and direccion <= 21999):
            self.functions[self.CurrentFunction][3][direccion-self.TempsBaseF] = result
        if(direccion >= 20000 and direccion < 21000):
            self.arrTemps[direccion-self.TempsBase] = result
        self.CurrentIteration+=1

    def switch_case(self, operador, terminoL, terminoR, asignar):
        cases = {
            'GOTO': lambda: self.goto(asignar),
            'GOTOF': lambda: self.gotof(operador, terminoL, terminoR, asignar),
            'WRITE': lambda: self.write(asignar),
            'READ': lambda: self.read(operador,terminoL,terminoR,asignar),
            '=': lambda: self.assign(operador,terminoL,terminoR,asignar),
            '+': lambda: self.addition(operador,terminoL,terminoR,asignar),
            '+T': lambda: self.memoria(operador,terminoL,terminoR,asignar),
            '+T2': lambda: self.memoria2(operador,terminoL,terminoR,asignar),
            '-': lambda: self.substraction(operador,terminoL,terminoR,asignar),
            '*': lambda: self.times(operador,terminoL,terminoR,asignar),
            '*T': lambda: self.timesm(operador,terminoL,terminoR,asignar),
            '/': lambda: self.divide(operador,terminoL,terminoR,asignar),
            'LINE': lambda: self.line(operador,terminoL,terminoR,asignar),
            'POINT': lambda: self.point(operador,terminoL,terminoR,asignar),
            'CIRCLE': lambda: self.circle(operador,terminoL,terminoR,asignar),
            'ARC': lambda: self.arc(operador,terminoL,terminoR,asignar),
            'PENUP': lambda: self.penup(operador,terminoL,terminoR,asignar),
            'PENDOWN': lambda: self.pendown(operador,terminoL,terminoR,asignar),
            'COLOR': lambda: self.color(operador,terminoL,terminoR,asignar),
            'SIZE': lambda: self.size(operador,terminoL,terminoR,asignar),
            'CLEAR': lambda: self.clear(operador,terminoL,terminoR,asignar),
            '!=': lambda: self.different(operador,terminoL,terminoR,asignar),
            '==': lambda: self.equal(operador,terminoL,terminoR,asignar),
            '<=': lambda: self.lte(operador,terminoL,terminoR,asignar),
            '>=': lambda: self.gte(operador,terminoL,terminoR,asignar),
            '<': lambda: self.lt(operador,terminoL,terminoR,asignar),
            '>': lambda: self.gt(operador,terminoL,terminoR,asignar),
            '&': lambda: self.andF(operador,terminoL,terminoR,asignar),
            '|': lambda: self.orF(operador,terminoL,terminoR,asignar),
            'ERA': lambda: self.eraF(operador,terminoL,terminoR,asignar),
            'PARAM': lambda: self.paramF(operador,terminoL,terminoR,asignar),
            'GOSUB': lambda: self.gosubF(operador,terminoL,terminoR,asignar),
            'END': lambda: self.endF(operador,terminoL,terminoR,asignar),
            'VERIFY': lambda: self.verify(operador,terminoL,terminoR,asignar),
        }
        cases.get(operador, lambda: print("Didn't match a case:"))()
                
    def main(self):
        turtle.title("Compiler MeMyself")
        self.t.getscreen()
        
            
        self.initialValues()
        print('CONSTANTES:', self.arrCtes)
        size = len(self.Quad)
        # print('--- size -----',size) 
        print('START READING QUADRUPLES')
        while(self.CurrentIteration <= size):
            # print('iteracion:',self.CurrentIteration)
            # print(self.CurrentIteration)
            # print(self.arrTemps)
            # print(self.functions)
            self.readQuadruples(self.CurrentIteration)
        print(self.arrInt)
        print(len(self.arrInt))
        # print(self.functions)
        # print('int',self.arrInt)
        # print('float',self.arrFloats)
        # print('temps',self.arrTemps)
        # print('ctes',self.arrCtes)
        turtle.done()