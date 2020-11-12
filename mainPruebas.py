    # Guillermo Enrique Valles Villegas
    # A01561722
    # MeMyself

from sly import Lexer, Parser
from TablaFunciones import tablaFunciones
from Cuadruplos import cuadruplos
from Stacks import stacks
from CuboSemantico import CuboSemantico

# DECLARACION DE VARIABLES GLOBALES Y STACKS
currentFunction = ''
currentScope = 'global'
currentType = ''
varType = ''
DirFuncs = tablaFunciones() #CREATE DIR TABLE
POper = stacks()
PID = stacks()
PSaltos = stacks()
PArreglos = stacks()
PTypes = stacks()
PQTypes = stacks()
Cube = CuboSemantico()
Quadruples = cuadruplos()

# CONTADORES DE VARIABLES Y SUS BASES
IntBase     = 10000
FloatBase   = 15000
CharsBase   = 18000
TempsBase   = 20000
CtesBase    = 22000
IntCont     = 0
FloatCont   = 0
CharsCont   = 0
TempsCont   = 0
CtesCont    = 0
ParCont     = 1
QuadCont    = 1


class MeMyselfLexer(Lexer):
        tokens = { PROGRAM, VAR, MODULE, VOID, INT, FLOAT, ASSIGN, CHAR, RELOP, 
                    IF, ELSE, FOR, TO, THEN, DO, WHILE, RETURN, PLUS, MAIN, TO, WRITE, READ, 
                    MINUS, TIMES, DIVIDE, CTEINT, CTEFLOAT, 
                    LETRERO, ID, LOGICOS,
                    LINE, POINT, CIRCLE, ARC, PENUP, PENDOWN, COLOR, SIZE, CLEAR}

        ignore = ' \t'
        literals = { ';', ':', '(', ')', '{', '}',',', '"'}

        CTEFLOAT  = r'([0-9]+)(\.)([0-9]+)?'
        CTEINT    = r'[0-9]+'
        ID        = r'[a-zA-Z]([a-zA-Z]|[0-9_])*'
        LETRERO   = r'[\"]([a-zA-Z]*)+[\"]'
        MINUS     = r'[\-]'
        PLUS      = r'[\+]'
        TIMES     = r'[\*]'
        DIVIDE    = r'[\/]'
        RELOP     = r'(!=)|(==)|(<=)|(>=)|(<)|(>)'
        ASSIGN    = r'='
        LOGICOS   = r'(\|)|(\&)'

        ID['program'] = PROGRAM
        ID['main'] = MAIN
        ID['var'] = VAR
        ID['module'] = MODULE
        ID['void'] = VOID
        ID['int'] = INT
        ID['float'] = FLOAT
        ID['char'] = CHAR
        ID['if'] = IF
        ID['else'] = ELSE
        ID['for'] = FOR
        ID['to'] = TO
        ID['then'] = THEN
        ID['do'] = DO
        ID['while'] = WHILE
        ID['return'] = RETURN
        ID['to'] = TO
        ID['write'] = WRITE
        ID['read'] = READ
        ID['then'] = THEN
        ID['line'] = LINE
        ID['point'] = POINT
        ID['circle'] = CIRCLE
        ID['arc'] = ARC
        ID['penup'] = PENUP
        ID['pendown'] = PENDOWN
        ID['color'] = COLOR
        ID['size'] = SIZE
        ID['clear'] = CLEAR

