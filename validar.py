#!/usr/bin/env python

def validar_clave(passwd):

	archivo = open('texto.txt', 'r')

	claves =archivo.read()

	lista_claves = claves.split("\n")

	if passwd in lista_claves:
		print "La clave se encontro"
	
	else:
		print "La clave no se encontro"

	archivo.close()

