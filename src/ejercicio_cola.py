from class_cola import *

class ejercicio_cola:
    
    def __init__(self):
        self.cola = Cola(10)
    
    def Numero_Elementos(self,var_cola):
        return var_cola.Num_Elem_Cola()
    
    def k_enesimo(self,var_cola,posicion): # posicion desde 1
        if(posicion >0):
            if(posicion <= var_cola.Num_Elem_Cola()):
                if(var_cola.Cola_Vacia()):
                    print( "Cola Vacia")
                else:
                    cola_aux = Cola(var_cola.Num_Elem_Cola()-1)
                    c=1
                    while(not var_cola.Cola_Vacia()):
                        if c!=posicion:
                            cola_aux.Encolar(var_cola.Desencolar())
                        else:
                            var_cola.Desencolar()
                        c =c+1
                    
                    var_cola=cola_aux
                    
            else:
                 print( "la posicion debe ser menor al tamano de la cola")
        else:
            print( "la posicion debe ser mayor a 0")
        return var_cola
    