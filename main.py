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
ParK        = 0
QuadCont    = 1


class MeMyselfLexer(Lexer):
        tokens = { PROGRAM, VAR, MODULE, VOID, INT, FLOAT, ASSIGN, CHAR, RELOP, 
                    IF, ELSE, FOR, TO, THEN, DO, WHILE, RETURN, PLUS, MAIN, TO, WRITE, READ, 
                    MINUS, TIMES, DIVIDE, CTEINT, CTEFLOAT, CTECHAR,  
                    LETRERO, ID, LOGICOS,
                    LINE, POINT, CIRCLE, ARC, PENUP, PENDOWN, COLOR, SIZE, CLEAR}

        ignore = ' \t'
        literals = { ';', ':', '(', ')', '{', '}',',', '"'}

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
        @_('"," LETRERO funcs_cteL quad_let quad_writeL  printe2', '"," exp quad_write printe2', '')
        def printe2(self, p):
            pass

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
        @_('estatuto', 'estatutos')
        def estatutos(self, p):
            pass

        #       ESTATUTO
        @_('funcionD estatuto', 'asignacion estatuto', 'lectura estatuto', 'escritura estatuto', 'decision estatuto', 'repeticiondo estatuto', 'repeticionfor estatuto', 'exp estatuto', 'especiales estatuto', '')
        def estatuto(self, p):
            pass
        
        #       ASIGNACION
        @_('ID quad_1 ASSIGN exp quad_a ";"', 'ID quad_1 ASSIGN funcionD quad_a')
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
        # @_('comparar LOGICOS quad_19 comparar', 'comparar')
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
        # @_('TIMES quad_3 factor termino2', 'DIVIDE quad_3 factor termino2','')
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
        #@_('"(" quad_6 expresion ")" quad_7','PLUS varcte',  'MINUS varcte', 'varcte')
        @_('"(" quad_6 exp ")" quad_7','PLUS varcte',  'MINUS varcte', 'varcte')
        def factor(self,p):
            pass

        #       VARCTE
        @_('ID quad_1','CTEINT funcs_cteI quad_cteI','CTEFLOAT funcs_cteF quad_cteF','CTECHAR funcs_cteC quad_cteC','LETRERO funcs_cteL quad_let')
        def varcte(self, p):
            pass

        #       VARS
        @_('VAR tipov ":" ID funcs_2 vars2 ";"', '')
        def vars(self, p):
            pass
        @_('"," ID funcs_2_1 vars2', '')
        def vars2(self, p):
            pass
        
        #       VARS
        @_('VAR tipov ":" ID funcs_2 vars2 ";"', '')
        def vDim(self, p):
            pass
        @_('"," ID funcs_2_1 vars2', '')
        def vDim2(self, p):
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
            # print('quad_cteI')
        @_('')
        def quad_cteF(self, p): # HACER PUSH A LOS STACKS CON CTE FLOATS
            cte = p[-2]
            PID.add(cte)
            PQTypes.add('float')
            # print('quad_cteF')
            
        @_('')
        def quad_cteC(self, p): # HACER PUSH A LOS STACKS CON CTE INTS
            cte = p[-2]
            PID.add(cte)
            PQTypes.add('char')
            # print('quad_cteI')
        @_('')
        def quad_let(self, p): # HACER PUSH A LOS STACKS CON LETREROS
            print('--------------- ENTRA A LETRERO --------')
            cte = p[-2]
            PID.add(cte)
            PQTypes.add('letrero')
            print('quad_cteS')
        @_('')
        def quad_1(self, p): # HACER PUSH A LOS STACKS CON EL ID DE LA VARIABLE Y SU TIPO
            PID.add(p[-1])
            tipo = DirFuncs.getVarType(p[-1])
            if tipo == None:
                print('ERROR: VARIABLE', p[-1], 'NOT DECLARED')
                exit()
            else:
                PQTypes.add(tipo)
            # PID.print()
            # PQTypes.print()
            # print('quad_1')
        @_('')
        def quad_2(self, p): #AGREGAR + o - AL POper 
            print(p[-1])
            POper.add(p[-1])
            # POper.print()
            # print('quad_2')
        @_('')
        def quad_3(self, p): #AGREGAR * o / AL POper
            POper.add(p[-1])
            # POper.print()
            # print('quad_3')    
        @_('')
        def quad_4(self, p): # CREA EL CUADRUPLO CON + -
            global QuadCont
            global TempsCont
            global TempsBase
            POper.print()
            # PID.print()
            if ((POper.empty() == False) and (PID.size() >= 2)):
                # print('entra al primer if')
                if ((POper.top() == '+') or (POper.top() == '-')):
                    # print("entra al segundo if")
                    right_operand = PID.pop()
                    right_type = PQTypes.pop()
                    left_operand = PID.pop()
                    left_type = PQTypes.pop()
                    # print('RO:', right_operand, '| RT: ', right_type, '| LO:', left_operand, '| LT: ', left_type)
                    operator = POper.pop()
                    # print('CUBE:', left_type, right_type, operator)
                    result_Type = Cube.obtenerTipo(left_type, right_type, operator)
                    if(result_Type != 'error'):
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
                        #1 Quadruples.print()
                    else:
                        print("ERROR: TYPE MISMATCH")
                        exit()
            # print('quad_4')
        @_('')
        def quad_5(self, p): # CREA EL CUADRUPLO CON / *
            global QuadCont
            global TempsCont
            global TempsBase
            # POper.print()
            # PID.print()
            if ((POper.empty() == False) and (PID.size() >= 2)):
                # print('entra al primer if')
                if ((POper.top() == '/') or (POper.top() == '*')):
                    # print("entra al segundo if")
                    right_operand = PID.pop()
                    right_type = PQTypes.pop()
                    left_operand = PID.pop()
                    left_type = PQTypes.pop()
                    # print('RO:', right_operand, '| RT: ', right_type, '| LO:', left_operand, '| LT: ', left_type)
                    operator = POper.pop()
                    # print('CUBE:', left_type, right_type, operator)
                    result_Type = Cube.obtenerTipo(left_type, right_type, operator)
                    if(result_Type != 'error'):
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
                        #1 Quadruples.print()
                    else:
                        print("ERROR: TYPE MISMATCH")
                        exit()
            # print('quad_5')
            
        @_('')
        def quad_6(self, p): # PUSH FALSE BOTTOM MARK
            POper.add(p[-1])
            # POper.print()
            # print('quad_6')
        @_('')
        def quad_7(self, p): # POP FALSE BOTTOM MARK
            POper.pop()
            # POper.print()
            # print('quad_7')
        @_('')
        def quad_8(self, p): # POP FALSE BOTTOM MARK
            POper.add(p[-1])
            # POper.print()
            # print('quad_7')
        
        @_('')
        def quad_9(self, p): # CREA EL CUADRUPLO CON RELOPS (!=)|(==)|(<=)|(>=)|(<)|(>)
            global QuadCont
            global TempsCont
            global TempsBase
            # POper.print()
            # PID.print()
            if ((POper.empty() == False) and (PID.size() >= 2)):
                # print('entra al primer if')
                if ((POper.top() == '!=') or (POper.top() == '==')or (POper.top() == '<=')or (POper.top() == '>=')or (POper.top() == '<')or (POper.top() == '>')):
                    # print("entra al segundo if")
                    right_operand = PID.pop()
                    right_type = PQTypes.pop()
                    left_operand = PID.pop()
                    left_type = PQTypes.pop()
                    # print('RO:', right_operand, '| RT: ', right_type, '| LO:', left_operand, '| LT: ', left_type)
                    operator = POper.pop()
                    # print('CUBE:', left_type, right_type, operator)
                    result_Type = Cube.obtenerTipo(left_type, right_type, operator)
                    if(result_Type != 'error'):
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
                        #1 Quadruples.print()
                    else:
                        print("ERROR: TYPE MISMATCH")
                        exit()
            # print('quad_9')
            
        @_('')
        def quad_10(self, p): # POP FALSE BOTTOM MARK
            POper.add(p[-1])
            # POper.print()
            # print('quad_10')
        @_('')
        def quad_11(self, p): # CREA EL CUADRUPLO CON & |
            # print('AND Y OR')
            global QuadCont
            global TempsCont
            global TempsBase
            # POper.print()
            # PID.print()
            # PQTypes.print()
            if ((POper.empty() == False) and (PID.size() >= 2)):
                # print('entra al primer if')
                if ((POper.top() == '&') or (POper.top() == '|')):
                    # print("entra al segundo if")
                    right_operand = PID.pop()
                    right_type = PQTypes.pop()
                    left_operand = PID.pop()
                    left_type = PQTypes.pop()
                    # print('RO:', right_operand, '| RT: ', right_type, '| LO:', left_operand, '| LT: ', left_type)
                    operator = POper.pop()
                    # print('CUBE:', left_type, right_type, operator)
                    result_Type = Cube.obtenerTipo(left_type, right_type, operator)
                    if(result_Type != 'error'):
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
                        #1 Quadruples.print()
                    else:
                        print("ERROR: TYPE MISMATCH")
                        exit()
            # print('quad_11')
        @_('')
        def quad_a(self, p): # CUADRUPLO DE ASIGNACION
            global QuadCont
            # PID.print()
            # PQTypes.print()
            # if ((PID.size() >= 2)):
            PID.print()
            right_operand = PID.pop()
            right_type = PQTypes.pop()
            left_operand = PID.pop()
            left_type = PQTypes.pop()
            operator = '='
            result_Type = Cube.obtenerTipo(left_type, right_type, operator)
            if(result_Type != 'error'):
                result = left_operand
                # print('RESULT ',result)
                if(type(result) == str):
                    result = DirFuncs.getVarDir(result)
                if(type(right_operand) == str):
                    right_operand = DirFuncs.getVarDir(right_operand)
                # print('RESULT memory ',result)
                Quadruples.add(QuadCont, operator, right_operand, 0, result)
                QuadCont+=1
                #1 Quadruples.print()
            else:
                print("ERROR: CANNOT ASSING VALUE", left_type ,'TO', right_type)
                exit()
            # print('quad_a')
            
        ###############            
        # PUNTOS NEURALGICOS: FUNCIONES PARA GOTOS Y FUNCIONES
        ############### 
        @_('')
        def quad_f1(self, p): # ACTUALIZA EL GOTO AL MAIN
            global QuadCont
            # PSaltos.print()
            Salto = PSaltos.pop()
            Quadruples.updateCuad(Salto, QuadCont)
            # print('quad_f1')
        @_('')
        def quad_if1(self, p): # CON BASE SI EL TIPO ES CORRECTO, AGREGA EL CUADRUPLO CON GOTOF Y 
                                #       HACE UN PUSH A LA PILA DE SALTOS // COMIENZA EL IF
            global QuadCont
            # PTypes.print()
            # PSaltos.print()
            # print('pqtypes')
            # PQTypes.print()
            # print('pid')
            # PID.print()
            # print('ptypes')
            # PTypes.print()
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
            # print('quad_if1')
        @_('')
        def quad_if2(self, p): # ACTUALIZA EL CUADRUPLO DE GOTOF // FINAL DEL IF 
            global QuadCont
            # PTypes.print()
            # PSaltos.print()
            end = PSaltos.pop()
            Quadruples.updateCuad(end, QuadCont)
            # print('quad_if2')
        @_('')
        def quad_if3(self, p): # HACE EL CUADRUPLO GOTO // COMIENZA EL ELSE
            global QuadCont
            # PQTypes.print()
            # PSaltos.print()
            Quadruples.add(QuadCont,'GOTO', 0, 0, '_')
            falseV = PSaltos.pop()
            PSaltos.add(QuadCont)
            QuadCont+=1
            Quadruples.updateCuad(falseV, QuadCont)
            # print('quad_if3')
        
        @_('')
        def quad_wd1(self, p): # DEJAMOS LA "SEMILLA" // COMIENZA EL WHILE
            global QuadCont
            # PTypes.print()
            # PSaltos.print()
            PSaltos.add(QuadCont)
            # print('quad_wd1')
        @_('')
        def quad_wd2(self, p): # ACTUALIZA EL CUADRUPLO DE GOTOF // FINAL DEL IF 
            global QuadCont
            # PQTypes.print()
            # PSaltos.print()
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
            # print('quad_wd2')
        @_('')
        def quad_wd3(self, p): # HACE EL CUADRUPLO GOTO // COMIENZA EL ELSE
            global QuadCont
            # PTypes.print()
            # PSaltos.print()
            end = PSaltos.pop()
            returnS = PSaltos.pop()
            Quadruples.add(QuadCont, 'GOTO', 0, 0, returnS)
            QuadCont+=1
            Quadruples.updateCuad(returnS+1, QuadCont)
            # print('quad_wd3')      
                    
        @_('')
        def quad_for1(self, p): # DEJAMOS LA "SEMILLA" // COMIENZA EL FOR
            global QuadCont
            global VControl
            var = p[-1]
            PID.add(var)
            # print(var)
            typeV = DirFuncs.getVarType(var)
            PQTypes.add(typeV)
            # print(typeV)
            if(typeV != 'int' and typeV != 'float'):
                print('ERROR: TYPE MISMATCH')
                exit()
            # print('quad_for1')
        @_('')
        def quad_for2(self, p): # DEJAMOS LA "SEMILLA" // COMIENZA EL FOR
            global QuadCont
            global VControl
            global TempsCont
            global TempsBase

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
                    # result = TempsBase + TempsCont
                    # TempsCont+=1
                    # print(exp, VControl)
                    exp_dir = DirFuncs.getVarDir(exp)
                    VControl_dir = DirFuncs.getVarDir(VControl)
                    Quadruples.add(QuadCont, '=', exp_dir, 0, VControl_dir)
                    # Quadruples.print()
                    # print('----')
                    PTypes.add(Tipo_Res)
                    PID.add(VControl)
                    QuadCont+=1
                else:
                    print('ERROR: TYPE MISMATCH')
                    exit()
            # print('quad_for2')
        @_('')
        def quad_for3(self, p): # DEJAMOS LA "SEMILLA" // COMIENZA EL FOR
            global QuadCont
            global VControl
            global TempsBase
            global TempsCont
            
            exp_type = PQTypes.pop()
            if(exp_type != 'int' and exp_type != 'float'):
                print('ERROR: TYPE MISMATCH')
            else:
                exp = PID.pop()
                resultF = TempsBase + TempsCont
                TempsCont+=1
                result = TempsBase + TempsCont
                
                if(type(exp) == str):
                    exp = DirFuncs.getVarDir(exp)
                if(type(resultF) == str):
                    resultF = DirFuncs.getVarDir(resultF)
                Quadruples.add(QuadCont, '=', exp, 0, resultF)
                # Quadruples.print()
                # print('----')
                QuadCont+=1
                if(type(VControl) == str):
                    VControl = DirFuncs.getVarDir(VControl)
                if(type(resultF) == str):
                    resultF = DirFuncs.getVarDir(resultF)
                Quadruples.add(QuadCont, '<', VControl, resultF, result)
                # Quadruples.print()
                # print('----')
                PSaltos.add(QuadCont-1)
                QuadCont+=1
                Quadruples.add(QuadCont, 'GOTOF',result, 0 ,'_')
                QuadCont+=1
                # Quadruples.print()
                # print('----')
                PSaltos.add(QuadCont-1)
            # print('quad_for3')
        @_('')
        def quad_for4(self, p): # DEJAMOS LA "SEMILLA" // COMIENZA EL FOR
            global QuadCont
            global VControl
            global TempsCont
            global TempsBase
            global CtesBase
            global CtesCont
            # print('VControl',VControl)
            if(not DirFuncs.searchVar('globales', '1')):
                DirFuncs.addVariable('globales','1','int',CtesCont+CtesBase)
                CtesCont+=1
            if(type(VControl) == str):
                    VControl = DirFuncs.getVarDir(VControl)
            print('cuaduplo added + at', QuadCont)
            uno = DirFuncs.getVarDir('1')
            Quadruples.add(QuadCont, '+', VControl, uno, VControl)
            QuadCont+=1
            fin = PSaltos.pop()
            ret = PSaltos.pop()
            # print(fin, ret)
            Quadruples.add(QuadCont, 'GOTO', 0, 0, ret)
            # Quadruples.print()
            # print('----')
            QuadCont+=1
            # print(fin, QuadCont)
            Quadruples.updateCuad(fin, QuadCont)
            # print('quad_for4')
        
        ###############            
        # PUNTOS NEURALGICOS PARA FUNCIONES ESPECIALES
        # 'line','point','circle','arc','penup','pendown','color','size','clear', 'read', 'write'
        ############### 
        
        @_('')
        def quad_line(self, p):
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
            print('quad_line')
        @_('')
        def quad_point(self, p):
            global QuadCont
            Quadruples.add(QuadCont, 'POINT', 0, 0, 0)
            QuadCont+=1
            print('quad_point') 
        @_('')
        def quad_circle(self, p):
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
            # print('quad_circle') 
        @_('')
        def quad_arc(self, p):
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
            # print('quad_arc') 
        @_('')
        def quad_penup(self, p):
            global QuadCont
            Quadruples.add(QuadCont, 'PENUP', 0, 0, 0)
            QuadCont+=1
            # print('quad_penup')
        @_('')
        def quad_pendown(self, p):
            global QuadCont
            Quadruples.add(QuadCont, 'PENDOWN', 0, 0, 0)
            QuadCont+=1
            # print('quad_pendown') 
        @_('')
        def quad_color(self, p):
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
            # print('quad_color') 
        @_('')
        def quad_size(self, p):
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
            # print('quad_size')
        @_('')
        def quad_clear(self, p):
            global QuadCont
            Quadruples.add(QuadCont, 'CLEAR', 0, 0, 0)
            QuadCont+=1
            # print('quad_clear')
             
        @_('')
        def quad_write(self, p):
            global QuadCont
            typeV = PQTypes.pop()
            var = PID.pop()
            if(type(var) == str):
                var = DirFuncs.getVarDir(var)
            Quadruples.add(QuadCont, 'WRITE', 0, 0, var)
            QuadCont+=1
            # print('quad_write')
        
        @_('')
        def quad_writeL(self, p):
            global QuadCont
            typeV = PQTypes.pop()
            var = PID.pop()
            if(type(var) == str):
                var = DirFuncs.getVarDir(var)
            Quadruples.add(QuadCont, 'WRITE', 0, 0, var)
            QuadCont+=1
            # print('quad_write')
            
        @_('')
        def quad_read(self, p):
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
            # print('quad_read')
        
         
        ###############            
        # FUNCIONES PARA AGREGAR A LAS TABLAS
        ############### 
        @_('')
        def funcs_1(self, p): # Agrega el programa
            global QuadCont
            self.currentFunction = p[-1]
            self.currentScope = 'global'
            DirFuncs.addFunction(self.currentFunction, 'main', self.currentScope, QuadCont)
            Quadruples.add(QuadCont, 'GOTO', 0, 0, '_')
            PSaltos.add(QuadCont)
            QuadCont+=1
            # print('funcs_1')
        @_('')
        def funcs_2(self, p): #Agrega Variable
            self.currentType = PTypes.pop()
            global IntCont
            global FloatCont
            global CharsCont
            #print('IntCont:', IntCont, 'FloatCont', FloatCont,'CharsCont', CharsCont)
            if(self.currentType == 'int'):
                DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, IntBase+IntCont)
                IntCont+=1
            if(self.currentType == 'float'):
                DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, FloatBase+FloatCont)
                FloatCont+=1
            if(self.currentType == 'char'):
                DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, CharsBase+CharsCont)
                CharsCont+=1
            # print('funcs_2')
        @_('')
        def funcs_2_1(self, p): #Agrega Variable
            global IntCont
            global FloatCont
            global CharsCont
            #print('IntCont:', IntCont, 'FloatCont', FloatCont,'CharsCont', CharsCont)
            if(self.currentType == 'int'):
                DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, IntBase+IntCont)
                IntCont+=1
            if(self.currentType == 'float'):
                DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, FloatBase+FloatCont)
                FloatCont+=1
            if(self.currentType == 'char'):
                DirFuncs.addVariable(self.currentFunction, p[-1], self.currentType, CharsBase+CharsCont)
                CharsCont+=1
            # print('funcs_2')
        @_('')
        def funcs_3(self, p): #Agregar modulo a DirFuncs
            self.currentType = PTypes.pop()
            # print('current Type:', self.currentType)
            self.currentFunction = p[-1]
            # print('current function: ', self.currentFunction)
            DirFuncs.addFunction(self.currentFunction, self.currentType, 'module'+str(self.currentFunction), QuadCont)
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
            #print('IntCont:', IntCont, 'FloatCont', FloatCont,'CharsCont', CharsCont)
            if(not DirFuncs.searchVar('globales', var)):
                DirFuncs.addVariable('globales', var, self.currentType, CtesCont+CtesBase)
                CtesCont+=1
            # print('funcs_2')
        @_('')
        def funcs_cteC(self, p): #Agrega variable constante entera
            self.currentType = 'char'
            global CtesBase
            global CtesCont
            #print('IntCont:', IntCont, 'FloatCont', FloatCont,'CharsCont', CharsCont)
            if(not DirFuncs.searchVar('globales', p[-1])):
                DirFuncs.addVariable('globales', p[-1], self.currentType, CtesCont+CtesBase)
                CtesCont+=1
            # print('funcs_2')
        @_('')
        def funcs_cteF(self, p): #Agrega variable constante entera
            self.currentType = 'float'
            global CtesBase
            global CtesCont
            #print('IntCont:', IntCont, 'FloatCont', FloatCont,'CharsCont', CharsCont)
            if(not DirFuncs.searchVar('globales', p[-1])):
                DirFuncs.addVariable('globales', p[-1], self.currentType, CtesCont+CtesBase)
                CtesCont+=1
            # print('funcs_2')
        @_('')
        def funcs_cteL(self, p): #Agrega variable constante entera
            print('--------------- ENTRA A LETRERO FUNCS --------')
            self.currentType = 'letrero'
            global CtesBase
            global CtesCont
            #print('IntCont:', IntCont, 'FloatCont', FloatCont,'CharsCont', CharsCont)
            if(not DirFuncs.searchVar('globales', p[-1])):
                DirFuncs.addVariable('globales', p[-1], self.currentType, CtesCont+CtesBase)
                CtesCont+=1
            # print('funcs_2')
                       
        @_('')
        def funcs_r(self, p):
            global CtesBase
            global CtesCont
            #print('IntCont:', IntCont, 'FloatCont', FloatCont,'CharsCont', CharsCont)
            DirFuncs.addVariable('globales', 'return'+p[-2], self.currentType, CtesCont+CtesBase)
            CtesCont+=1
            # print('funcs_r')
            
        @_('')
        def funcs_r2(self, p):
            global QuadCont
            var = PID.pop()
            typeV = PQTypes.pop()
            varR = DirFuncs.getVarDir('return'+self.currentFunction)
            typeR = DirFuncs.getVarType('return'+self.currentFunction)
            # DirFuncs.printFunction()
            # print(var, typeV, varR, typeR)
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
            # print('funcs_r2')
        
        @_('')
        def funcs_calls(self, p):
            self.currentFunction = p[-1]
            var = 'return'+p[-1]
            PID.add(var)
            PID.print()
            tipo = DirFuncs.getVarType(var)
            PQTypes.add(tipo)
            # print(DirFuncs.search(func))
            if(not DirFuncs.search(self.currentFunction)):
                print('ERROR: FUNCTION', self.currentFunction, 'NOT DECLARED')
                exit()
            # print('funcs_calls')
        
        @_('')
        def funcs_calls2(self, p):
            global QuadCont
            global ParK
            global ParamPointer
            Quadruples.add(QuadCont, 'ERA', 0 ,0, self.currentFunction)
            QuadCont+=1
            ParK = 1
            # print(DirFuncs.getParType(self.currentFunction, ParK))
            ParamPointer = DirFuncs.getParType(self.currentFunction, ParK)
            # print(DirFuncs.getParType(self.currentFunction, ParK))
            # print('funcs_calls2')
        
        @_('')
        def funcs_calls3(self, p):
            global QuadCont
            global TempsBase
            global TempsCont
            global ParamPointer
            global ParK
            # print('PQTypes')
            # PQTypes.print()
            # print('PTypes')
            # PTypes.print()
            argument = PID.pop()
            # print('argument', argument)
            # PQTypes.add(DirFuncs.getVarType(argument))
            argumentType = PQTypes.pop()
            # print('ParK',ParK)
            # print('Param pointer',ParamPointer)
            # print('argument type',argumentType)
            if(argumentType == ParamPointer):
                if(type(argument) == str):
                    argument = DirFuncs.getVarDir(argument)
                Quadruples.add(QuadCont,'PARAM', argument, ParK, TempsBase+TempsCont)    
                QuadCont+=1
                TempsCont+=1
            else:
                print('ERROR: PARAM TYPE. EXPECTED:', ParamPointer, ', GIVEN:', argumentType)
                exit()
            # print('funcs_calls3')
        
        @_('')
        def funcs_calls4(self, p):
            global ParK
            global ParamPointer
            ParK+=1
            try:
                ParamPointer = DirFuncs.getParType(self.currentFunction, ParK)
            except:
                print('ERROR: WRONG NUMBER OF PARAMETERS')
                exit()
            else:
                ParamPointer = DirFuncs.getParType(self.currentFunction, ParK)
                
            # print('funcs_calls4')
        
        @_('')
        def funcs_calls5(self, p):
            global ParK
            global ParamPointer
            try:
                ParamPointer = DirFuncs.getParType(self.currentFunction, ParK+1)
            except:
                ParamPointer = DirFuncs.getParType(self.currentFunction, ParK)
            else:
                print('ERROR: WRONG NUMBER OF PARAMETERS')
                exit()
            # print('funcs_calls5')
            
        @_('')
        def funcs_calls6(self, p):
            global QuadCont
            # print('CURRENT FUNCTION', self.currentFunction)
            goTo = DirFuncs.getJump(self.currentFunction)
            # print('GOTO', goTo)
            Quadruples.add(QuadCont,'GOSUB', self.currentFunction, 0, goTo)    
            QuadCont+=1
            # print('funcs_calls6')
        
        @_('')
        def funcs_calls7(self, p):
            global QuadCont
            # print('CURRENT FUNCTION', self.currentFunction)
            # print('GOTO', goTo)
            Quadruples.add(QuadCont,'END', 0, 0, 0)    
            QuadCont+=1
            # print('funcs_calls6')
            
        @_('')
        def current_typeV(self, p):
            PTypes.add('void')
            # print('current_typeV')
        

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
    #print(result)
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
    DirFuncs.printFunction()
    print('Cuadruplos')
    Quadruples.print()
    print('PID')
    PID.print()
    print('PTypes')
    PTypes.print()
    print('PQTypes')
    PQTypes.print()
    print('PPar')
    PPar.print()
    VirtualMachine = MaquinaVirtual(Quadruples, DirFuncs, TempsCont)
    VirtualMachine.main()
