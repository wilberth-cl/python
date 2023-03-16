# Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
print("\n::: IMPAR :::\n")

print("Introduce un número entero:")
n = int(input("=> "))

print()

i = 1
while i <= n:
	if i%2 == 1:
		print(f"=> {i}")
	i = i + 1

print("\n::: OTRA FORMA :::\n")

impares = [str(i) for i in range(1, n+1) if i%2 != 0]
print(", ".join(impares))

pares = [str(i) for i in range(1 + n+1) if i%2 == 0]
print(", ".join(pares))