from Nodo import Paciente
class listasimple():
    def __init__(self):
        self.primero=None
        self.ultimo = None
        self.size = 0
    def insertlast(self,nombre,edad,periodos,m,rejilla,matriz):
        # Mejor insertar al final
        
        newpaciente= Paciente(nombre,edad,periodos,m,rejilla,matriz)
        self.size += 1
        if self.primero is None:
            self.primero = newpaciente
            self.ultimo = newpaciente
        else:
            tmp = self.primero
            while tmp.getsig() is not None:
                tmp=tmp.getsig()
            tmp.setsig(newpaciente)
    def printlist(self):
        tmp = self.primero
        print(self.size)
        while tmp is not None:
            print("Nombre: ", tmp.nombre," ","Edad: ", tmp.edad," ","periodos: ", tmp.periodos," ","M: ", tmp.m,"\n","Rejilla: \n", tmp.rejilla,"\n","Infectada: \n", tmp.matriz)
            tmp=tmp.getsig()
    def getpaciente(self, nombre):
        tmp = self.primero
        for x in range(self.size):
            if tmp.nombre == nombre:
                print("Nombre: ", tmp.nombre," ","Edad: ", tmp.edad," ","periodos: ", tmp.periodos," ","M: ", tmp.m,"\n","Rejilla: \n", tmp.rejilla,"\n","Infectada: \n", tmp.matriz) 
                return tmp
            tmp = tmp.getsig()
    def getmatrix(self, nombre):
        tmp = self.primero
        for x in range(self.size):
            if tmp.nombre == nombre:
                return tmp.matriz
            tmp = tmp.getsig()
    