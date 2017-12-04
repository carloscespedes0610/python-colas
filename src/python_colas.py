from ejercicio_cola import *
from class_cola import *

ej = ejercicio_cola()

# numero de elementos de la cola  ---------------
print("*-*-*-*-*-*-*-* numero de elementos de la cola *-*-*-*-*-")
cola = Cola(8)
cola.Leer_Cola(1,5,9,8,7,6)
print("numero de elementos: "+str(ej.Numero_Elementos(cola)))
cola=[]

# eliminar el k-enesimo elemento --------------------
print("*-*-*-*-*-*-*-* eliminar el k-enesimo(>0) elemento de una cola *-*-*-*-*-")
cola = Cola(8)
cola.Leer_Cola(1,2,3,4,5,6)
cola=ej.k_enesimo(cola,3)
print("cola despues de eliminar el k-enesimo elemento")
cola.Imprimir_Cola()

print("*-*-*-*-*-*-*-**-*-*-*-*- Fin *-*-*-*-*-*-*-*-*-*-*-*-*-")
print("Alumno: Carlos Alberto Cespedes Soliz")

