
from xml.dom import minidom
from xml.etree.cElementTree import parse, Element
from tkinter import filedialog as fd
from listasimple import listasimple
print("-----Predicción Patrones Enfermedades-----")
global lista
lista = listasimple()
a= input("¿Desea abrir archivo? Ingrese SI/NO " )
if a=="SI":
    filename = fd.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.xml*"), ("Text files", "*.LFP*"),("all files", "*.*")))
    docxml=minidom.parse(filename)
    pacientes = docxml.getElementsByTagName('pacientes')
    paciente = docxml.getElementsByTagName('paciente')
    for i in paciente:
        print(i)
        nombre = docxml.getElementsByTagName('nombre')
        for k in nombre:
            lista.insertlast( k.firstChild.data,1,1,1)
            

#Paciente es mi clase nodo
# lista.insertlast('mariano',19,2,3)
# lista.insertlast('messi',19,2,3)
lista.printlist()
print("HOLAAAA")
