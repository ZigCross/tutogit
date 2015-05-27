#!/usr/bin/env python

from archivo import guardardatos
from prueba  import prueba 

salir = False

while not salir:
	opcion = raw_input('Seleccione una opcion: ')

	if opcion == '1':
		passwd = raw_input('Ingrese una contrasena alfanumerica en minusculas: ')
		
		if prueba(passwd):
			guardardatos(passwd)

	elif opcion == '2':
		print "Bloque de la opcion 2"
	elif opcion == '3':
		salir = True
		print "Adios!"
	else:
		print "Seleccione una opcion valida"

