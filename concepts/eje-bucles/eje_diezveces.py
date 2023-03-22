# Escribir un programa que pida al usuario una palabra
# y la muestre por pantalla 10 veces.
print("\n::: DIEZ VECES :::\n")

print("Introduce una palabra:")
palabra = input("=> ")
print()

i = 0

while i < 10:
	print(f"{i+1}: {palabra}")
	i = i + 1