class MeMyselfParser(Parser):
        
        tokens = MeMyselfLexer.tokens

        def __init__(self):
            self.names = { }

        #       PROGRAM
        @_('PROGRAM ID ";" program2 program3 program4')
        def program(self, p):
            pass
        @_('vars program2', '')
        def program2(self, p):
            pass
        @_('funcs', '')
        def program3(self, p):
            pass
        @_('MAIN "(" ")" "{" estatutos "}"')
        def program4(self, p):
            pass

        #       FUNCS
        @_('funcs2', '')
        def funcs(self, p):
            pass
        @_('funcv funcs', 'funcr funcs')
        def funcs2(self, p):
            pass

        #       FUNCV
        @_('VOID MODULE ID "(" parametros ")" ";" vars "{" estatutos "}"', '')
        def funcv(self, p):
            pass

        #       FUNCR
        @_('tipov MODULE ID "(" parametros ")" ";" vars "{" estatutos return0 "}"', '')
        def funcr(self, p):
            pass

        #       ESTATUTOS
        @_('estatuto', 'estatutos')
        def estatutos(self, p):
            pass

        #       ESTATUTO
        @_('asignacion', 'funcs', 'lectura estatuto', 'escritura estatuto', 'decision estatuto', 'repeticiondo estatuto', 'repeticionfor estatuto', 'exp estatuto', 'especiales estatuto', '')
        def estatuto(self, p):
            pass

        #       ASIGNACION
        @_('ID ASSIGN exp ";"')
        def asignacion(self, p):
            pass

        #       LECTURA
        @_('READ "(" ID lectura2 ")" ";"')
        def lectura(self, p):
            pass
        @_('"," ID lectura2', '')
        def lectura2(self, p):
            pass

        #       ESCRITURA
        @_('WRITE "(" escritura2 ")" ";"')
        def escritura(self, p):
            pass
        @_('printe', 'escritura3')
        def escritura2(self, p):
            pass
        @_('"," escritura2', '')
        def escritura3(self, p):
            pass

        #       PRINT
        @_('LETRERO printe2', 'exp printe2')
        def printe(self, p):
            pass
        @_('LETRERO', 'exp', '')
        def printe2(self, p):
            pass

        #       DECISION
        @_('IF "(" expresion ")" THEN decision2 decision3')
        def decision(self, p):
            pass
        @_('"{" estatutos ";" "}"')
        def decision2(self, p):
            pass
        @_('ELSE "{" estatutos ";" "}"', '')
        def decision3(self, p):
            pass

        #       DO
        @_('WHILE "(" expresion ")" DO "{" estatutos ";" "}"')
        def repeticiondo(self, p):
            pass

        #       FOR
        @_('FOR ID ASSIGN exp TO exp DO "{" estatutos ";" "}"')
        def repeticionfor(self, p):
            pass

        #       ESPECIALES
        @_('line','point','circle','arc','penup','pendown','color','size','clear')
        def especiales(self, p):
            pass
        
        #       LINE
        @_('LINE "(" exp "," exp "," exp "," exp ")" ";"')
        def line(self, p):
            pass

        #       POINT
        @_('POINT "(" exp "," exp ")" ";"')
        def point(self, p):
            pass

        #       CIRCLE
        @_('CIRCLE "(" exp ")" ";"')
        def circle(self, p):
            pass

        #       ARC
        @_('ARC "(" exp ")" ";"')
        def arc(self, p):
            pass

        #       PENUP
        @_('PENUP "(" ")" ";"')
        def penup(self, p):
            pass

        #       PENDOWN
        @_('PENDOWN "(" ")" ";"')
        def pendown(self, p):
            pass

        #       COLOR
        @_('COLOR "(" CTEINT ")" ";"')
        def color(self, p):
            pass

        #       SIZE
        @_('SIZE "(" exp ")" ";"')
        def size(self, p):
            pass

        #       CLEAR
        @_('CLEAR "(" ")" ";"')
        def clear(self, p):
            pass

        #      EXPRESION
        @_('comparar LOGICOS comparar', 'comparar')
        def expresion(self,p):
            pass
        
        #      COMPARAR
        @_('exp RELOP exp')
        def comparar(self,p):
            pass

        #       RETURN
        @_('RETURN "(" exp ")"')
        def return0(self,p):
            pass

        #       EXP
        @_('termino exp2')
        def exp(self,p):
            pass

        @_('PLUS termino exp2','MINUS termino exp2', '')
        def exp2(self,p):
            pass
        
        #       TERMINO
        @_('factor termino2')
        def termino(self,p):
            pass
        
        @_('TIMES factor termino2', 'DIVIDE factor termino2','')
        def termino2(self,p):
            pass

        #       PARAMETROS
        @_('tipov ID parametros2', '')
        def parametros(self,p):
            global ParCont
            ParCont = 1
            pass
        
        @_('"," tipov ID parametros2','')
        def parametros2(self,p):
            pass

        #       FACTOR
        #@_('"(" quad_6 expresion ")" quad_7','PLUS varcte',  'MINUS varcte', 'varcte')
        @_('"(" expresion ")"','PLUS varcte',  'MINUS varcte', 'varcte')
        def factor(self,p):
            pass


        #       VARCTE
        @_('ID','CTEINT','CTEFLOAT','LETRERO')
        def varcte(self, p):
            pass

        #       VARS
        @_('VAR tipov ":" ID vars2 ";"', '')
        def vars(self, p):
            pass
        @_('"," ID vars2', '')
        def vars2(self, p):
            pass

        #       TIPOV
        @_('INT', 'FLOAT', 'CHAR')
        def tipov(self, p):
            PTypes.add(p[0])
            pass
        
        # #################################
        # ## FUNCIONES PARA LAS ACCIONES ##
        # #################################
        
        # #FUNCIONES PARA LOS CUADRUPLOS
        # @_('')
        # def quad_cteI(self, p): # HACER PUSH A LOS STACKS CON CTE INTS
        #     cte = p[-1]
        #     PID.add(cte)
        #     PQTypes.add('int')
        #     # print('quad_cteI')
        # @_('')
        # def quad_cteF(self, p): # HACER PUSH A LOS STACKS CON CTE FLOATS
        #     cte = p[-1]
        #     PID.add(cte)
        #     PQTypes.add('float')
        #     # print('quad_cteF')
        # # @_('')
        # # def quad_cteS(self, p): # HACER PUSH A LOS STACKS CON LETREROS
        # #     cte = p[-1]
        # #     PID.add(cte)
        # #     PQTypes.add('letrero')
        # #     print('quad_cteS')
        # @_('')
        # def quad_1(self, p): # HACER PUSH A LOS STACKS CON EL ID DE LA VARIABLE Y SU TIPO
        #     PID.add(p[-1])
        #     tipo = DirFuncs.getVarType(p[-1])
        #     if tipo == None:
        #         print('ERROR: VARIABLE', p[-1], 'NOT DECLARED')
        #         exit()
        #     else:
        #         PQTypes.add(DirFuncs.getVarType(p[-1]))
        #     # PID.print()
        #     # PQTypes.print()
        #     # print('quad_1')
        # @_('')
        # def quad_2(self, p): #AGREGAR + o - AL POper 
        #     POper.add(p[-1])
        #     # POper.print()
        #     # print('quad_2')
        # @_('')
        # def quad_3(self, p): #AGREGAR * o / AL POper
        #     POper.add(p[-1])
        #     # POper.print()
        #     # print('quad_3')    
        # @_('')
        # def quad_4(self, p): # CREA EL CUADRUPLO CON + -
        #     global QuadCont
        #     # POper.print()
        #     # PID.print()
        #     if ((POper.empty() == False) and (PID.size() >= 2)):
        #         # print('entra al primer if')
        #         if ((POper.top() == '+') or (POper.top() == '-')):
        #             # print("entra al segundo if")
        #             right_operand = PID.pop()
        #             right_type = PQTypes.pop()
        #             left_operand = PID.pop()
        #             left_type = PQTypes.pop()
        #             print('RO:', right_operand, '| RT: ', right_type, '| LO:', left_operand, '| LT: ', left_type)
        #             operator = POper.pop()
        #             print('CUBE:', left_type, right_type, operator)
        #             result_Type = Cube.obtenerTipo(left_type, right_type, operator)
        #             if(result_Type != 'error'):
        #                 result = 't'
        #                 Quadruples.add(QuadCont, operator, left_operand, right_operand, result)
        #                 QuadCont+=1
        #                 Quadruples.print()
        #             else:
        #                 print("ERROR: TYPE MISMATCH")
        #                 exit()
        #     # print('quad_4')
        # @_('')
        # def quad_5(self, p): # CREA EL CUADRUPLO CON / *
        #     global QuadCont
        #     # POper.print()
        #     # PID.print()
        #     if ((POper.empty() == False) and (PID.size() >= 2)):
        #         # print('entra al primer if')
        #         if ((POper.top() == '/') or (POper.top() == '*')):
        #             # print("entra al segundo if")
        #             right_operand = PID.pop()
        #             right_type = PQTypes.pop()
        #             left_operand = PID.pop()
        #             left_type = PQTypes.pop()
        #             print('RO:', right_operand, '| RT: ', right_type, '| LO:', left_operand, '| LT: ', left_type)
        #             operator = POper.pop()
        #             print('CUBE:', left_type, right_type, operator)
        #             result_Type = Cube.obtenerTipo(left_type, right_type, operator)
        #             if(result_Type != 'error'):
        #                 result = 't'
        #                 Quadruples.add(QuadCont, operator, left_operand, right_operand, result)
        #                 QuadCont+=1
        #                 Quadruples.print()
        #             else:
        #                 print("ERROR: TYPE MISMATCH")
        #                 exit()
        #     # print('quad_5')
            
        # @_('')
        # def quad_6(self, p): # PUSH FALSE BOTTOM MARK
        #     POper.add(p[-1])
        #     POper.print()
        #     # print('quad_6')
        # @_('')
        # def quad_7(self, p): # POP FALSE BOTTOM MARK
        #     POper.pop()
        #     POper.print()
        #     # print('quad_7')
        # @_('')
        # def quad_8(self, p): # POP FALSE BOTTOM MARK
        #     POper.add(p[-1])
        #     POper.print()
        #     # print('quad_7')
        
        # @_('')
        # def quad_9(self, p): # CREA EL CUADRUPLO CON RELOPS (!=)|(==)|(<=)|(>=)|(<)|(>)
        #     global QuadCont
        #     # POper.print()
        #     # PID.print()
        #     if ((POper.empty() == False) and (PID.size() >= 2)):
        #         # print('entra al primer if')
        #         if ((POper.top() == '!=') or (POper.top() == '==')or (POper.top() == '<=')or (POper.top() == '>=')or (POper.top() == '<')or (POper.top() == '>')):
        #             # print("entra al segundo if")
        #             right_operand = PID.pop()
        #             right_type = PQTypes.pop()
        #             left_operand = PID.pop()
        #             left_type = PQTypes.pop()
        #             print('RO:', right_operand, '| RT: ', right_type, '| LO:', left_operand, '| LT: ', left_type)
        #             operator = POper.pop()
        #             print('CUBE:', left_type, right_type, operator)
        #             result_Type = Cube.obtenerTipo(left_type, right_type, operator)
        #             if(result_Type != 'error'):
        #                 result = 't'
        #                 Quadruples.add(QuadCont, operator, left_operand, right_operand, result)
        #                 QuadCont+=1
        #                 Quadruples.print()
        #             else:
        #                 print("ERROR: TYPE MISMATCH")
        #                 exit()
        #     # print('quad_9')
                    
        # ###############            
        # # FUNCIONES PARA AGREGAR A LAS TABLAS
        # ############### 
        # @_('')
        # def funcs_1(self, p): # Agrega el programa
        #     global QuadCont
        #     self.currentFunction = p[-1]
        #     self.currentScope = 'global'
        #     DirFuncs.addFunction(self.currentFunction, 'main', self.currentScope)
        #     Quadruples.add(QuadCont, 'GOTO', 0, 0, '_')
        #     QuadCont+=1
        #     # print('funcs_1')
        # @_('')
        # def funcs_2(self, p): #Agrega Variable
        #     self.currentType = PTypes.pop()
        #     global IntCont
        #     global FloatCont
        #     global CharsCont
        #     #print('IntCont:', IntCont, 'FloatCont', FloatCont,'CharsCont', CharsCont)
        #     if(self.currentType == 'int'):
        #         DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, IntBase+IntCont)
        #         IntCont+=1
        #     if(self.currentType == 'float'):
        #         DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, FloatBase+FloatCont)
        #         FloatCont+=1
        #     if(self.currentType == 'char'):
        #         DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, CharsBase+CharsCont)
        #         CharsCont+=1
        #     # print('funcs_2')
        # @_('')
        # def funcs_3(self, p): #Agregar modulo a DirFuncs
        #     self.currentType = PTypes.pop()
        #     # print('current Type:', self.currentType)
        #     self.currentFunction = p[-1]
        #     # print('current function: ', self.currentFunction)
        #     DirFuncs.addFunction(self.currentFunction, self.currentType, 'module'+str(self.currentFunction))
        # @_('')
        # def funcs_4(self, p): #Agregar parametros a modulo
        #     global ParCont
        #     self.currentType = PTypes.pop()
        #     DirFuncs.addParametros(self.currentFunction, ParCont ,self.currentType)
        #     ParCont+=1
                       
        # @_('')
        # def current_typeV(self, p):
        #     PTypes.add('void')
        #     # print('current_typeV')
        

        # FUNCION PRINCIPAL DEL PROGRAMA 
