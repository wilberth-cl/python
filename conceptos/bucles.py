animales = ["perro", "gato", "conejo", "ardilla"]

print(animales[1])
print()

for animal in animales:
	
	if animal == "gato":
		print("miau, miau")
		continue
		#break
	print(animal)
	
print()

for numero in range(1, 10):
	print(numero)

print()

for letter in "Wilberth":
	print(letter)

print()

count = 2
while count <= 40:
	print(count)
	count = count + 1