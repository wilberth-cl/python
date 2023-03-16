# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza aparecen a continuación.
#
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print("::: Pizerría :::\n")
print("Sería una pizza vegana?")
resp = input("( si/no )=> ")

reseta = "Mozzarella, Tomate"

if resp == "si":
	pizza = "Vegana"
	menu = "Pimiento y Tofu."

	print("\nIngredientes vegetarianos:")
	print(f"{menu} ")
	print("\nCuales serian los ingredientes:")
	ingres = input("=> ")
	print(f"\nSu Orden es:\n Pizza: {pizza}.\n Ingredientes: {reseta}, {ingres}.")
else:
	pizza = "No Vegana"
	menu = "Peperoni, Jamón y Salmón."

	print("\nIngredientes no vegetarianos:")
	print(f"{menu} ")
	print("\nCuales serian los ingredientes:")
	ingres = input("=> ")
	print(f"\nSu Orden es:\n Pizza: {pizza}.\n Ingredientes: {reseta}, {ingres}.")

