from Nodo import Paciente
class listasimple():
    def __init__(self):
        self.primero=None
        self.ultimo = None
        self.size = 0
    def insertlast(self,nombre,edad,periodos,m):
        # Mejor insertar al final
        self.size += 1
        newpaciente= Paciente(nombre,edad,periodos,m)
        if self.primero is None:
            self.primero = newpaciente
            self.ultimo = newpaciente
        else:
            # tmp = self.primero
            # while tmp.siguiente is not None:
            #     tmp.setsig(newpaciente)  
            self.ultimo.setsig(newpaciente)
            self.ultimo = newpaciente
    def printlist(self):
        tmp = self.primero
        for i in range (self.size):
            print(i,"Nombre: ", tmp.nombre," ","Edad: ", tmp.edad," ","periodos: ", tmp.periodos," ","M: ", tmp.m)
            tmp = tmp.getsig()