#!/usr/bin/env python

archivo = open('prueba.txt', 'r')

linea=archivo.readline()

claves = []

while linea!="":
	print linea
	linea = archivo.readline()
	claves.append(linea)

print claves

archivo.close()

