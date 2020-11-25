    # Guillermo Enrique Valles Villegas
    # A01561722
    # Compilador MeMyself

from sly import Lexer, Parser
from TablaFunciones import tablaFunciones
from Cuadruplos import cuadruplos
from Stacks import stacks
from CuboSemantico import CuboSemantico
from MemoriaVirtual import MaquinaVirtual

# DECLARACION DE VARIABLES GLOBALES Y STACKS
currentFunction = ''
currentScope = 'global'
currentType = ''
nombrePrograma = ''
varType = ''
VControl = ''
ParamPointer = ''
DirFuncs = tablaFunciones() #CREATE DIR TABLE
DirFuncs.addFunction('globales','ctes','global',1)
POper = stacks()
PID = stacks()
PPar = stacks()
PQPar = stacks()
PSaltos = stacks()
PTypes = stacks()
PQTypes = stacks()
PDim = stacks()
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
# CONTADORES PARA FUNCIONES
IntBaseF     = 11000
FloatBaseF   = 16000
CharsBaseF   = 19000
TempsBaseF   = 21000
IntContF     = 0
FloatContF   = 0
CharsContF   = 0
TempsContF   = 0

####
ParCont     = 1
ParCounter  = 1
QuadCont    = 1
LIM1        = 1
LIM2        = 0
R           = 1
M1          = 1
M2          = 0
sizeA       = 1
DIM         = 1
currentArray = ''


