print("\n::: Separado Por Comas :::\n")

print("Número:")
n = int(input("=> "))

def nmreverse(n):
	nm = [str(i) for i in range(0, n)]
	nm.reverse()
	print(" - ".join(nm))

nmreverse(n)
