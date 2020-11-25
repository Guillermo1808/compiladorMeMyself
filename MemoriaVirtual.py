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
    drawing = False
    
    def __init__(self, cuadruplosD, funcionesD, cantTemps):
        self.cuadruplosF = cuadruplos()
        self.DirFunc = tablaFunciones()
        self.cuadruplosF = cuadruplosD
        self.DirFunc = funcionesD
        self.Quad = self.cuadruplosF.getValues()
        self.Temporales = cantTemps
        
    def initialFunctionValues(self, fid):     #Cuando es llamado con ERA, esta funcion agrega un diccionario con arreglos
                                            #  cuyo tamaño depende del que tiene la funcion guardado
        valores = self.DirFunc.getFunctionInitialValues(fid)
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
        
        
    def initialValues(self):        #Obtiene los valores principales de la memoria
        valores = self.DirFunc.getInitialValues()
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
                
        valoresVars = self.DirFunc.getGlobalVarsValues()
        for keys in valoresVars:
            direccion = valoresVars[keys]['memory']
            if(direccion >= 10000 and direccion <= 11000):
                if 'size' in valoresVars[keys].keys():
                    for x in range(valoresVars[keys]['size']):
                        self.arrInt.append(0)
                else:
                    self.arrInt.append(0)
            if(direccion >= 15000 and direccion <= 16000):
                self.arrFloats.append(0)
            if(direccion >= 18000 and direccion <= 19000):
                self.arrChars.append(0)
            
        for i in range(self.Temporales):
            self.arrTemps.append(0)
        
    
    def getValue(self,direccion):       #Con la direccion, obtiene el valor de la variable
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
        
    def readQuadruples(self, iteration): #lee los cuadruplos y le manda los valores al switch case
        operador = self.Quad[iteration]['operador']
        terminoL = self.Quad[iteration]['termino1']
        terminoR = self.Quad[iteration]['termino2']
        asignar = self.Quad[iteration]['asignar']
        self.switch_case(operador, terminoL, terminoR, asignar)
    
    def assign(self, operador, terminoL, terminoR, asignar): #Funcion encargada para asignar valores
        
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
            #Si es arreglo las direcciones son apuntadores, por lo que necesitan doble get value
            aux = asignar
            aux = self.getValue(aux)
            aux = self.getValue(aux)
            if(aux == None):
                terminoL = self.getValue(terminoL)
                terminoL = self.getValue(terminoL)
            else:
                terminoL = self.getValue(terminoL)
                asignar = self.getValue(asignar)
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

            self.isArray = False
        self.CurrentIteration+=1
        
            #Funcion encargada para sumar valores    
    def addition(self, operador, terminoL, terminoR, asignar):
        terminoL = self.getValue(terminoL)
        terminoR = self.getValue(terminoR)
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

        #Funcion encargada para restar valores
    def substraction(self, operador, terminoL, terminoR, asignar):
        terminoL = self.getValue(terminoL)
        terminoR = self.getValue(terminoR)
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
        #Funcion encargada para multiplicar valores
    def times(self, operador, terminoL, terminoR, asignar):
        
        terminoL = self.getValue(terminoL)
        terminoR = self.getValue(terminoR)
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
        
        #Funcion encargada para dividir valores
    def divide(self, operador, terminoL, terminoR, asignar):
        terminoL = self.getValue(terminoL)
        terminoR = self.getValue(terminoR)
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
    
    def goto(self,asignar):     #Cambia el valor del apuntador actual de los cuadruplos
        self.CurrentIteration = asignar
    
    def gotof(self,operador, terminoL, terminoR, asignar):
        terminoL = self.getValue(terminoL) #Cambia el valor del apuntador actual de los cuadruplos
        
        if(terminoL != 1):
            self.CurrentIteration = asignar
        else:
            self.CurrentIteration+=1
    
    def write(self,asignar): #Funcion para imprimir los resultados

        if self.isArray:
            x = self.getValue(asignar)
            x = self.getValue(x)
            print(x)
        else:
            print(self.getValue(asignar))
        self.CurrentIteration+=1
    
    def read(self,operador, terminoL, terminoR, direccion):#Asigna el valor leido de consola a la variable
        var = input()
        if(direccion >= 10000 and direccion < 11000):
            var = int(var)
            self.arrInt[direccion-self.IntBase] = var
        if(direccion >= 15000 and direccion < 16000):
            var = float(var)
            self.arrFloats[direccion-self.FloatBase] = var
        if(direccion >= 18000 and direccion < 19000):
            self.arrChars[direccion-self.CharsBase] = var
        
        if(direccion >= 11000 and direccion <= 14999):
            self.functions[self.CurrentFunction][0][direccion-self.IntBaseF] = var
        if(direccion >= 16000 and direccion <= 17999):
            self.functions[self.CurrentFunction][1][direccion-self.FloatBaseF] = var
        if(direccion >= 19000 and direccion <= 19999):
            self.functions[self.CurrentFunction][2][direccion-self.CharsBaseF] = var
        self.CurrentIteration+=1
    
    def line(self, operador, terminoL, terminoR, asignar):#Funcion Turtle - Dibuja una linea
        asignar = self.getValue(asignar)
        self.t.goto(terminoR,asignar)
        self.drawing = True
        self.CurrentIteration+=1
        
    def point(self, operador, terminoL, terminoR, asignar):#Funcion Turtle - Dibuja un punto
        self.t.dot(5)
        self.drawing = True
        self.CurrentIteration+=1
        
    def circle(self, operador, terminoL, terminoR, asignar):#Funcion Turtle - Dibuja un circulo
        asignar = self.getValue(asignar)
        self.t.circle(asignar)
        self.drawing = True
        self.CurrentIteration+=1
    
    def arc(self, operador, terminoL, terminoR, asignar):#Funcion Turtle - Dibuja un arco
        asignar = self.getValue(asignar)
        self.t.circle(asignar, 180)
        self.drawing = True
        self.CurrentIteration+=1
    
    def penup(self,operador, terminoL, terminoR, asignar):#Funcion Turtle - Levanta la pluma para dejar de escribir
        self.t.penup()
        self.drawing = True
        self.CurrentIteration+=1
        
    def pendown(self,operador, terminoL, terminoR, asignar):#Funcion Turtle - Baja la pluma para escribir
        self.t.pendown()
        self.drawing = True
        self.CurrentIteration+=1 
    
    def color(self,operador, terminoL, terminoR, asignar):#Funcion Turtle - Cambia el color con valores RGB
        asignar = self.getValue(asignar)
        terminoR = self.getValue(terminoR)
        terminoL = self.getValue(terminoL)
        self.t.screen.colormode(255)
        self.t.color(terminoL,terminoR,asignar)
        self.drawing = True
        self.CurrentIteration+=1
    
    def size(self,operador, terminoL, terminoR, asignar):#Funcion Turtle - Cambia el tamaño del lapiz
        asignar = self.getValue(asignar)
        self.t.pensize(asignar)
        self.drawing = True
        self.CurrentIteration+=1
    
    def clear(self,operador, terminoL, terminoR, asignar):#Funcion Turtle - Limpia la pantalla
        self.t.clear()
        self.drawing = True
        self.CurrentIteration+=1
    
    #Comienzan los "boleanos". En base a lo que de de resultado la comparación. Devuelven 1, que es True, o 2 que es false
    
    def equal(self,operador, terminoL, terminoR, direccion):#Funcion encargada de checar si es igual
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
    
    def different(self,operador, terminoL, terminoR, direccion):#Funcion encargada de checar si es diferente
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
        
    def lte(self,operador, terminoL, terminoR, direccion):#Funcion encargada de checar si es menor o igual
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
     
    def lt(self,operador, terminoL, terminoR, direccion):#Funcion encargada de checar si es menor
        valorL = self.getValue(terminoL)
        valorR = self.getValue(terminoR)
       
        if(valorL < valorR):
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
    
    def gte(self,operador, terminoL, terminoR, direccion):#Funcion encargada de checar si es mayor o igual
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
    
    def gt(self,operador, terminoL, terminoR, direccion):#Funcion encargada de checar si es mayor
        valorL = self.getValue(terminoL)
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
    
    def andF(self,operador, terminoL, terminoR, direccion):#Funcion encargada de checar si ambos terminos son true
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
    
    def orF(self,operador, terminoL, terminoR, direccion): #Funcion encargada de checar si alguno de los terminos es true
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
        
        #Terminan los boleanos
    
    def eraF(self,operador, terminoL, terminoR, direccion):#Crea el contexto para la función
        self.CurrentFunction +=1
        self.initialFunctionValues(direccion)
        self.CurrentIteration+=1
    
    def paramF(self,operador, terminoL, terminoR, direccion):#Asigna el valor para parametros
        asignar = terminoL
        terminoL = self.getValue(terminoL)
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
        self.gosub = self.CurrentIteration
        self.CurrentIteration = direccion

    def endF(self,operador, terminoL, terminoR, direccion):#termina la función. Setea el currentFunction a 0  (global)
        self.CurrentIteration = self.gosub
        self.currentFunction = 0
        self.CurrentIteration+=1
    
    def verify(self,operador, terminoL, terminoR, direccion):#Funcion encargada de verificar si el valor de arreglo esta dentro del rango

        terminoL = self.getValue(terminoL)
        if(terminoL < direccion and terminoL >= terminoR):
            self.CurrentIteration+=1
        else:
            print('ERROR: ARRAY INDEX OUT OF BOUNDS')
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
        
    def memoria2(self,operador, terminoL, terminoR, direccion):#Funcion encargada de sumar memorias para los arreglos
        
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

    def switch_case(self, operador, terminoL, terminoR, asignar): #Swtich case para los valores que pueda tener el operador de los cuadruplos
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
                
    def main(self): #Funcion principal.
        turtle.title("Mayka")
        self.initialValues()
        size = len(self.Quad)
        while(self.CurrentIteration <= size): #While que lee todos los cuadruplos
    
            self.readQuadruples(self.CurrentIteration)
        print('Program ended with code 0;')
   
        if self.drawing:
            turtle.done()