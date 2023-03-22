a = input("Numero a: ")

if int(a) < 5:
	print(f"{a} es menor a 5")
elif int(a) == 5:
	print("son iguales")
else:
	print(f"{a} es mayor a 5")


b = input("Numero b:")

if int(b) >= 0 and int(b) <= 10:
	print(f"{b} esta en el rango (0-10)")
if int(b) > 20 or int(b) > 30:
	print(f"{b} esta en el rango (21-X)")
if not( int(b) > 50 ): 
	print(f"{b} es menor a 100")
