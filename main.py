#!/usr/bin/env python

from archivo import guardardatos
from prueba  import prueba 
from validar import validar_clave

salir = False

while not salir:
	opcion = raw_input('Seleccione una opcion: ')

	if opcion == '1':
		passwd = raw_input('Ingrese una contrasena alfanumerica en minusculas: ')
		
		if prueba(passwd):
			guardardatos(passwd)

	elif opcion == '2':
		passwd2 = raw_input('Ingrese una contrasena alfanumerica: ')

		validar_clave(passwd2)

	elif opcion == '3':
		salir = True
		print "Adios!"
	else:
		print "Seleccione una opcion valida"

