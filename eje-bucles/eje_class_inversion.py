class Inversion():
	def __init__(self, inversion=0, interes=0, tiempo=0):
		self.inversion = inversion
		self.interes = interes
		self.tiempo = tiempo
	
	@property
	def inversion(self):
		return self.inversion
	@inversion.setter
	def inversion(self, inversion):
		self._inversion = inversion

	@property
	def interes(self):
		return self.interes
	@interes.setter
	def interes(self, interes):
		self._interes = interes

	@property
	def tiempo(self):
		return self.tiempo
	@tiempo.setter
	def tiempo(self, tiempo):
		self._tiempo = tiempo

	def rendimiento(self):
		ganancia = self._inversion
		rendimientototal = 0
		i = 1
		while i <= self._tiempo:
			rendimiento = ganancia * self._interes
			ganancia += rendimiento
			rendimientototal += rendimiento
			print(f"año[{i}] => ${rendimiento}")
			i += 1
		self.reporte(ganancia, rendimientototal)

	def reporte(self, ganancia, rendimientototal):
		print("-----------------------")
		print(f"Inversion Inicial => ${self._inversion}")
		print(f"Rendiemientos: ====> ${rendimientototal}")
		print(f"Capital ===========> ${ganancia}")

print("\n::: Mi Clase Inversion :::\n")

miInversion = Inversion()

inversion = int(input("Inversión => "))
interes = float(input("Interés ===> "))
tiempo = int(input("Tiempo ====> "))
print("-----------------------")

miInversion.inversion = inversion
miInversion.interes = interes
miInversion.tiempo = tiempo

miInversion.rendimiento()
