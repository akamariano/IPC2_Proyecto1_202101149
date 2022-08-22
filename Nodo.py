class Paciente():
    def __init__(self,nombre,edad,periodos,m):
        self.nombre=nombre
        self.edad=edad
        self.periodos = periodos
        self.m=m
        self.next=None
        self.siguiente = None
    def getsig(self):
        return self.siguiente
    def setsig(self, paciente):
         self.siguiente = paciente


