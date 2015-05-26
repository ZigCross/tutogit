#! usr/bin python 

# parte del programa que esta crea el archivo
# "texto.txt" y los guarda en el archivo creado

print " BUENOS DIAS !!!!! "
print "PROGRAMITA SENSILL0"

def guardardatos():
	archivo= open("texto.txt", "a")
	print"ingrese datos a guardar: "
	datos = raw_input()
	print "datos guardados: " + datos
	archivo.write(datos +"\n")
	archivo.close




guardardatos()

