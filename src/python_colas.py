from ejercicio_cola import *
from class_cola import *

ej = ejercicio_cola()

cola = Cola(8)
cola.Leer_Cola(1,5,9,8,7,6)
print(ej.Numero_Elementos(cola))

cola=ej.k_enesimo(cola,10)
cola.Imprimir_Cola_Dev()
