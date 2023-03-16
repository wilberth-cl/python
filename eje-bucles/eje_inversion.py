print("\n::: INVERSION :::\n")

print("Cantidad:")
inversion = int(input("=> "))

print("Intereses:")
interes = float(input("=> "))

print("Tiempo (años):")
tiempo = int(input("=> "))

i = 1
ganancia = 0
inversioninicial = inversion

while i <= tiempo:
	ganancia = inversion * interes

	inversion += ganancia

	print(f"año[{i}] => ${ganancia}")
	i += 1

if i-1 == tiempo:
	print(f"\nCapital => { inversioninicial+ganancia }")