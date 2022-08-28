
from asyncio.windows_events import PipeServer
from xml.dom import minidom
from xml.etree.cElementTree import parse, Element
from tkinter import N, filedialog as fd
from listasimple import listasimple
import xml.etree.ElementTree as ET
import numpy as np
import graphviz as gp
from Nodo import DoublyLinkedList
from Nodo import listadetableros
import collections
#######
	
	# def get_count(self):
		
	# 	if self.head is None:
	# 		print(0)
	# 		n = self.head
	# 		count = 0
	# 	while n is not None:
	# 		count = count + 1
	# 		n = n.ref
	# 		return count
#######
print("-----Predicción Patrones Enfermedades-----")
lista = listasimple()
a= input("¿Desea abrir archivo? Ingrese SI/NO " )
if a=="SI":
	filename = fd.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.xml*"), ("Text files", "*.LFP*"),("all files", "*.*")))
	docxml=minidom.parse(filename)
	paciente = docxml.getElementsByTagName('paciente')
	
	for i in paciente:
		# print(i)
	   
		nombre = i.getElementsByTagName('nombre')
		edad = i.getElementsByTagName('edad')
		periodo = i.getElementsByTagName('periodos')
		m = i.getElementsByTagName('m')
		rejilla = i.getElementsByTagName('rejilla')
		celda = i.getElementsByTagName('celda')
		nu=int(m[0].firstChild.data)
		a = np.zeros((nu, nu))
		# print(a)
		for k in rejilla:
			# print(k)
			n=0
			for l in celda:
				
				# print(l.attributes['f'].value, l.firstChild.data)
				# print("Valor celda F: ", celda[n].attributes['f'].value, "Valor celda C: ", celda[n].attributes['c'].value)
				a[(int(celda[n].attributes['f'].value)-1)][(int(celda[n].attributes['c'].value)-1)]=1
				n+=1
				# print(n)
			coord = np.zeros((n, 2))
			# print("Coordenadas: \n",coord)
			p=0
			for j in celda:
				
				coord[p][0]=(int(celda[p].attributes['f'].value))
				coord[p][1]=(int(celda[p].attributes['c'].value))
				p+=1
			# for sana in a:
			enfermas=0
			nu=nu-1
			# print("N: ",nu)
			a2=a.copy()
			# dll = DoublyLinkedList()
			# rows = len(a2)
			# cols = len(a2)
			# dll.insertData(a2, rows, cols)
			# dll.display()
			# for x in range(nu):
			#     enfermas=0
			#     for y in range(nu):
			#         enfermas=0
			#         print(x,y)
			#         if(x==0 and y==0):
			#             if(a[x][y+1]==1):
			#                 enfermas+=1 
			#             if(a[x+1][y]==1):
			#                 enfermas+=1
			#             if(a[x+1][y+1]==1):
			#                 enfermas+=1
			#         if(x==0 and y==nu):
			#             if(a[x-1][y-1]==1):
			#                 enfermas+=1 
			#             if(a[x+1][y-1]==1):
			#                 enfermas+=1
			#             if(a[x+1][y+1]==1):
			#                 enfermas+=1
			#         if(x==nu and y==0):
			#             if(a[x-1][y]==1):
			#                 enfermas+=1 
			#             if(a[x][y+1]==1):
			#                 enfermas+=1
			#             if(a[x-1][y+1]==1):
			#                 enfermas+=1
			#         if(x==nu and y ==nu):
			#             if(a[x-1][y]==1):
			#                 enfermas+=1 
			#             if(a[x][y-1]==1):
			#                 enfermas+=1
			#             if(a[x-1][y-1]==1):
			#                 enfermas+=1
			#         if((0<x<nu) and y==0):
			#             if(a[x-1][y]==1):
			#                 enfermas+=1
			#             if(a[x-1][y+1]==1):
			#                 enfermas+=1
			#             if(a[x][y+1]==1):
			#                 enfermas+=1
			#             if(a[x+1][y-1]==1):
			#                 enfermas+=1
			#             if(a[x+1][y+1]==1):
			#                 enfermas+=1
			#         if((0<x<nu) and y==nu):
			#             if(a[x-1][y]==1):
			#                 enfermas+=1
			#             if(a[x-1][y-1]==1):
			#                 enfermas+=1
			#             if(a[x][y-1]==1):
			#                 enfermas+=1
			#             if(a[x+1][y-1]==1):
			#                 enfermas+=1
			#             if(a[x+1][y-1]==1):
			#                 enfermas+=1
			#         if(x==0 and (0 < y < nu)):
			#             if(a[x][y-1]==1):
			#                 enfermas+=1
			#             if(a[x][y+1]==1):
			#                 enfermas+=1
			#             if(a[x+1][y]==1):
			#                 enfermas+=1
			#             if(a[x+1][y-1]==1):
			#                 enfermas+=1
			#             if(a[x+1][y+1]==1):
			#                 enfermas+=1
			#         if(x==nu and (0 < y < nu)):
			#             if(a[x][y-1]==1):
			#                 enfermas+=1
			#             if(a[x][y+1]==1):
			#                 enfermas+=1
			#             if(a[x-1][y]==1):
			#                 enfermas+=1
			#             if(a[x-1][y-1]==1):
			#                 enfermas+=1
			#             if(a[x-1][y+1]==1):
			#                 enfermas+=1
			#         if((0 < x < nu) and (0 < y < nu)):
			#                 if(a[x-1][y]==1):
			#                     enfermas+=1
			#                 if(a[x-1][y-1]==1):
			#                     enfermas+=1
			#                 if(a[x-1][y+1]==1):
			#                     enfermas+=1
			#                 if(a[x][y-1]==1):
			#                     enfermas+=1 
			#                 if(a[x][y+1]==1):
			#                     enfermas+=1
			#                 if(a[x+1][y-1]==1):
			#                     enfermas+=1
			#                 if(a[x+1][y]==1):
			#                     enfermas+=1
			#                 if(a[x+1][y+1]==1):
			#                     enfermas+=1
			#         if(a[x][y]==1 and (2<=enfermas<=3)):
			#             a[x][y]==1
			#         if(a[x][y]==1 and (enfermas <2 or enfermas >4)):
			#             a[x][y]==0
			#         if(a[x][y]==0 and enfermas <=2 ):
			#             a[x][y]==0
			#         if(enfermas==3 and a[x][y]==0):
			#             a[x][y]=1
			#         if(a[x][y]==0 and enfermas>3):
			#             a[x][y]=0
			# print("Patron 1: \n",a)


			

		# dll.display()
		
		# print(nombre)
		# print(edad)
		# print(periodo)
		# print(m)
		lista.insertlast( nombre[0].firstChild.data,edad[0].firstChild.data,periodo[0].firstChild.data,m[0].firstChild.data,coord,a2)
		
		# print("Infectada \n",a)
		# print("Coordenadas: \n",coord)
		
			

