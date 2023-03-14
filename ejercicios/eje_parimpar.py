print("::: par / impar :::")

n = input("Introduce un número: ")

a = int(n) % 2;

if a == 0:
	print(f"{n} es un número par, residuo: {a}")
else:
	print(f"{n} es un número impar, residuo: {a}")