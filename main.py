#!/usr/bin/env python

salir = False

while not salir:
	opcion = raw_input('Seleccione una opcion: ')

	if opcion == '1':
		print "Bloque de la opcion 1"
	elif opcion == '2':
		print "Bloque de la opcion 2"
	elif opcion == '3':
		salir = True
		print "Adios!"
	else:
		print "Seleccione una opcion valida"