if __name__ == '__main__':

    file = open("test.txt", 'r')
    masterline = ""

    for line in file:
        masterline = masterline + line.strip()
        
    lexer = MeMyselfLexer()
    parser = MeMyselfParser()
    cuadruplo = cuadruplos()
    result = parser.parse(lexer.tokenize(masterline))
    print(result)
    # while True:
    #     try:
    #         text = input('duck > ')
    #         result = parser.parse(lexer.tokenize(text))
    #         print(result)
    #         # for line in file:
    #         #     result = parser.parse(lexer.tokenize(line.strip()))
    #         #     print(result)

    #     except EOFError:
    #         break
    file.close()
    # DirFuncs.printFunction()

# if __name__ == '__main__':
    
#     lexer = MeMyselfLexer()
#     parser = MeMyselfParser()
#     cuadruplo = cuadruplos()
#     while True:
#          try:
#              text = input('---> ')
#              parser.parse(lexer.tokenize(text))
#              for tok in lexer.tokenize(text):
#                  print(tok)
#          except EOFError:
#              break
    
# if __name__ == '__main__':
#     file = open("test.txt", 'r')
#     text = ""
#     for line in file:
#         fullLine = text + line.strip()
        
#     print(text)
#     lexer = MeMyselfLexer()
#     parser = MeMyselfParser()
#     result = parser.parse(lexer.tokenize(text))
#     print(result)
#     # while True:
#     #      try:
#     #          #text = input('---> ')
#     #          parser.parse(lexer.tokenize(text))
#     #          for tok in lexer.tokenize(text):
#     #              print(tok)
#     #      except EOFError:
#     #          break
#     file.close()