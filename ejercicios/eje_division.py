print(":::DIVISION:::")

n_a = input("Número 1: ")
n_b = input("Número 2: ")

if int(n_b) == 0:
	print(f"Error: no se puente dividir entre {n_b}.")
else:
	n_c = int(n_a) / int(n_b)
	print(f"La división es: {n_c}")
