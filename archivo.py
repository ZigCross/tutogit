#! usr/bin python 

# parte del programa que esta crea el archivo
# "texto.txt" y los guarda en el archivo creado

def guardardatos(datos):
	archivo= open("texto.txt", "a")
	archivo.write(datos +"\n")
	archivo.close
