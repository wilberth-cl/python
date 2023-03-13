class Mascota:
	def __init__(self, nombre, clasificacion_nacimiento, clasificacion_alimentacion, clasificacion_comportamiento, clasificacion_habitad):
		self.nombre = nombre
		self.clasificacion_nacimiento = clasificacion_nacimiento
		self.clasificacion_alimentacion = clasificacion_alimentacion
		self.clasificacion_comportamiento = clasificacion_comportamiento
		self.clasificacion_habitad = clasificacion_habitad

	@property
	def nombre(self):
		return self.__nombre
	@nombre.setter
	def nombre(self, new_nombre):
		self.__nombre = new_nombre

	@property
	def clasificacion_nacimiento(self):
		return self.__clasificacion_nacimiento
	@clasificacion_nacimiento.setter
	def clasificacion_nacimiento(self, new_clasificacion_nacimiento):
		self.__clasificacion_nacimiento = new_clasificacion_nacimiento

	@property
	def clasificacion_alimentacion(self):
		return self.__clasificacion_alimentacion
	@clasificacion_alimentacion.setter
	def clasificacion_alimentacion(self, new_clasificacion_alimentacion):
		self.__clasificacion_alimentacion = new_clasificacion_alimentacion

	@property
	def clasificacion_comportamiento(self):
		return self.__clasificacion_comportamiento
	@clasificacion_comportamiento.setter
	def clasificacion_comportamiento(self, new_clasificacion_comportamiento):
		self.__clasificacion_comportamiento = new_clasificacion_comportamiento

	@property
	def clasificacion_habitad(self):
		return self.__clasificacion_habitad
	@clasificacion_habitad.setter
	def clasificacion_habitad(self, new_clasificacion_habitad):
		self.__clasificacion_habitad = new_clasificacion_habitad


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
print("::: Mascota 2 Modificado :::")
print("Se cambio el nombre")
print("Nombre: "+miOtraMascota.nombre)
print("Nacimiento: "+miOtraMascota.clasificacion_nacimiento)
print("Alimentacion: "+miOtraMascota.clasificacion_alimentacion)
print("Comportamiento: "+miOtraMascota.clasificacion_comportamiento)
print("Habitad: "+miOtraMascota.clasificacion_habitad)