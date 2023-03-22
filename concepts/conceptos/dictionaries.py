persona = {
	"nombre" : "Wilberth",
	"apellido" : "Francisco",
	"altura" : 1.69
}

favorito = {
	"color" : "rojo",
	"numero" : 7,
	"ciudad" : "Mérida"
}

#Lista de Diccionarios

cart = [
	{
		"nombre" : "Gorra",
		"precio" : 56,
		"modelo" : "Casual"
	},{
		"nombre" : "Pants",
		"precio" : 249.99,
		"modelo" : "Deportivo"
	}
]

print( dir( {"":""} ) )

print()
print("keys::::")

#Obtener las llaves
print( persona.keys() )
print( favorito.keys()  )
print( cart[1].keys()  )

print()
print("Values:::")

#Obtener Valores
print( persona.values() )
print( favorito.values() )
print( cart[1].values() )

print()
print("Items:::")

#Extraer en Lista de Tuplas
print( persona.items() )
print( favorito.items() )
print( cart[1].items() )