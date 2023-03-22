# Para tributar un determinado impuesto se debe ser mayor de 16 años 
# y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales 
# y muestre por pantalla si el usuario tiene que tributar o no.

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