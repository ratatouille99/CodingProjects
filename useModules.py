#IMPORT: importa toda la libreria y nos da acceso a todos sus metodos y funciones
#FROM....IMPORT: Nos da acceso a una funcion o metodo en especifico
#FROM...IMPORT...AS: Nos permite importar una funcion especifica y renombrarla como queramos despues de la palabra clave as

from random import choice #Importamos la funcion choice q elige un valor aleatorio de un arreglo
import webbrowser #nos permite tomar control de nuestro explorador y abrir paginas webs
from time import time as time_now

webbrowser.open('https://es-la.facebook.com/')#Nos direccionamos a facebook

array = ['N', 'O', 'E']
random = choice(array)
print(random)

tiempo = time_now()
print(tiempo)