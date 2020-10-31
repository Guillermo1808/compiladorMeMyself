#   Guillermo Enrique Valles Villegas
#   A01561722
#   
#           CUBO SEMANTICO
#   Sirve para revisar que las expresiones sean matematicamente correctas

from collections import defaultdict
class CuboSemantico:
    cuboSemantico = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))

        # PLUS
    cuboSemantico['int']['int']['+'] = 'int'
    cuboSemantico['float']['float']['+'] = 'float'
    cuboSemantico['int']['float']['+'] = 'float'
    cuboSemantico['float']['int']['+'] = 'float'

        # MINUS
    cuboSemantico['int']['int']['-'] = 'int'
    cuboSemantico['float']['float']['-'] = 'float'
    cuboSemantico['int']['float']['-'] = 'float'
    cuboSemantico['float']['int']['-'] = 'float'

        # TIMES
    cuboSemantico['int']['int']['*'] = 'int'
    cuboSemantico['float']['float']['*'] = 'float'
    cuboSemantico['int']['float']['*'] = 'float'
    cuboSemantico['float']['int']['*'] = 'float'

        # DIVIDE
    cuboSemantico['int']['int']['/'] = 'float'
    cuboSemantico['float']['float']['/'] = 'float'
    cuboSemantico['int']['float']['/'] = 'float'
    cuboSemantico['float']['int']['/'] = 'float'

        # != DIFFERENT
    cuboSemantico['int']['int']['!='] = 'int'
    cuboSemantico['float']['float']['!='] = 'int'
    cuboSemantico['int']['float']['!='] = 'int'
    cuboSemantico['float']['int']['!='] = 'int'

        # == EQUAL
    cuboSemantico['int']['int']['=='] = 'int'
    cuboSemantico['float']['float']['=='] = 'int'
    cuboSemantico['int']['float']['=='] = 'int'
    cuboSemantico['float']['int']['=='] = 'int'
    cuboSemantico['char']['char']['=='] = 'int'

        # <= LESS OR EQUAL
    cuboSemantico['int']['int']['<='] = 'int'
    cuboSemantico['float']['float']['<='] = 'int'
    cuboSemantico['int']['float']['<='] = 'int'
    cuboSemantico['float']['int']['<='] = 'int'

        # >= GREATER OR EQUAL
    cuboSemantico['int']['int']['>='] = 'int'
    cuboSemantico['float']['float']['>='] = 'int'
    cuboSemantico['int']['float']['>='] = 'int'
    cuboSemantico['float']['int']['>='] = 'int'

        # > GREATER
    cuboSemantico['int']['int']['>'] = 'int'
    cuboSemantico['float']['float']['>'] = 'int'
    cuboSemantico['int']['float']['>'] = 'int'
    cuboSemantico['float']['int']['>'] = 'int'

        # < LESS
    cuboSemantico['int']['int']['<'] = 'int'
    cuboSemantico['float']['float']['<'] = 'int'
    cuboSemantico['int']['float']['<'] = 'int'
    cuboSemantico['float']['int']['<'] = 'int'

        # = ASSIGN
    cuboSemantico['int']['int']['='] = 'int'
    cuboSemantico['float']['float']['='] = 'float'
    cuboSemantico['char']['char']['='] = 'char'

        # & AND
    cuboSemantico['int']['int']['&'] = 'int'

        # | OR
    cuboSemantico['int']['int']['|'] = 'int'


    def obtenerTipo(self, left, right, operador):
        if(self.cuboSemantico[left][right][operador] == None):
            return 'error'
        else:
            return self.cuboSemantico[left][right][operador]

# if __name__ == '__main__':
#     a = input()
#     b = input()
#     c = input()
#     d = obtenerTipo(a,b,c)
#     print(d)