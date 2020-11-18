# Guillermo Enrique Valles Villegas
# A01561722
# Maquina Virtual

from TablaFunciones import tablaFunciones
from Cuadruplos import cuadruplos
from Stacks import stacks
import turtle
import sys

class MaquinaVirtual: 
    arrInt = []
    arrFloats = []
    arrChars = []
    arrTemps = []
    arrCtes = []
    IntBase     = 10000
    FloatBase   = 15000
    CharsBase   = 18000
    TempsBase   = 20000
    CtesBase    = 22000
    CurrentIteration = 1
    t = turtle.Turtle()
    
    def __init__(self, cuadruplosD, funcionesD, cantTemps):
        self.cuadruplosF = cuadruplos()
        self.DirFunc = tablaFunciones()
        self.cuadruplosF = cuadruplosD
        self.DirFunc = funcionesD
        self.Quad = self.cuadruplosF.getValues()
        self.Temporales = cantTemps
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
        # print(self.arrCtes)
        valoresVars = self.DirFunc.getGlobalVarsValues()
        # print(valoresVars)
        for keys in valoresVars:
            direccion = valoresVars[keys]['memory']
            if(direccion >= 10000 and direccion <= 14999):
                # print('int')
                self.arrInt.append(0)
            if(direccion >= 15000 and direccion <= 17999):
                # print('floats')
                self.arrFloats.append(0)
            if(direccion >= 18000 and direccion <= 19999):
                # print('chars')
                self.arrChars.append(0)
            # if(direccion >= 20000 and direccion <= 21999):
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
        if(direccion >= 10000 and direccion <= 14999):
            return self.arrInt[direccion-self.IntBase]
        if(direccion >= 15000 and direccion <= 17999):
            return self.arrFloats[direccion-self.FloatBase]
        if(direccion >= 18000 and direccion <= 19999):
            return self.arrChars[direccion-self.CharsBase]
        if(direccion >= 20000 and direccion <= 21999):
            return self.arrTemps[direccion-self.TempsBase]
        if(direccion >= 22000 and direccion <= 23999):
            return self.arrCtes[direccion-self.CtesBase]
        
    def readQuadruples(self, iteration):
        # print('---- READ QUADS ----')
        # print(self.Quad[iteration])
        operador = self.Quad[iteration]['operador']
        terminoL = self.Quad[iteration]['termino1']
        terminoR = self.Quad[iteration]['termino2']
        asignar = self.Quad[iteration]['asignar']
        # print(operador,terminoL,terminoR,asignar)
        self.switch_case(operador, terminoL, terminoR, asignar)
    
    def assign(self, operador, terminoL, terminoR, asignar):
        # print('ASSIGN')
        terminoL = self.getValue(terminoL)
        if(asignar >= 10000 and asignar <= 14999):
            self.arrInt[asignar-self.IntBase]= terminoL
        if(asignar >= 15000 and asignar <= 17999):
            self.arrFloats[asignar-self.FloatBase]= terminoL
        if(asignar >= 18000 and asignar <= 19999):
            self.arrChars[asignar-self.CharsBase]= terminoL
        if(asignar >= 20000 and asignar <= 21999):
            self.arrTemps[asignar-self.TempsBase] = terminoL
            
        self.CurrentIteration+=1
                
    def addition(self, operador, terminoL, terminoR, asignar):
        # print('ADDITION')
        terminoL = self.getValue(terminoL)
        terminoR = self.getValue(terminoR)
        # print('varlor L: ',terminoL,'varlor R: ',terminoR)
        if(asignar >= 10000 and asignar <= 14999):
            self.arrInt[asignar-self.IntBase]= terminoL+terminoR
        if(asignar >= 15000 and asignar <= 17999):
            self.arrFloats[asignar-self.FloatBase]= terminoL+terminoR
        if(asignar >= 20000 and asignar <= 21999):
            self.arrTemps[asignar-self.TempsBase] = terminoL+terminoR
            
        self.CurrentIteration+=1

        
    def substraction(self, operador, terminoL, terminoR, asignar):
        # print('SUBSTRACTION')
        terminoL = self.getValue(terminoL)
        terminoR = self.getValue(terminoR)
        # print('varlor L: ',terminoL,'varlor R: ',terminoR)
        if(asignar >= 10000 and asignar <= 14999):
            self.arrInt[asignar-self.IntBase]= terminoL-terminoR
        if(asignar >= 15000 and asignar <= 17999):
            self.arrFloats[asignar-self.FloatBase]= terminoL-terminoR
        if(asignar >= 20000 and asignar <= 21999):
            self.arrTemps[asignar-self.TempsBase] = terminoL-terminoR 
               
        self.CurrentIteration+=1
        
    def times(self, operador, terminoL, terminoR, asignar):
        # print('TIMES')
        terminoL = self.getValue(terminoL)
        terminoR = self.getValue(terminoR)
        # print('varlor L: ',terminoL,'varlor R: ',terminoR)
        if(asignar >= 10000 and asignar <= 14999):
            self.arrInt[asignar-self.IntBase]= terminoL*terminoR
        if(asignar >= 15000 and asignar <= 17999):
            self.arrFloats[asignar-self.FloatBase]= terminoL*terminoR
        if(asignar >= 20000 and asignar <= 21999):
            self.arrTemps[asignar-self.TempsBase] = terminoL*terminoR
                
        self.CurrentIteration+=1
        
        
    def divide(self, operador, terminoL, terminoR, asignar):
        # print('DIVIDE')
        terminoL = self.getValue(terminoL)
        terminoR = self.getValue(terminoR)
        # print('varlor L: ',terminoL,'varlor R: ',terminoR)
        if(asignar >= 10000 and asignar <= 14999):
            self.arrInt[asignar-self.IntBase]= terminoL/terminoR
        if(asignar >= 15000 and asignar <= 17999):
            self.arrFloats[asignar-self.FloatBase]= terminoL/terminoR
        if(asignar >= 20000 and asignar <= 21999):
            self.arrTemps[asignar-self.TempsBase] = terminoL/terminoR
                
        self.CurrentIteration+=1
    
    def goto(self,asignar):
        # print('GOTO')
        self.CurrentIteration = asignar
        # print('CURRENT ITERATION:', self.CurrentIteration)
        self.readQuadruples(asignar)
    
    def write(self,asignar):
        # print('WRITE')
        print(self.getValue(asignar))
        self.CurrentIteration+=1
    
    def read(self,operador, terminoL, terminoR, direccion):
        print('READ')
        var = input()
        if(direccion >= 10000 and direccion <= 14999):
            # print('int')
            var = int(var)
            self.arrInt[direccion-self.IntBase] = var
        if(direccion >= 15000 and direccion <= 17999):
            # print('floats')
            var = float(var)
            self.arrFloats[direccion-self.FloatBase] = var
        if(direccion >= 18000 and direccion <= 19999):
            # print('chars')
            self.arrChars[direccion-self.CharsBase] = var
        self.CurrentIteration+=1
    
    def line(self, operador, terminoL, terminoR, asignar):
        print('LINE')
        terminoR = self.getValue(terminoR)
        asignar = self.getValue(asignar)
        self.t.goto(terminoR,asignar)
        self.CurrentIteration+=1
        
    def point(self, operador, terminoL, terminoR, asignar):
        print('POINT')
        self.t.dot(5)
        self.CurrentIteration+=1
        
    def circle(self, operador, terminoL, terminoR, asignar):
        print('CIRCLE')
        asignar = self.getValue(asignar)
        self.t.circle(asignar)
        self.CurrentIteration+=1
    
    def arc(self, operador, terminoL, terminoR, asignar):
        print('ARC')
        asignar = self.getValue(asignar)
        self.t.circle(asignar, 180)
        self.CurrentIteration+=1
    
    def penup(self,operador, terminoL, terminoR, asignar):
        print('PENUP')
        self.t.penup()
        self.CurrentIteration+=1
        
    def pendown(self,operador, terminoL, terminoR, asignar):
        print('PENDOWN')
        self.t.pendown()
        self.CurrentIteration+=1 
    
    def color(self,operador, terminoL, terminoR, asignar):
        print('COLOR')
        asignar = self.getValue(asignar)
        terminoR = self.getValue(terminoR)
        terminoL = self.getValue(terminoL)
        self.t.screen.colormode(255)
        self.t.color(terminoL,terminoR,asignar)
        self.CurrentIteration+=1
    
    def size(self,operador, terminoL, terminoR, asignar):
        print('SIZE')
        asignar = self.getValue(asignar)
        self.t.pensize(asignar)
        self.CurrentIteration+=1
    
    def clear(self,operador, terminoL, terminoR, asignar):
        print('CLEAR')
        self.t.clear()
        self.CurrentIteration+=1
    #   x       x       x             x         x       x       x       x                   
    # 'line','point','circle','arc','penup','pendown','color','size','clear', 'read', 'write'
    def switch_case(self, operador, terminoL, terminoR, asignar):
        cases = {
            'GOTO': lambda: self.goto(asignar),
            'WRITE': lambda: self.write(asignar),
            'READ': lambda: self.read(operador,terminoL,terminoR,asignar),
            '=': lambda: self.assign(operador,terminoL,terminoR,asignar),
            '+': lambda: self.addition(operador,terminoL,terminoR,asignar),
            '-': lambda: self.substraction(operador,terminoL,terminoR,asignar),
            '*': lambda: self.times(operador,terminoL,terminoR,asignar),
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
        }
        cases.get(operador, lambda: print("Didn't match a case"))()
                
    def main(self):
        turtle.title("Compiler MeMyself")
        self.t.getscreen()
        
            
        self.initialValues()
        size = len(self.Quad)
        # print('--- size -----',size) 
        print('START READING QUADRUPLES')
        for x in range(size):
            # print('ci:',self.CurrentIteration, 'size', size)
            if(self.CurrentIteration <= size):
                self.readQuadruples(self.CurrentIteration)
        turtle.done()