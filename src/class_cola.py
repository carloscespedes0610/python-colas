
class Cola:
    
    def __init__(self,capacidad):
        self.cola=list()
        self.capacidad=capacidad
    
    def Cola_Vacia(self):
        return self.cola == []
    
    def Cola_Llena(self):
        return len(self.cola)==self.capacidad
    
    def Encolar(self, elemento):
        if(self.Cola_Llena()):
            return "Cola Llena, el elemento "+str(elemento)+" no pudo ser agregado"
        else:
            self.cola.append(elemento)
            return "Elemento Agregado: "+str(elemento)
    
    def Desencolar(self):
        if(self.Cola_Vacia()):
            return "No Existe Ningun Elemento En La Cola, Cola Vacia"
        else:
            return self.cola.pop(0)
    
    
    def Leer_Cola(self, *elementos):

        for k in elementos:
            print(self.Encolar(k))
            
    def Num_Elem_Cola(self):
        return len(self.cola)
            
    def Invertir(self):
        lista=list()
        while(not self.Cola_Vacia()):
            lista.append(self.cola.pop(self.Num_Elem_Cola()-1))
    
        self.cola = lista
    
    def Primero(self):
        if (self.Cola_Vacia()):
            return "No Existe Ningun Elemento En La Cola, Cola Vacia"
        else:
            return self.cola[0]
    
    def Quitar_Primero(self):
        self.cola.pop(0)
        
    
   
    
    def Imprimir_Cola(self):
        print("Imprimiento Cola:")
        for k in self.cola:
            print(k)
            
            
    def Imprimir_Cola_Dev(self):
        print(str(self.cola)+"; capacidad: "+str(self.capacidad))