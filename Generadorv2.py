#!/usr/bin/env python3
#from pyautogui import hotkey
import time
import os
import string
import random

def inicio():
	print(r"""
	           ______________________________________________________________________________________
		   |				   Instituto Politecnico Nacional			|
		   |			Escuela Superior de Ingenieria Mecanica y Electrica		|
		   |					Unidad Culhuacan                                |
		   |											|
		   |  Analisis de seguridad en el canal de comunicación de dispositivos inalambricos    |
		   |											|
                   |				Script Generador basado en Jackit			|
		   |											|
		   |   creado por:									|
		   |		Pérez Guzmán Jonathan							|
		   |		Ramirez Mendoza David							|
		   |		Rojas Hernandez Brandon Alonso 						|
		   |____________________________________________________________________________________|
													""")


inicio()

f = open("Respuesta.txt", "w+")				# Abir archivo de texto "Respuestas.txt" con permiso para escribir
Basura = string.ascii_letters				# Definimos una variable donde se guardaran las letras contenidas en el modulo ASCII
Aux = ''						# Variable auxiliar para guardar la cadena basura
for i in range(random.randint(7,19)):         		# Ciclo for aleatorio
	Aleatorio = random.randint(1, 5)		# Variable con un valor aleatorio que define el numero de caracteres que ocuparemos
	Aux = random.choices(Basura, k=Aleatorio)	# Guardamos en nuestra variable auxiliar la cadena de caracteres cargadas
							# en Basura con una longitud aleatia "a"
	f.write("DELAY 4000 \n")                      	# Contenido del archivo de texto
	f.write("STRING ")				# Contenido del archivo de texto
	f.write("".join(Aux))				# Guardamos la cadena en el archivo de texto, al generarse una lista en el paso anterior y dado que la funcion
							# write solo nos permite guardar cadenas usamos la funcion join para concatenar el contenido de la lista y
							# crear una cadena
	f.write("\n")
f.close()

#-----------------------------Empieza Ataque-----------------------------
'''
os.system('jackit --reset --address 16:C8:44:97:B4  --vendor Logitech --script /root/Desktop/Letras.txt') # os es la libreria que ocupamos y el "." denota lo que hara esa libreria

time.sleep(15)
hotkey('ctrl','c')
time.sleep(2)
os.system('all')
'''