#Paciente es mi clase nodo
# lista.insertlast('mariano',19,2,3)
# lista.insertlast('messi',19,2,3)
# lista.printlist()
print("PACIENTE:")
# dll.display()
# dll.get_count() 

print("Ingrese el nombre del paciente: ")
x = input()
paciente1=lista.getpaciente(nombre=x)
a3=lista.getmatrix(nombre=x)
dll = DoublyLinkedList()
rows = len(a3)
cols = len(a3)
dll.insertData(a3, rows, cols)
dll.dibujargrafica(x,"Período Inicial")
nodotablero = listadetableros()
nodotablero.tablero=dll
paciente1.settableros(nodotablero)
nodotab2=paciente1.tableros
for i in range(int(paciente1.periodos)):
	dll2=DoublyLinkedList()
	dll2.insertData(nodotab2.tablero.siguientediag(), rows, cols)
	tablero2=listadetableros()
	tablero2.tablero=dll2
	dll2.dibujargrafica(x,str(i+1))
	nodotab2.siguiente=tablero2
	nodotab2=None
	nodotab2=tablero2
	# dll2.display()
nodotab2=None
nodotab2=paciente1.tableros
nodotab3=paciente1.tableros
for i in range(int(paciente1.periodos)):
	for j in range(int(paciente1.periodos)):
		if i==j:
			pass
		if (nodotab2.tablero.siguientediag())==(nodotab3.tablero.siguientediag()):
			print("Se ha encontrado el patrón en: ", j+1 )
			break
		
		nodotab3=nodotab3.siguiente
	nodotab2=nodotab2.siguiente
	nodotab3=paciente1.tableros
# detecta=False
# for i in range(int(paciente1.periodos)):
# 	if detecta:
# 		break
# 	for j in range(int(paciente1.periodos)):
# 		if i==j:
# 			continue
# 		else:
# 			if (nodotab2.tablero.siguientediag())==(nodotab3.tablero.siguientediag()):
# 				detecta=True
# 				print("Se ha encontrado el patrón en: ", i )
# 				break

		
# 		nodotab3=nodotab3.siguiente
# 	nodotab2=nodotab2.siguiente
# 	nodotab3=paciente1.tableros

# print("Matriz con lista enlazada")
dll.display()
# print("TAMAÑO",dll.size)