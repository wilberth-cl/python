## CLASES = HERENCIA
# Declaraciones publicas 	[ metodoName ]	[ variableName ]
# Declaraciones no publicas [ _metodoName ] [ _variableName ] ==> { Encapsulación }

# SELF => referencia al objeto actual, como usar this.

# Clases...
# ...PADRE
class Pizza():
	def __init__(self, size, nombre, precio):
		self._size = size
		self._nombre = nombre
		self._precio = precio

	@property
	def size(self):
		return self._size
	@size.setter
	def size(self, new_size):
		self._size = new_size

	@property
	def nombre(self):
		return self._nombre
	@nombre.setter
	def nombre(self, new_nombre):
		self._nombre = new_nombre

	@property
	def precio(self):
		return self._precio
	@precio.setter
	def precio(self, new_precio):
		self._precio = new_precio
	
# ..DERIVADA, HIJA
class Especialidad(Pizza):
	def __init__(self, size, nombre, precio, ingredientes):
		super().__init__(size, nombre, precio)
		self._ingredientes = ingredientes

	@property
	def ingredientes(self):
		return self._ingredientes;
	@ingredientes.setter
	def ingredientes(self, new_ingredientes):
		self._ingredientes = new_ingredientes

# Objetos, instancias
miEspecialidad = Especialidad('Grande','Hawaina','110','queso, jamón, piña')
print("Tamaño/Nombre: "+miEspecialidad.size+' '+miEspecialidad.nombre)
print("Precio: $"+miEspecialidad.precio)
print("Ingredientes: "+miEspecialidad.ingredientes)

print()

miEspecialidad.size = input("Tamaño: ")
miEspecialidad.nombre = input("Nombre: ")
miEspecialidad.precio = input("Precio: ")
miEspecialidad.ingredientes = input("Ingredientes: ")

print()

print("Tamaño/Nombre: "+miEspecialidad.size+' '+miEspecialidad.nombre)
print("Precio: $"+miEspecialidad.precio)
print("Ingredientes: "+miEspecialidad.ingredientes)