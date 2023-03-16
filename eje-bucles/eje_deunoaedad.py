# Escribir un programa que pregunte al usuario su edad 
# y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
print("\n::: DE UNO A EDAD :::\n")

print("Cuál es tu edad:")
edad = input("=> ")

i = 1
while i <= int(edad):
	if i == 1:
		print(f">> {i} año")
		i = i + 1
	else:
		print(f">> {i} años")
		i = i + 1

