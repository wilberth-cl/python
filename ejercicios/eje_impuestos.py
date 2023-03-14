print("::: Impuestos :::")

print()
print("Cuál es su edad?")
edad = input("=> ")

if int(edad) > 16:

	print("Cuál es su ingreso mesual?")
	ingreso = input("=> ")
	
	if int(ingreso) >= 1000:
		print("Hey!, tienes algnas contribuciones pendientes.")
	else:
		print("Por el momento no cuentas con impuestos pendientes.")

else:
	print("Aún eres muy jovén para tributar.")