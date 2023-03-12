class Mascota:
	def __init__(self, nombre, clasificacion_nacimiento, clasificacion_alimentacion, clasificacion_comportamiento, clasificacion_habitad):
		self.nombre = nombre
		self.clasificacion_nacimiento = clasificacion_nacimiento
		self.clasificacion_alimentacion = clasificacion_alimentacion
		self.clasificacion_comportamiento = clasificacion_comportamiento
		self.clasificacion_habitad = clasificacion_habitad

	def nombre(self):
		return self.nombre

	def clasificacion_nacimiento(self):
		return self.clasificacion_nacimiento

	def clasificacion_alimentacion(self):
		return self.clasificacion_alimentacion

	def clasificacion_comportamiento(self):
		return self.clasificacion_comportamiento

	def clasificacion_habitad(self):
		return self.clasificacion_habitad


miMascota = Mascota('Terry','Viviparo','Omnivoro','Domestico','Terrestre')

print("Nombre: "+miMascota.nombre)
print("Nacimiento: "+miMascota.clasificacion_nacimiento)
print("Alimentacion: "+miMascota.clasificacion_alimentacion)
print("Comportamiento: "+miMascota.clasificacion_comportamiento)
print("Habitad: "+miMascota.clasificacion_habitad)
