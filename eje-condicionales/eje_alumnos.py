# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un nombre anterior a la M
# y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo,
# y muestre por pantalla el grupo que le corresponde.

print("::: GRUPOS :::")

print("Su nombre: ")
nombre = input("=> ")

print("Su sexo (h/m): ")
sexo = input("=> ")

# A M:[A-L] H:[Ñ-Z] 
# B M[Ñ-Z] H:[A-L]
if sexo == "m":
	if nombre.lower() < "m":
		grupo = "A"
	else:
		grupo = "B"
else:
	if nombre.lower() > "n":
		grupo = "A"
	else:
		grupo = "B"
print("Tu grupo es: "+ grupo)