class MeMyselfLexer(Lexer):
        tokens = { PROGRAM, VAR, MODULE, VOID, INT, FLOAT, ASSIGN, CHAR, RELOP, 
                    IF, ELSE, FOR, TO, THEN, DO, WHILE, RETURN, PLUS, MAIN, TO, WRITE, READ, 
                    MINUS, TIMES, DIVIDE, CTEINT, CTEFLOAT, CTECHAR,  
                    LETRERO, ID, LOGICOS,
                    LINE, POINT, CIRCLE, ARC, PENUP, PENDOWN, COLOR, SIZE, CLEAR, CALL}

        ignore = ' \t'
        literals = { ';', ':', '(', ')', '{', '}', '[', ']',',', '"'}

        CTEFLOAT  = r'([0-9]+)(\.)([0-9]+)?'
        CTEINT    = r'[0-9]+'
        LETRERO   = r'[\"]([a-zA-Z]*)+[\"]'
        CTECHAR    = r'\'[a-zA-Z_]\''
        ID        = r'[a-zA-Z]([a-zA-Z]|[0-9_])*'
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
        ID['call'] = CALL
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
        @_('PROGRAM ID funcs_1 ";" program2 program3 program4')
        def program(self, p):
            pass
        @_('vars program2', '')
        def program2(self, p):
            pass
        @_('funcs', '')
        def program3(self, p):
            pass
        @_('MAIN quad_f1 "(" ")" "{" estatutos "}"')
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
        @_('VOID current_typeV MODULE ID funcs_3 "(" parametros ")" ";" vars "{" estatutos "}" funcs_calls7 ', '')
        def funcv(self, p):
            pass

        #       FUNCR
        @_('tipov MODULE ID funcs_3 funcs_r "(" parametros ")" ";" vars "{" estatutos return0 "}" funcs_calls7 ', '')
        def funcr(self, p):
            pass

        #       LECTURA
        @_('READ "(" ID quad_read lectura2 ")" ";"')
        def lectura(self, p):
            pass
        @_('"," ID quad_read lectura2', '')
        def lectura2(self, p):
            pass

        #       ESCRITURA
        @_('WRITE "(" escritura2 ")" ";"')
        def escritura(self, p):
            pass
        @_('printe', ' escritura3')
        def escritura2(self, p):
            pass
        @_('"," escritura2', '')
        def escritura3(self, p):
            pass

        #       PRINT
        @_('LETRERO funcs_cteL quad_let quad_writeL  printe2', 'exp quad_write printe2')
        def printe(self, p):
            pass
        @_('"," printe', '')
        def printe2(self, p):
            pass
        # @_('"," LETRERO funcs_cteL quad_let quad_writeL  printe2', '"," exp quad_write printe2', '')
        # def printe2(self, p):
        #     pass

        #       DECISION
        @_('IF "(" expresion ")" quad_if1 THEN decision2 decision3 quad_if2')
        def decision(self, p):
            pass
        @_('"{" estatutos "}"')
        def decision2(self, p):
            pass
        @_('ELSE "{" quad_if3 estatutos "}"', '')
        def decision3(self, p):
            pass

        #       DO
        @_('WHILE quad_wd1 "(" expresion ")" quad_wd2 DO "{" estatutos "}" quad_wd3')
        def repeticiondo(self, p):
            pass

        #       FOR
        @_('FOR ID quad_for1 ASSIGN exp quad_for2 TO exp quad_for3 DO "{" estatutos "}" quad_for4')
        def repeticionfor(self, p):
            PTypes.pop()
            PID.pop()
            pass
        
        #       ESTATUTOS
        @_('estatuto estatutos', '')
        def estatutos(self, p):
            pass

        #       ESTATUTO
        @_('funcionC', 'asignacion', 'lectura', 'escritura', 'decision', 'repeticiondo', 'repeticionfor', 'exp', 'especiales', '')
        def estatuto(self, p):
            pass
        
        #       FUNCION CALL
        @_('CALL ID funcs_calls "(" funcs_calls2 funcionC2 funcs_calls5 ")" funcs_calls6 ";"')
        def funcionC(self, p):
            pass
        @_('exp funcs_calls3 funcionC3','')
        def funcionC2(self, p):
            pass
        @_('"," funcs_calls4 funcionC2','')
        def funcionC3(self, p):
            pass
        
        #       ASIGNACION
        @_('array ASSIGN quad_1array exp quad_a ";"','array ASSIGN quad_1array funcionD quad_a ";"','ID ASSIGN quad_1a exp quad_a ";"', 'ID ASSIGN quad_1a funcionD quad_a')
        def asignacion(self, p):
            pass
        
        #       FUNCION
        @_('ID funcs_calls "(" funcs_calls2 funcionD2 funcs_calls5 ")" funcs_calls6 ";"')
        def funcionD(self, p):
            pass
        @_('exp funcs_calls3 funcionD3','')
        def funcionD2(self, p):
            pass
        @_('"," funcs_calls4 funcionD2','')
        def funcionD3(self, p):
            pass
        

        #       ESPECIALES
        @_('line','point','circle','arc','penup','pendown','color','size','clear')
        def especiales(self, p):
            pass
        
        #       LINE
        @_('LINE "(" exp "," exp ")" quad_line ";"')
        def line(self, p):
            pass

        #       POINT
        @_('POINT "(" ")" quad_point ";"')
        def point(self, p):
            pass

        #       CIRCLE
        @_('CIRCLE "(" exp ")" quad_circle ";"')
        def circle(self, p):
            pass

        #       ARC
        @_('ARC "(" exp ")" quad_arc ";"')
        def arc(self, p):
            pass

        #       PENUP
        @_('PENUP "(" ")" quad_penup ";"')
        def penup(self, p):
            pass

        #       PENDOWN
        @_('PENDOWN "(" ")" quad_pendown ";"')
        def pendown(self, p):
            pass

        #       COLOR
        @_('COLOR "(" exp "," exp "," exp ")" quad_color ";"')
        def color(self, p):
            pass

        #       SIZE
        @_('SIZE "(" exp ")" quad_size ";"')
        def size(self, p):
            pass

        #       CLEAR
        @_('CLEAR "(" ")" quad_clear ";"')
        def clear(self, p):
            pass

        #      EXPRESION
        @_('comparar LOGICOS quad_10 comparar quad_11', 'comparar')
        def expresion(self,p):
            pass
        
        #      COMPARAR
        @_('exp RELOP quad_8 exp quad_9')
        def comparar(self,p):
            pass

        #       RETURN
        @_('RETURN "(" exp ")" funcs_r2 ";"')
        def return0(self,p):
            pass

        #       EXP
        @_('termino quad_4 exp2')
        def exp(self,p):
            pass

        @_('PLUS quad_2 exp','MINUS quad_2 exp', '')
        def exp2(self,p):
            pass
        
        #       TERMINO
        @_('factor quad_5 termino2')
        def termino(self,p):
            pass
        @_('TIMES quad_3 termino', 'DIVIDE quad_3 termino','')
        def termino2(self,p):
            pass

        #       PARAMETROS
        @_('tipov ID funcs_2 funcs_4 parametros2', '')
        def parametros(self,p):
            global ParCont
            ParCont = 1
            pass
        
        @_('"," tipov ID funcs_2 funcs_4 parametros2','')
        def parametros2(self,p):
            pass

        #       FACTOR
        @_('"(" quad_6 exp ")" quad_7','PLUS varcte',  'MINUS varcte','varcte')
        def factor(self,p):
            pass

        #       VARCTE
        @_('funcionD', 'array','ID quad_1','CTEINT funcs_cteI quad_cteI','CTEFLOAT funcs_cteF quad_cteF','CTECHAR funcs_cteC quad_cteC','LETRERO funcs_cteL quad_let')
        def varcte(self, p):
            pass
        
        #     LLAMADA A VARIABLE EN ARREGLO
        @_('ID quad_array1 "[" quad_array2 exp quad_array3 array2 "]" quad_array5' )
        def array(self, p):
            pass
        
        @_('"," quad_array4 exp quad_array3', '')
        def array2(self, p):
            pass
        
        
        #       VARS
        @_('varsN', 'varsD')
        def vars(self, p):
            pass
        
        #       VARS NORMALES
        @_('VAR tipov ":" ID funcs_2 varsN2 ";"', '')
        def varsN(self, p):
            pass
        @_('"," ID funcs_2_1 varsN2', '')
        def varsN2(self, p):
            pass
        
        @_('VAR tipov ":" ID funcs_2A "[" CTEINT funcs_3A varsD2 "]" funcs_5A ";"') 
        def varsD(self, p):
            pass
        @_('"," CTEINT funcs_4A', '')
        def varsD2(self, p):
            pass

        #       TIPOV
        @_('INT', 'FLOAT', 'CHAR')
        def tipov(self, p):
            PTypes.add(p[0])
            pass
        
        #################################
        ## FUNCIONES PARA LAS ACCIONES ##
        #################################
        
        #FUNCIONES PARA LOS CUADRUPLOS
        @_('')
        def quad_cteI(self, p): # HACER PUSH A LOS STACKS CON CTE INTS
            cte = p[-2]
            if(p[-3] == '-'):
                cte = '-'+cte
            PID.add(cte)
            PQTypes.add('int')
        @_('')
        def quad_cteF(self, p): # HACER PUSH A LOS STACKS CON CTE FLOATS
            cte = p[-2]
            PID.add(cte)
            PQTypes.add('float')
            
        @_('')
        def quad_cteC(self, p): # HACER PUSH A LOS STACKS CON CTE INTS
            cte = p[-2]
            PID.add(cte)
            PQTypes.add('char')
        @_('')
        def quad_let(self, p): # HACER PUSH A LOS STACKS CON LETREROS
            cte = p[-2]
            PID.add(cte)
            PQTypes.add('letrero')
        @_('')
        def quad_1(self, p): # HACER PUSH A LOS STACKS CON EL ID DE LA VARIABLE Y SU TIPO
            PID.add(p[-1])
            tipo = DirFuncs.getVarType(p[-1])
            if tipo == None:
                print('ERROR: VARIABLE', p[-1], 'NOT DECLARED')
                exit()
            else:
                PQTypes.add(tipo)
            
        @_('')
        def quad_1a(self, p): # HACER PUSH A LOS STACKS CON EL ID DE LA VARIABLE Y SU TIPO
            
            PID.add(p[-2])

            tipo = DirFuncs.getVarType(p[-2])
            if tipo == None:
                print('ERROR: VARIABLE', p[-2], 'NOT DECLARED')
                exit()
            else:
                PQTypes.add(tipo)
            
            
        @_('')
        def quad_1array(self, p): # HACER PUSH A LOS STACKS CON EL ID DE LA VARIABLE Y SU TIPO
            global currentArray
            tipo = DirFuncs.getVarType(currentArray)
            if tipo == None:
                print('ERROR: VARIABLE', currentArray, 'NOT DECLARED')
                exit()
            else:
                PQTypes.add(tipo)
            
        @_('')
        def quad_2(self, p): #AGREGAR + o - AL POper 
            print(p[-1])
            POper.add(p[-1])
            
        @_('')
        def quad_3(self, p): #AGREGAR * o / AL POper
            POper.add(p[-1])
             
        @_('')
        def quad_4(self, p): # CREA EL CUADRUPLO CON + -
            global QuadCont
            global TempsCont
            global TempsBase
            global TempsContF
            global TempsBaseF
            if ((POper.empty() == False) and (PID.size() >= 2)):
                if ((POper.top() == '+') or (POper.top() == '-')):
                    right_operand = PID.pop()
                    right_type = PQTypes.pop()
                    left_operand = PID.pop()
                    left_type = PQTypes.pop()
                    operator = POper.pop()
                    result_Type = Cube.obtenerTipo(left_type, right_type, operator)
                    if(result_Type != 'error'):
                        if(self.currentScope != 0):
                            result = TempsContF + TempsBaseF
                            TempsContF+=1
                        else:
                            result = TempsBase + TempsCont
                            TempsCont+=1
                        if(type(left_operand) == str):
                            left_operand = DirFuncs.getVarDir(left_operand)
                        if(type(right_operand) == str):
                            right_operand = DirFuncs.getVarDir(right_operand)
                        Quadruples.add(QuadCont, operator, left_operand, right_operand, result)
                        PQTypes.add(result_Type)
                        PID.add(result)
                        QuadCont+=1
                    else:
                        print("ERROR: TYPE MISMATCH")
                        exit()
        @_('')
        def quad_5(self, p): # CREA EL CUADRUPLO CON / *
            global QuadCont
            global TempsCont
            global TempsBase
            global TempsBaseF
            global TempsContF
            if ((POper.empty() == False) and (PID.size() >= 2)):
                if ((POper.top() == '/') or (POper.top() == '*')):
                    right_operand = PID.pop()
                    right_type = PQTypes.pop()
                    left_operand = PID.pop()
                    left_type = PQTypes.pop()
                    operator = POper.pop()
                    result_Type = Cube.obtenerTipo(left_type, right_type, operator)
                    if(result_Type != 'error'):
                        
                        if(self.currentScope != 0):
                            result = TempsContF + TempsBaseF
                            TempsContF+=1
                        else:
                            result = TempsBase + TempsCont
                            TempsCont+=1
                        if(type(left_operand) == str):
                            left_operand = DirFuncs.getVarDir(left_operand)
                        if(type(right_operand) == str):
                            right_operand = DirFuncs.getVarDir(right_operand)
                        Quadruples.add(QuadCont, operator, left_operand, right_operand, result)
                        PQTypes.add(result_Type)
                        PID.add(result)
                        QuadCont+=1
                    else:
                        print("ERROR: TYPE MISMATCH")
                        exit()
            
        @_('')
        def quad_6(self, p): # PUSH FALSE BOTTOM MARK
            POper.add(p[-1])
            
        @_('')
        def quad_7(self, p): # POP FALSE BOTTOM MARK
            POper.pop()
           
        @_('')
        def quad_8(self, p): # Agrega RELOPS a la pila de operandos (!=)|(==)|(<=)|(>=)|(<)|(>)
            POper.add(p[-1])
            
        
        @_('')
        def quad_9(self, p): # CREA EL CUADRUPLO CON RELOPS (!=)|(==)|(<=)|(>=)|(<)|(>)
            global QuadCont
            global TempsCont
            global TempsBase
            global TempsContF
            if ((POper.empty() == False) and (PID.size() >= 2)):
                if ((POper.top() == '!=') or (POper.top() == '==')or (POper.top() == '<=')or (POper.top() == '>=')or (POper.top() == '<')or (POper.top() == '>')):
                    right_operand = PID.pop()
                    right_type = PQTypes.pop()
                    left_operand = PID.pop()
                    left_type = PQTypes.pop()
                    operator = POper.pop()
                    result_Type = Cube.obtenerTipo(left_type, right_type, operator)
                    if(result_Type != 'error'):
                        
                        if(self.currentScope != 0):
                            result = TempsContF + TempsBaseF
                            TempsContF+=1
                        else:
                            result = TempsBase + TempsCont
                            TempsCont+=1
                        if(type(left_operand) == str):
                            left_operand = DirFuncs.getVarDir(left_operand)
                        if(type(right_operand) == str):
                            right_operand = DirFuncs.getVarDir(right_operand)
                        Quadruples.add(QuadCont, operator, left_operand, right_operand, result)
                        PQTypes.add(result_Type)
                        PID.add(result)
                        QuadCont+=1
                    else:
                        print("ERROR: TYPE MISMATCH")
                        exit()
            
        @_('')
        def quad_10(self, p): # Agrega & o | a la Pila de Operandos
            POper.add(p[-1])
            
        @_('')
        def quad_11(self, p): # CREA EL CUADRUPLO CON & |

            global QuadCont
            global TempsCont
            global TempsBase
            global TempsBaseF
            global TempsContF
            
            if ((POper.empty() == False) and (PID.size() >= 2)):
                
                if ((POper.top() == '&') or (POper.top() == '|')):
                    
                    right_operand = PID.pop()
                    right_type = PQTypes.pop()
                    left_operand = PID.pop()
                    left_type = PQTypes.pop()
                    operator = POper.pop()
                    result_Type = Cube.obtenerTipo(left_type, right_type, operator)
                    if(result_Type != 'error'):
                        if(self.currentScope != 0):
                            result = TempsContF + TempsBaseF
                            TempsContF+=1
                        else:
                            result = TempsBase + TempsCont
                            TempsCont+=1
                        if(type(left_operand) == str):
                            left_operand = DirFuncs.getVarDir(left_operand)
                        if(type(right_operand) == str):
                            right_operand = DirFuncs.getVarDir(right_operand)
                        Quadruples.add(QuadCont, operator, left_operand, right_operand, result)
                        PQTypes.add(result_Type)
                        PID.add(result)
                        QuadCont+=1
                    else:
                        print("ERROR: TYPE MISMATCH")
                        exit()
        @_('')
        def quad_a(self, p): # CUADRUPLO DE ASIGNACION
            global QuadCont
        
            right_operand = PID.pop()
            right_type = PQTypes.pop()
            left_operand = PID.pop()
            left_type = PQTypes.pop()
            operator = '='
            
            result_Type = Cube.obtenerTipo(left_type, right_type, operator)
            if(result_Type != 'error'):
                result = left_operand
                if(type(result) == str):
                    result = DirFuncs.getVarDir(result)
                if(type(right_operand) == str):
                    right_operand = DirFuncs.getVarDir(right_operand)
                Quadruples.add(QuadCont, operator, right_operand, 0, result)
                QuadCont+=1
            else:
                print("ERROR: CANNOT ASSING VALUE", left_type ,'TO', right_type)
                exit()
            
        ###############            
        # PUNTOS NEURALGICOS: FUNCIONES PARA GOTOS Y FUNCIONES
        ############### 
        @_('')
        def quad_f1(self, p): # ACTUALIZA EL GOTO AL MAIN
            global QuadCont
            global nombrePrograma
            self.currentScope = 0
            self.currentFunction = nombrePrograma
            Salto = PSaltos.pop()
            Quadruples.updateCuad(Salto, QuadCont)
        @_('')
        def quad_if1(self, p): # CON BASE SI EL TIPO ES CORRECTO, AGREGA EL CUADRUPLO CON GOTOF Y 
                                #       HACE UN PUSH A LA PILA DE SALTOS // COMIENZA EL IF
            global QuadCont
            exp_type = PQTypes.pop()
            if(exp_type != 'int'):
                print('ERROR: TYPE MISMATCH')
                exit()
            else:
                result = PID.pop()
                if(type(result) == str):
                    result = DirFuncs.getVarDir(result)
                Quadruples.add(QuadCont, 'GOTOF', result, 0, '_')
                PSaltos.add(QuadCont)
                QuadCont+=1

        @_('')
        def quad_if2(self, p): # ACTUALIZA EL CUADRUPLO DE GOTOF // FINAL DEL IF 
            global QuadCont
            end = PSaltos.pop()
            Quadruples.updateCuad(end, QuadCont)
        @_('')
        def quad_if3(self, p): # HACE EL CUADRUPLO GOTO // COMIENZA EL ELSE
            global QuadCont
            Quadruples.add(QuadCont,'GOTO', 0, 0, '_')
            falseV = PSaltos.pop()
            PSaltos.add(QuadCont)
            QuadCont+=1
            Quadruples.updateCuad(falseV, QuadCont)
                    
        @_('')
        def quad_wd1(self, p): # DEJAMOS LA "SEMILLA" // COMIENZA EL WHILE
            global QuadCont
            PSaltos.add(QuadCont)
        @_('')
        def quad_wd2(self, p): # ACTUALIZA EL CUADRUPLO DE GOTOF // FINAL DEL IF 
            global QuadCont
            exp_type = PQTypes.pop()
            if(exp_type != 'int'):
                print('ERROR: TYPE MISMATCH')
            else:
                result = PID.pop()
                if(type(result) == str):
                    result = DirFuncs.getVarDir(result)
                Quadruples.add(QuadCont, 'GOTOF', result, 0, '_')
                QuadCont+=1
                PSaltos.add(QuadCont)
        @_('')
        def quad_wd3(self, p): # HACE EL CUADRUPLO GOTO // COMIENZA EL ELSE
            global QuadCont
            end = PSaltos.pop()
            returnS = PSaltos.pop()
            Quadruples.add(QuadCont, 'GOTO', 0, 0, returnS)
            QuadCont+=1
            Quadruples.updateCuad(returnS+1, QuadCont)
               
                    
        @_('')
        def quad_for1(self, p): # DEJAMOS LA "SEMILLA" // COMIENZA EL FOR
            global QuadCont
            global VControl
            var = p[-1]
            PID.add(var)
            typeV = DirFuncs.getVarType(var)
            PQTypes.add(typeV)
            if(typeV != 'int' and typeV != 'float'):
                print('ERROR: TYPE MISMATCH')
                exit()
        @_('')
        def quad_for2(self, p): # Cuadruplo para iniciar la variable con el primer valor
            global QuadCont
            global VControl
            global TempsCont
            global TempsBase
            global TempsContF
            global TempsBaseF

            exp_type = PQTypes.pop()
            if(exp_type != 'int'):
                print('ERROR: TYPE MISMATCH')
                exit()
            else:
                exp = PID.pop() # 0
                VControl = PID.pop() # i
                Control_type = PQTypes.pop()
                Tipo_Res = Cube.obtenerTipo(Control_type, exp_type, '=')
                if(Tipo_Res != 'error'):
                    exp_dir = DirFuncs.getVarDir(exp)
                    VControl_dir = DirFuncs.getVarDir(VControl)
                    Quadruples.add(QuadCont, '=', exp_dir, 0, VControl_dir)
                    PTypes.add(Tipo_Res)
                    PID.add(VControl)
                    QuadCont+=1
                else:
                    print('ERROR: TYPE MISMATCH')
                    exit()
        @_('')
        def quad_for3(self, p): # Crea cuadruplo para verificar que ID sea menor que el valor cada vez. Crea el gotof y hace Push a la pila de saltos. 
            global QuadCont
            global VControl
            global TempsBase
            global TempsCont
            global TempsContF
            global TempsBaseF
            
            exp_type = PQTypes.pop()
            if(exp_type != 'int' and exp_type != 'float'):
                print('ERROR: TYPE MISMATCH')
            else:
                exp = PID.pop()
                print(self.currentFunction)
                if(self.currentScope != 0):
                    resultF = TempsContF + TempsBaseF
                    TempsContF+=1
                else:
                    resultF = TempsBase + TempsCont
                    TempsCont+=1
                
                if(self.currentScope != 0):
                    result = TempsContF + TempsBaseF
                    TempsContF+=1
                else:
                    result = TempsBase + TempsCont
                    TempsCont+=1
                if(type(exp) == str):
                    exp = DirFuncs.getVarDir(exp)
                if(type(resultF) == str):
                    resultF = DirFuncs.getVarDir(resultF)
                Quadruples.add(QuadCont, '=', exp, 0, resultF)
        
                QuadCont+=1
                if(type(VControl) == str):
                    VControl = DirFuncs.getVarDir(VControl)
                if(type(resultF) == str):
                    resultF = DirFuncs.getVarDir(resultF)
                Quadruples.add(QuadCont, '<', VControl, resultF, result)
               
                PSaltos.add(QuadCont-1)
                QuadCont+=1
                Quadruples.add(QuadCont, 'GOTOF',result, 0 ,'_')
                QuadCont+=1
                
                PSaltos.add(QuadCont-1)
        @_('')
        def quad_for4(self, p): # Crea cuádruplo para sumarle 1 al ID. Actualiza el cuádruplo de gotof y hace un cuádruplo goto con pop de para volver al do.
            global QuadCont
            global VControl
            global TempsCont
            global TempsBase
            global TempsBaseF
            global TempsContF
            global CtesBase
            global CtesCont
            
            if(not DirFuncs.searchVar('globales', '1')):
                DirFuncs.addVariable('globales','1','int',CtesCont+CtesBase)
                CtesCont+=1
            if(type(VControl) == str):
                    VControl = DirFuncs.getVarDir(VControl)
            uno = DirFuncs.getVarDir('1')
            Quadruples.add(QuadCont, '+', VControl, uno, VControl)
            QuadCont+=1
            fin = PSaltos.pop()
            ret = PSaltos.pop()
            Quadruples.add(QuadCont, 'GOTO', 0, 0, ret)
            QuadCont+=1
            Quadruples.updateCuad(fin, QuadCont)
        
        ###############            
        # PUNTOS NEURALGICOS PARA FUNCIONES ESPECIALES
        # 'line','point','circle','arc','penup','pendown','color','size','clear', 'read', 'write'
        ############### 
        
        @_('')
        def quad_line(self, p):# Crea el cuadruplo para line 
            global QuadCont
            typeV = PQTypes.pop()
            var = PID.pop()
            typeV2 = PQTypes.pop()
            var2 = PID.pop()
            result_type = Cube.obtenerTipo(typeV, typeV2, 'LINE')
            if(result_type != 'error'):
                if(type(var2) == str):
                    var2 = DirFuncs.getVarDir(var2)
                if(type(var) == str):
                    var = DirFuncs.getVarDir(var)
                Quadruples.add(QuadCont, 'LINE', 0, var2, var)
                QuadCont+=1
            else:
                print('ERROR: TYPE MISMATCH')
                exit()
        @_('')
        def quad_point(self, p):# Crea el cuadruplo para punto 
            global QuadCont
            Quadruples.add(QuadCont, 'POINT', 0, 0, 0)
            QuadCont+=1
        @_('')
        def quad_circle(self, p):# Crea el cuadruplo para circulo 
            global QuadCont
            typeV = PQTypes.pop()
            var = PID.pop()
            result_type = Cube.obtenerTipo(typeV, '_', 'CIRCLE')
            if(result_type != 'error'):
                if(type(var) == str):
                    var = DirFuncs.getVarDir(var)
                Quadruples.add(QuadCont, 'CIRCLE', 0, 0, var)
                QuadCont+=1
            else:
                print('ERROR: TYPE MISMATCH')
                exit()
        @_('')
        def quad_arc(self, p):# Crea el cuadruplo para arc 
            global QuadCont
            typeV = PQTypes.pop()
            var = PID.pop()
            result_type = Cube.obtenerTipo(typeV, '_', 'ARC')
            if(result_type != 'error'):
                if(type(var) == str):
                    var = DirFuncs.getVarDir(var)
                Quadruples.add(QuadCont, 'ARC', 0, 0, var)
                QuadCont+=1
            else:
                print('ERROR: TYPE MISMATCH')
                exit()
        @_('')
        def quad_penup(self, p):# Crea el cuadruplo para penup 
            global QuadCont
            Quadruples.add(QuadCont, 'PENUP', 0, 0, 0)
            QuadCont+=1
        @_('')
        def quad_pendown(self, p):# Crea el cuadruplo para pendown 
            global QuadCont
            Quadruples.add(QuadCont, 'PENDOWN', 0, 0, 0)
            QuadCont+=1
        @_('')
        def quad_color(self, p): # Crea el cuadruplo para color 
            global QuadCont
            typeV = PQTypes.pop()
            b = PID.pop()
            typeV2 = PQTypes.pop()
            g = PID.pop()
            typeV3 = PQTypes.pop()
            r = PID.pop()
            if(typeV != 'int' or typeV2 != 'int' or typeV3 != 'int'):
                print('ERROR: TYPE MISMATCH')
                exit()
            else:
                if(type(r) == str):
                    r = DirFuncs.getVarDir(r)
                if(type(g) == str):
                    g = DirFuncs.getVarDir(g)
                if(type(b) == str):
                    b = DirFuncs.getVarDir(b)
                Quadruples.add(QuadCont, 'COLOR', r, g, b)
                QuadCont+=1
        @_('')
        def quad_size(self, p):# Crea el cuadruplo para size con expresion
            global QuadCont
            typeV = PQTypes.pop()
            var = PID.pop()
            result_type = Cube.obtenerTipo(typeV, '_', 'SIZE')
            if(result_type != 'error'):
                if(type(var) == str):
                    var = DirFuncs.getVarDir(var)
                Quadruples.add(QuadCont, 'SIZE', 0, 0, var)
                QuadCont+=1
            else:
                print('ERROR: TYPE MISMATCH')
                exit()
        @_('')
        def quad_clear(self, p):
            global QuadCont
            Quadruples.add(QuadCont, 'CLEAR', 0, 0, 0)
            QuadCont+=1
             
        @_('')
        def quad_write(self, p): # Crea el cuadruplo para WRITE con expresion
            global QuadCont
            typeV = PQTypes.pop()
            var = PID.pop()
            if(type(var) == str):
                var = DirFuncs.getVarDir(var)
            Quadruples.add(QuadCont, 'WRITE', 0, 0, var)
            QuadCont+=1
                    
        @_('')
        def quad_writeL(self, p): # Crea el cuadruplo para WRITE con letrero
            global QuadCont
            typeV = PQTypes.pop()
            var = PID.pop()
            if(type(var) == str):
                var = DirFuncs.getVarDir(var)
            Quadruples.add(QuadCont, 'WRITE', 0, 0, var)
            QuadCont+=1
            
        @_('')
        def quad_read(self, p): #Luego de verificar que la variable exista, crea el cuadruplo READ
            global QuadCont
            var = p[-1]
            typeV = DirFuncs.getVarType(var)
            if(typeV != None):
                if(type(var) == str):
                    var = DirFuncs.getVarDir(var)
                Quadruples.add(QuadCont, 'READ', 0, 0, var)
                QuadCont+=1
            else:
                print('ERROR: VAR', var,'NOT DECLARED')
                exit()        
         
        ###############            
        # FUNCIONES PARA AGREGAR A LAS TABLAS
        ############### 
        @_('')
        def funcs_1(self, p): # Agrega el programa, creando la tabla de funciones principal 
            global QuadCont
            global nombrePrograma
            nombrePrograma = p[-1]
            self.currentFunction = p[-1]
            self.currentScope = 'global'
            DirFuncs.addFunction(self.currentFunction, 'main', self.currentScope, QuadCont)
            Quadruples.add(QuadCont, 'GOTO', 0, 0, '_') #goto al main 
            PSaltos.add(QuadCont) #agrega el cuadruplo 1 a la pila de saltos
            self.currentScope = 0
            QuadCont+=1
            # print('funcs_1')
        @_('')
        def funcs_2(self, p): #Agrega Variable
            self.currentType = PTypes.pop()
            global IntCont
            global FloatCont
            global CharsCont
            global IntContF
            global FloatContF
            global CharsContF
            
            
            if(self.currentScope == 0):
            
                if(self.currentType == 'int'):
                    DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, IntBase+IntCont)
                    IntCont+=1
                if(self.currentType == 'float'):
                    DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, FloatBase+FloatCont)
                    FloatCont+=1
                if(self.currentType == 'char'):
                    DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, CharsBase+CharsCont)
                    CharsCont+=1
            else:
                if(self.currentType == 'int'):
                    DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, IntBaseF+IntContF)
                    IntContF+=1
                if(self.currentType == 'float'):
                    DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, FloatBaseF+FloatContF)
                    FloatContF+=1
                if(self.currentType == 'char'):
                    DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, CharsBaseF+CharsContF)
                    CharsContF+=1
        
        @_('')
        def funcs_2A(self, p): #Agrega el tipo a la pila de tipos
            self.currentType = PTypes.pop()
                                
        @_('')
        def funcs_3A(self, p): #Agrega Variable
            global LIM1
            global LIM2
            global M1
            global M2
            global R
            global sizeA
            LIM1 = p[-1]
            LIM1 = int(LIM1)
            R = LIM1+1
            
        @_('')
        def funcs_4A(self, p): #Agrega Variable
            global LIM1
            global LIM2
            global M1
            global M2
            global R
            global sizeA
            LIM2 = p[-1]
            LIM2 = int(LIM2)
            R = R*(LIM2+1)
        
        @_('')
        def funcs_5A(self, p): #Agrega Variable
            global LIM1
            global LIM2
            global M1
            global M2
            global R
            global sizeA
            global IntBase
            global IntCont
            global FloatBase
            global FloatCont
            global CharsBase
            global CharsCont
            global IntBaseF
            global IntContF
            global FloatBaseF
            global FloatContF
            global CharsBaseF
            global CharsContF
            M1 = R/(LIM1+1)
            M1 = int(M1)
            sizeA = LIM1+1
            if(M1 != 1):
                M2 = M1/(LIM2+1)
                M2 = int(M2)
                sizeA = LIM1*LIM2
                if(M2 != 1):
                    print('ERROR CON M2')
                    exit()
            
            if(self.currentType == 'int'):
                if(self.currentScope != 0):
                    DirFuncs.addArray(self.currentFunction, p[-7], self.currentType, IntBaseF+IntContF,sizeA,M1, M2, LIM1, LIM2)
                    IntContF+=sizeA
                else:
                    DirFuncs.addArray(self.currentFunction, p[-7], self.currentType, IntBase+IntCont,sizeA,M1, M2, LIM1, LIM2)
                    IntCont+=sizeA
            if(self.currentType == 'float'):
                if(self.currentScope != 0):
                    DirFuncs.addArray(self.currentFunction, p[-7], self.currentType, FloatBaseF+FloatContF,sizeA,M1, M2, LIM1, LIM2)
                    FloatContF+=sizeA
                else:
                    DirFuncs.addArray(self.currentFunction, p[-7], self.currentType, FloatBase+FloatCont,sizeA,M1, M2, LIM1, LIM2)
                    FloatCont+=sizeA
            if(self.currentType == 'char'):
                if(self.currentScope != 0):
                    DirFuncs.addArray(self.currentFunction, p[-7], self.currentType, CharsBase+CharsCont,sizeA,M1, M2, LIM1, LIM2)
                    CharsContF+=sizeA
                else:
                    DirFuncs.addArray(self.currentFunction, p[-7], self.currentType, CharsBase+CharsCont,sizeA,M1, M2, LIM1, LIM2)
                    CharsCont+=sizeA
                
            M1 = 1
            M2 = 0
            R = 1
            LIM1 = 1
            LIM2 = 1
            sizeA = 1
            
        @_('')
        def funcs_2_1(self, p): #Agrega Variable
            global IntCont
            global FloatCont
            global CharsCont
            if(self.currentType == 'int'):
                DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, IntBase+IntCont)
                IntCont+=1
            if(self.currentType == 'float'):
                DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, FloatBase+FloatCont)
                FloatCont+=1
            if(self.currentType == 'char'):
                DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, CharsBase+CharsCont)
                CharsCont+=1
        @_('')
        def funcs_3(self, p): #Agregar modulo a DirFuncs
            self.currentType = PTypes.pop()
            self.currentFunction = p[-1]
            self.currentScope +=1
            DirFuncs.addFunction(self.currentFunction, self.currentType, self.currentScope, QuadCont)
        @_('')
        def funcs_4(self, p): #Agregar parametros a modulo
            global ParCont
            DirFuncs.addParametros(self.currentFunction, ParCont ,self.currentType)
            ParCont+=1
        
        @_('')
        def funcs_cteI(self, p): #Agrega variable constante entera
            
            self.currentType = 'int'
            global CtesBase
            global CtesCont
            var = p[-1]
            if(p[-2] == '-'):
                var = '-'+var
            if(not DirFuncs.searchVar('globales', var)):
                DirFuncs.addVariable('globales', var, self.currentType, CtesCont+CtesBase)
                CtesCont+=1
        @_('')
        def funcs_cteC(self, p): #Agrega variable char 
            self.currentType = 'char'
            global CtesBase
            global CtesCont
            if(not DirFuncs.searchVar('globales', p[-1])):
                DirFuncs.addVariable('globales', p[-1], self.currentType, CtesCont+CtesBase)
                CtesCont+=1
        @_('')
        def funcs_cteF(self, p): #Agrega variable constante flotante
            self.currentType = 'float'
            global CtesBase
            global CtesCont
            if(not DirFuncs.searchVar('globales', p[-1])):
                DirFuncs.addVariable('globales', p[-1], self.currentType, CtesCont+CtesBase)
                CtesCont+=1
        @_('')
        def funcs_cteL(self, p): #Agrega constante Letrero

            self.currentType = 'letrero'
            global CtesBase
            global CtesCont
            if(not DirFuncs.searchVar('globales', p[-1])):
                DirFuncs.addVariable('globales', p[-1], self.currentType, CtesCont+CtesBase)
                CtesCont+=1
                       
        @_('')
        def funcs_r(self, p): #Agrega la variable constante que tendra el valor de retorno del modulo
            global CtesBase
            global CtesCont
            DirFuncs.addVariable('globales', 'return'+p[-2], self.currentType, CtesCont+CtesBase)
            CtesCont+=1
            
        @_('')
        def funcs_r2(self, p): # Crea cuadruplo para asignarle el valor al reutrn de la funcion donde este
            global QuadCont
            var = PID.pop()
            typeV = PQTypes.pop()
            varR = DirFuncs.getVarDir('return'+self.currentFunction)
            typeR = DirFuncs.getVarType('return'+self.currentFunction)
            result_type = Cube.obtenerTipo(typeV, typeR, '=')
            if(result_type != 'error'):
                if(type(var) == str):
                    var = DirFuncs.getVarDir(var)
                if(type(var) == str):
                    varR = DirFuncs.getVarDir(varR)
                Quadruples.add(QuadCont, '=', var, 0, varR)
                QuadCont+=1
            else:
                print('ERROR: TYPE MISMATCH')
                exit()
        
        @_('')
        def funcs_calls(self, p): # Verifica que la funcion haya sido declarada previamente
            self.currentFunction = p[-1]
            var = 'return'+p[-1]
            PID.add(var)
            
            tipo = DirFuncs.getVarType(var)
            PQTypes.add(tipo)
            
            if(not DirFuncs.search(self.currentFunction)):
                print('ERROR: FUNCTION', self.currentFunction, 'NOT DECLARED')
                exit()
        
        @_('')
        def funcs_calls2(self, p): #Crea cuadruplo ERA
            global QuadCont
            global ParCounter
            global ParamPointer
            Quadruples.add(QuadCont, 'ERA', 0 ,0, self.currentFunction)
            QuadCont+=1
        
        @_('')
        def funcs_calls3(self, p): #Verifica que el tipo de parametro dado concuerde con el que se declaro y crea el cuadruplo PARAM
            global QuadCont
            global TempsBase
            global TempsCont
            global TempsContF
            global TempsBaseF
            global ParamPointer
            global ParCounter
            argument = PID.pop()
            argumentType = PQTypes.pop()
            try:
                ParamPointer = DirFuncs.getParType(self.currentFunction, ParCounter)
            except:
                print('ERROR: WRONG NUMBER OF PARAMETERS. EXPECTED: 0')
                exit() 
            else:   
                print(ParamPointer)
                if(argumentType == ParamPointer):
                    if(type(argument) == str):
                        argument = DirFuncs.getVarDir(argument)
                    if(self.currentScope != 0):
                        result = TempsContF + TempsBaseF
                        TempsContF+=1
                    else:
                        result = TempsCont + TempsBase
                        TempsCont+=1
                    Quadruples.add(QuadCont,'PARAM', argument, ParCounter, result)    
                    QuadCont+=1
                    TempsCont+=1
                else:
                    print('ERROR: PARAM TYPE. EXPECTED:', ParamPointer, ', GIVEN:', argumentType)
                    exit()        
        @_('')
        def funcs_calls4(self, p): #Aumenta el counter de parametros y regresa error si se excede el numero de parametros
            global ParCounter
            global ParamPointer
            ParCounter+=1
            try:
                ParamPointer = DirFuncs.getParType(self.currentFunction, ParCounter)
            except:
                print('ERROR: WRONG NUMBER OF PARAMETERS. EXPECTED:', ParCounter)
                exit()
            else:
                ParamPointer = DirFuncs.getParType(self.currentFunction, ParCounter)
                        
        @_('')
        def funcs_calls5(self, p): #Regresa error si no se esperaban parametros
            global ParCounter
            global ParamPointer
            try:
                ParamPointer = DirFuncs.getParType(self.currentFunction, ParCounter+1)
            except:
                pass
            else:
                print('ERROR: WRONG NUMBER OF PARAMETERS. EXPECTED: 0')
                exit() 
            
        @_('')
        def funcs_calls6(self, p): #Crea cuadruplo GOSUB
            global QuadCont
            global ParCounter
            goTo = DirFuncs.getJump(self.currentFunction)
            Quadruples.add(QuadCont,'GOSUB', self.currentFunction, 0, goTo)    
            QuadCont+=1
            ParCounter = 1
        
        @_('')
        def funcs_calls7(self, p): # Agrega cuadruplo de End y reinicia los contadores de variables
            global QuadCont
            global IntContF
            global FloatContF   
            global CharsContF  
            global TempsContF
            Quadruples.add(QuadCont,'END', 0, 0, 0)    
            QuadCont+=1
            DirFuncs.addVarCant(self.currentFunction, IntContF,FloatContF,CharsContF, TempsContF)
            IntContF     = 0
            FloatContF   = 0
            CharsContF   = 0
            TempsContF   = 0
            # print('funcs_calls6')
        
        @_('')
        def quad_array1(self, p):
            global currentArray
            global LIM1
            global LIM2
            LIM1 = True
            LIM2 = False
            var = p[-1]
            currentArray = var
            PID.add(var)
            typeV = DirFuncs.getVarType(var)
            PQTypes.add(typeV)
            
        @_('')
        def quad_array2(self, p):
            global DIM 
            ID = PID.pop()
            typeV = PQTypes.pop()
            if(DirFuncs.checkIfArray(self.currentFunction, ID)):
               DIM = 1
               PDim.add(ID)
               PDim.add(DIM) 
               POper.add('(')
            else:
                print('ERROR: VAR', ID, 'NOT DECLARED AS ARRAY')
                exit()
            
        @_('')
        def quad_array3(self, p):
            global QuadCont
            global LIM1
            global LIM2
            global DIM
            global currentArray
            global TempsBase
            global TempsCont
            global TempsContF
            global TempsBaseF

            if(LIM1):
                lim = DirFuncs.getArrL(currentArray, 1)
                varDir = PID.top()
                varDir2 = DirFuncs.getVarDir(varDir)
                if(varDir2 != None):
                    varDir = varDir2
                Quadruples.add(QuadCont,'VERIFY',varDir,0, lim)
                QuadCont+=1
                m = DirFuncs.getArrM(currentArray, 1)
                var = PID.pop()
                var2 = DirFuncs.getVarDir(var)
                if(var2 != None):
                    var = var2
                if(self.currentScope != 0):
                    temp = TempsContF + TempsBaseF
                    TempsContF+=1
                else:
                    temp = TempsCont + TempsBase
                    TempsCont+=1
                Quadruples.add(QuadCont,'*T', var, m, temp)
                QuadCont+=1
                PID.add(temp)
              
                
            if(LIM2):
                lim = DirFuncs.getArrL(currentArray, 2)
                varDir = PID.top()
                varDir = DirFuncs.getVarDir(varDir)
                Quadruples.add(QuadCont,'VERIFY', varDir,0, lim)
                QuadCont+=1
                aux2 = PID.pop()
                aux1 = PID.pop()
                var = DirFuncs.getVarDir(currentArray)
                if(self.currentScope != 0):
                    temp = TempsContF + TempsBaseF
                    TempsContF+=1
                else:
                    temp = TempsBase+TempsCont
                    TempsCont +=1
                aux2 = DirFuncs.getVarDir(aux2)
                Quadruples.add(QuadCont,'+T2', aux1, aux2, temp)
                QuadCont+=1
                PID.add(temp)
            

        @_('')
        def quad_array4(self, p):
            global LIM1
            global LIM2
            LIM1 = False
            LIM2 = True
        @_('')
        def quad_array5(self, p):
            global currentArray
            global QuadCont
            global TempsCont
            global TempsBase
            global TempsContF
            global TempsBaseF
            aux1 = PID.pop()
            
            var = DirFuncs.getVarDir(currentArray)
            if(self.currentScope != 0):
                temp = TempsContF + TempsBaseF
                TempsContF+=1
            else:
                temp = TempsBase+TempsCont
                TempsCont +=1
            
            Quadruples.add(QuadCont,'+T', aux1, var, temp)
            PID.add(temp)
            QuadCont+=1
            TempsCont+=1
            POper.pop()
            
            
        @_('')
        def current_typeV(self, p):
            PTypes.add('void')
        

        # FUNCION PRINCIPAL DEL PROGRAMA 
if __name__ == '__main__':

    file = open("main.txt", 'r')
    masterline = ""

    for line in file:
        masterline = masterline + line.strip()
    
    lexer = MeMyselfLexer()
    parser = MeMyselfParser()
    cuadruplo = cuadruplos()
    result = parser.parse(lexer.tokenize(masterline))
    file.close()
    # DirFuncs.printFunction()
    # print('Cuadruplos')
    # Quadruples.print()
    
    #Llama a la maquina virtual. De parametros envia los cuadruplos, el directorio, y los temporales que se necesitan
    VirtualMachine = MaquinaVirtual(Quadruples, DirFuncs, TempsCont) 
    VirtualMachine.main()
