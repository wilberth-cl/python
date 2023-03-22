###librerias para basededatos.txt
from operator import itemgetter


###Main
#
def inicio():
	mensage_inicio()
	opcion = None
	while opcion != 4:
		
		print("------> MENU\n")
		opcion = int(input("Introduce una opción:\n[ 1 ] => Listar\n[ 2 ] => Buscar\n[ 3 ] => Agregar\n[ 4 ] => Salir\n[Opcion] >>>> "))

		if opcion == 1:
			listar()
		elif opcion == 2:
			buscar()
		elif opcion == 3:
			agregar()
		elif opcion == 4:
			continue
		else:
			print("\nOpción Incorrecta!\n")

	mensage_final()



###Methods main
#
def mensage_inicio():
	print("\n>>>> Welcome! <<<<\n")

#
def mensage_final():
	print("\n>>>>> ¡Hasta Luego! <<<<<\n")



###Methos helps
#Formatea las Filas Existentes
def extraer_filas_db():
	
	archivo = open("basededatos.txt","r")
	lista = []
	for fila in archivo:
		fila_archivo = fila.split("-")
		lista.append(fila_archivo)
	archivo.close()
	return lista

#
def imprimir_tabla_menu(lista_filas_db):
	if lista_filas_db:
		encabezado = "{:>15} {:>15} {:>15}".format("Nombre", "Comida", "Precio")
		print(encabezado)
		print("_" * 60)
		for fila in lista_filas_db:
			fila_precio = "$"+fila[2]
			nueva_fila = "{:>15} {:>15} {:>15}".format(fila[0], fila[1], fila_precio)
			print(nueva_fila)
	else:
		print("\nBasededatos Vacía!\n")



###Methods Options
#
def listar():
	print("\n------> Listar \n")

	opcion = None
	while opcion != 4:
		opcion = int(input("Ordenar por:\n[ 1 ] => Nombre\n[ 2 ] => Comida\n[ 3 ] => Precio\n[ 4 ] => Salir\n[Opcion] >>>> "))

		#Obtener por indices 0-1-2
		lista_filas_db = extraer_filas_db()

		if opcion == 1:
			lista_filas_db.sort(key=itemgetter(0))
			imprimir_tabla_menu(lista_filas_db)
		elif opcion == 2:
			lista_filas_db.sort(key=itemgetter(1))
			imprimir_tabla_menu(lista_filas_db)
		elif opcion == 3:
			lista_filas_db.sort(key=itemgetter(2))
			imprimir_tabla_menu(lista_filas_db)
		elif opcion == 4:
			continue
		else:
			print("\nOpción Incorrecta!\n")

	print("------> Saliste de Listar...\n")

#
def buscar():
	print("\n------> Buscar\n")

	opcion = None
	while opcion != "1":
		opcion = input("[ 1 ] => Salir\n[Buscar] >>>> ")

		if opcion != "1":
			lista_filas_db = extraer_filas_db()
			encontrado = []
			for fila in lista_filas_db:
				if opcion in fila:
					encontrado.append(fila)

			if encontrado:
				imprimir_tabla_menu(encontrado)
			else:
				print("\nSin Resultados!\n")

	print("------> Saliste de Buscar...\n")

#
def agregar():
	print("\n------> Agregar\n")

	restaurant = input("Nombre del restaurant:\n => ")
	platillo = 	 input("Platillo principal:\n => ")
	precio =	 input("Precio del platillo:\n => ")
	nueva_fila = str(restaurant.lower()+'-'+platillo.lower()+'-'+precio+'\n')
	archivo = open("basededatos.txt",'a')
	archivo.write(nueva_fila)
	archivo.close()

	print(f"------> Se agrego correctamente: {nueva_fila}")
	print("------> Saliste de Agregar...\n")


###Start
inicio()
