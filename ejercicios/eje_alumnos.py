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
