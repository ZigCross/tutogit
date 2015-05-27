#!/usr/bin/env python

from archivo import guardardatos

salir = False

while not salir:
	opcion = raw_input('Seleccione una opcion: ')

	if opcion == '1':
		passwd = raw_input('Ingrese una contrasena alfanumerica en minusculas: ')
		# Aqui va el codigo de ramses
		if funcion_ramses(passwd):
			guardardatos(passwd)

	elif opcion == '2':
		print "Bloque de la opcion 2"
	elif opcion == '3':
		salir = True
		print "Adios!"
	else:
		print "Seleccione una opcion valida"

