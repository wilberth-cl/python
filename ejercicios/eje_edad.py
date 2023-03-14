# Escribir un programa que pregunte al usuario su edad
# y muestre por pantalla si es mayor de edad o no.

edad = input("Cuál es su edad?: ")

if int(edad) < 18:
	print(f"Eres menor de edad, tienes {edad} años.")
else:
	print(f"Eres mayor de edad, tienes {edad} años.")