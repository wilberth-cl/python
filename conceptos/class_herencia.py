## CLASES = HERENCIA
# Declaraciones publicas 	[ metodoName ]	[ variableName ]
# Declaraciones no publicas [ _metodoName ] [ _variableName ] ==> { Encapsulación }

# SELF => referencia al objeto actual, como usar this.

# Clases...
# PADRE
class Animal:	
	def __init__(self, especie):
		#parametros
		#atributos
		self._especie = especie

	@property
	def especie(self):
		return self._especie
	@especie.setter
	def especie(self, new_especie):
		self._especie = new_especie

# DERIVADA, HIJA
class Mascota(Animal):
	def __init__(self, especie, nombre):
		#atributos padre y darivada
		super().__init__(especie)
		self._nombre = nombre

	@property
	def nombre(self):
		return self._nombre

	@nombre.setter
	def nombre(self, new_nombre):
		self._nombre = new_nombre


# ...Objetos, instancias
miMascota = Mascota('Gato','Terry')
print(miMascota.nombre)
print(miMascota.especie)