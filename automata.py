#Función del Automata
def Automata(cadenaUsuario): 
        #Se inicializan las variables
        elementos=[]
        estado = 0
        indice = 0
        #Se le agrega al final de cadenaUsuario el símbolo $ (fin de cadena) y se guarda en la variable cadena 
        cadena=cadenaUsuario+'$'
        #Mientras el indice sea menor a la longitud de la cadena y se encuentre en el estado inicial
        while(indice<=(len(cadena)-1)  and estado==0):  
                #Se inicializan las siguientes variables
                lexema=''
                token='error'
                num=-1
                #Mientras el indice sea menor a la longitud de la cadena y NO se encuentre en el estado 20
                while(indice<=(len(cadena)-1) and estado!=20):
                    if estado==0:#Si está en el estado inicial
                        #Si en la posición cadena[indice] hay espacio en blanco
                        if(cadena[indice].isspace()):
                            estado=0 #El estado se establece como el inicial
                        #Si en la posición cadena[indice] hay una letra o un guión bajo
                        elif cadena[indice].isalpha() or cadena[indice]=='_':
                            estado=4 #La variable estado se establece con el número 4
                            lexema+=cadena[indice] #Al lexema se le agrega el contenido de cadena[indice]
                            token='identificador' #El token se define como un identificador
                            num=0 #La variable num se establece con el número 0
                        #Si en la posición cadena[indice] hay un $ (fin de cadena)
                        elif cadena[indice]=='$':
                            estado=20 #Se establece el estado como el final
                            lexema+=cadena[indice] #Al lexema se le agrega el contenido de cadena[indice]
                            token='$'  #El token se define como un signo de pesos o final de cadena
                            num=23 #La variable num se establece con el número 23
                        elif cadena[indice].isdigit():
                            lexema+=cadena[indice]
                            token='entero'
                            estado=6 
                            num=1
                        elif cadena[indice]=='"':
                            lexema+=cadena[indice]
                            estado=11
                            indice+=1
                        elif cadena[indice]=='=':
                            lexema+=cadena[indice]
                            token='='
                            estado=5  
                            num=18  
                        elif cadena[indice]=='+' or cadena[indice]=='-':
                            lexema+=cadena[indice]
                            token='opSuma'
                            estado=20 
                            num=5 
                        elif cadena[indice]=='*' or cadena[indice]=='/':
                            lexema+=cadena[indice]
                            token='opMul'
                            estado=20 
                            num=6
                        elif cadena[indice]=='<' or cadena[indice]=='>':
                            lexema+=cadena[indice]
                            token='opRelac'
                            estado=12
                            num=7 
                        elif cadena[indice]=='|':
                            lexema+=cadena[indice]
                            estado=13  
                        elif cadena[indice]=='&':
                            lexema+=cadena[indice]
                            estado=14 
                        elif cadena[indice]=='!':
                            lexema+=cadena[indice]
                            token='opNot'
                            estado=10 
                            num=10   
                        elif cadena[indice]==';':
                            lexema+=cadena[indice]
                            token=';'
                            estado=20 
                            num=12 
                        elif cadena[indice]==',':
                            lexema+=cadena[indice]
                            token=','
                            estado=20 
                            num=13 
                        elif cadena[indice]=='(':
                            lexema+=cadena[indice]
                            token='('
                            estado=20 
                            num=14 
                        elif cadena[indice]==')':
                            lexema+=cadena[indice]
                            token=')'
                            estado=20 
                            num=15
                        elif cadena[indice]=='{':
                            lexema+=cadena[indice]
                            token='{'
                            estado=20 
                            num=16 
                        elif cadena[indice]=='}':
                            lexema+=cadena[indice]
                            token='}'
                            estado=20 
                            num=17
                        #Si NO hay un espacio en blanco o alguno de los tokens válidos       
                        else:
                            estado=20 #Se establece el estado como el final
                            token='error' #El token se define como un error
                            lexema=cadena[indice] #Al lexema se le agrega el contenido de cadena[indice]
                            num=-1 #La variable num se establece con el número -1
                        indice+=1 #Se le suma 1 a la variable indice (se pasa a la siguiente posición)
                    elif estado==4:
                        #Si en la posición cadena[indice] hay un digito, una letra o un guión bajo
                        if cadena[indice].isdigit() or cadena[indice].isalpha() or cadena[indice]=='_':
                            estado=4 #Se establece el estado como el 4
                            lexema+=cadena[indice] #Al lexema se le agrega el contenido de cadena[indice]
                            token='identificador' #El token se define como un identificador
                            indice+=1 #Se le suma 1 a la variable indice (se pasa a la siguiente posición)
                            num=0 #La variable num se establece con el número 1
                        #Si en la posición cadena[indice] NO hay un digito, una letra o un guión bajo
                        else:
                            estado=20 #Se establece el estado como el final
                    elif estado==5:
                         #Si en la posición cadena[indice] NO hay un "="
                        if cadena[indice]!='=':
                            estado=20 #Se establece el estado como el final
                        #Si en la posición cadena[indice] NO hay un "="
                        else:
                            estado=20 #Se establece el estado como el final
                            lexema+=cadena[indice] #Al lexema se le agrega el contenido de cadena[indice]
                            token='opIgualdad' #El token se define como un operador de igualdad
                            indice+=1 #Se le suma 1 a la variable indice (se pasa a la siguiente posición)
                            num=11 #La variable num se establece con el número 11
                    elif estado==6:
                        if cadena[indice].isdigit():
                            estado=7 
                            lexema+=cadena[indice] 
                            token='entero' 
                            indice+=1 
                            num=1 
                        if cadena[indice]=='.':
                            estado=7
                            lexema+=cadena[indice]
                            indice+=1
                        else:
                            estado=20  
                    elif estado==7:
                        if cadena[indice].isdigit():
                            estado=8
                            lexema+=cadena[indice]
                            token='real'
                            indice+=1
                            num=2
                        if cadena[indice]=='.':
                            estado=8
                            lexema+=cadena[indice]
                            indice+=1
                        else:
                            estado=20
                    elif estado==8:
                        if cadena[indice].isdigit():
                            estado=9
                            lexema+=cadena[indice]
                            token='real'
                            indice+=1
                            num=2
                        else:
                            estado=20
                    elif estado==9:
                        if cadena[indice].isdigit():
                            estado=20
                            lexema+=cadena[indice]
                            token='real'
                            indice+=1
                            num=2
                        else:
                            estado=20
                    elif estado==10:
                        if cadena[indice]!='=':
                            estado=20
                        else:
                            estado=20
                            lexema+=cadena[indice]
                            token='opIgualdad'
                            indice+=1
                            num=11
                    elif estado==11:
                        if cadena[indice]=='"':
                            estado=20
                            lexema+=cadena[indice]
                            token='cadena'
                            indice+=1
                            num=3
                        else:
                            while(indice<=(len(cadena)-1) and cadena[indice]!='"'): 
                                lexema+=cadena[indice]
                                token='cadena'
                                num=3
                                indice+=1
                    elif estado==12:
                        if cadena[indice]!='=':
                            estado=20
                        else:
                            estado=20
                            lexema+=cadena[indice]
                            token='opRelac'
                            indice+=1
                            num=7
                    elif estado==13:
                        if cadena[indice]!='|':
                            estado=20
                        else:
                            estado=20
                            lexema+=cadena[indice]
                            token='opOr'
                            indice+=1
                            num=8
                    elif estado==14:
                        if cadena[indice]!='&':
                            estado=20
                        else:
                            estado=20
                            lexema+=cadena[indice]
                            token='opAnd'
                            indice+=1
                            num=9
                estado=0 #Se establece el estado como el inicial
                elementos.append({'lexema':lexema,'token':token,'num':num})  #Se guarda la info en la lista elementos
        #Se itera la lista de elementos para detectar si hay palabras reservadas y se establecen los
        #datos correspondientes a dicha palabra
        for elemento in elementos:
            if elemento['lexema']=="if":
                elemento['token']="if"
                elemento['num'] = 19
            elif elemento['lexema']=="else":
                elemento['token']="else"
                elemento['num'] = 22
            elif elemento['lexema']=="while":
                elemento['token']="while"
                elemento['num']=20
            elif elemento['lexema']=="return":
                elemento['token']="return"
                elemento['num']=21
            elif elemento['lexema']=="int":
                elemento['token']="tipo de dato"
                elemento['num']=4
            elif elemento['lexema']=="float":
                elemento['token']="tipo de dato"
                elemento['num']=4
            elif elemento['lexema']=="void":
                elemento['token']="tipo de dato"
                elemento['num']=4
            print(elemento) #Se imprime la info