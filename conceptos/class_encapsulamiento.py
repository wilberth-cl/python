## CLASES = ENCAPSULAMIENTO
# Declaraciones publicas 	[ metodoName ]	[ variableName ]
# Declaraciones no publicas [ _metodoName ] [ _variableName ] ==> { Encapsulación }

# Clases...
class Mascota:
	def __init__(self, nombre, clasificacion_nacimiento, clasificacion_alimentacion, clasificacion_comportamiento, clasificacion_habitad):
		self._nombre = nombre
		self._clasificacion_nacimiento = clasificacion_nacimiento
		self._clasificacion_alimentacion = clasificacion_alimentacion
		self._clasificacion_comportamiento = clasificacion_comportamiento
		self._clasificacion_habitad = clasificacion_habitad

	@property
	def nombre(self):
		return self._get_nombre()
	@nombre.setter
	def nombre(self, new_nombre):
		self._nombre = new_nombre

	def _get_nombre(self):
		return self._nombre

	@property
	def clasificacion_nacimiento(self):
		return self._clasificacion_nacimiento
	@clasificacion_nacimiento.setter
	def clasificacion_nacimiento(self, new_clasificacion_nacimiento):
		self._clasificacion_nacimiento = new_clasificacion_nacimiento

	@property
	def clasificacion_alimentacion(self):
		return self._clasificacion_alimentacion
	@clasificacion_alimentacion.setter
	def clasificacion_alimentacion(self, new_clasificacion_alimentacion):
		self._clasificacion_alimentacion = new_clasificacion_alimentacion

	@property
	def clasificacion_comportamiento(self):
		return self._clasificacion_comportamiento
	@clasificacion_comportamiento.setter
	def clasificacion_comportamiento(self, new_clasificacion_comportamiento):
		self._clasificacion_comportamiento = new_clasificacion_comportamiento

	@property
	def clasificacion_habitad(self):
		return self._clasificacion_habitad
	@clasificacion_habitad.setter
	def clasificacion_habitad(self, new_clasificacion_habitad):
		self._clasificacion_habitad = new_clasificacion_habitad

# ...Objetos
miMascota = Mascota('Terry','Viviparo','Omnivoro','Domestico','Terrestre')
miOtraMascota = Mascota('Raul','Viviparo','Omnivoro','Domestico','Terrestre')

print("::: Mascota 1 :::")
print("Nombre: "+miMascota.nombre)
print("Nacimiento: "+miMascota.clasificacion_nacimiento)
print("Alimentacion: "+miMascota.clasificacion_alimentacion)
print("Comportamiento: "+miMascota.clasificacion_comportamiento)
print("Habitad: "+miMascota.clasificacion_habitad)

print("::: Mascota 2 :::")

print("Nombre: "+miOtraMascota.nombre)
print("Nacimiento: "+miOtraMascota.clasificacion_nacimiento)
print("Alimentacion: "+miOtraMascota.clasificacion_alimentacion)
print("Comportamiento: "+miOtraMascota.clasificacion_comportamiento)
print("Habitad: "+miOtraMascota.clasificacion_habitad)

miOtraMascota.nombre = "Alex"
print("--- Se cambio el nombre ---")

print("::: Mascota 2 Modificado :::")
print("Nombre: "+miOtraMascota.nombre)
print("Nacimiento: "+miOtraMascota.clasificacion_nacimiento)
print("Alimentacion: "+miOtraMascota.clasificacion_alimentacion)
print("Comportamiento: "+miOtraMascota.clasificacion_comportamiento)
print("Habitad: "+miOtraMascota.clasificacion_habitad)