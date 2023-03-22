#print()
#dir()
#type()

def resta(a, b):
	c = a - b;
	return c


print( resta(4,2) )


def suma(nombre="Alguien"):
	a = input("Number a: ")
	b = input("Number b: ")
	c = int(a) + int(b)

	print(f"{nombre}, la suma es: {c}")

suma("Wilberth")
suma()
