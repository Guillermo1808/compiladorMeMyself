# Guillermo Enrique Valles Villegas
# A01561722
# Maquina Virtual

from TablaFunciones import tablaFunciones as funciones
from Cuadruplos import cuadruplos
from Stacks import stacks
import sys

class MaquinaVirtual: 
    arrInt = stacks()
    arrFloats = stacks()
    arrChars = stacks()
    arrTemps = stacks()
    arrCtes = stacks()
    IntBase     = 10000
    FloatBase   = 15000
    CharsBase   = 18000
    TempsBase   = 20000
    CtesBase    = 22000
    
    def __init__(self, dictionary):
        self.dictionary = dictionary
        

    def initialValues(self, funciones):
        funciones['globales']['variables'].print()
        

