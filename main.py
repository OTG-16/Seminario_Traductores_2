#Importaciones
import os
from automata import Automata

#Limpieza de pantalla
os.system ("cls")
#Se solicita el texto a analizar al usuario
cadenaUsuario = input('Favor de ingresar el texto a analizar: ')
print("\nTexto analizado")  #Mensaje
#Se manda a llamar a la función Automata y se le pasa la variable cadenaUsuario como parámetro
Automata(cadenaUsuario)


