# En una determinada empresa, sus empleados son evaluados al final de cada año.
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
# traduciéndose en mejores beneficios.
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más,
# pero no valores intermedios entre las cifras mencionadas.
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
# La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
#
# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más
#
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento,
# así como la cantidad de dinero que recibirá el usuario.
print("::: EVALUACIONES :::")

print("Indique su puntuación:")
puntuacion = input("=> ")

base = 2400

if float(puntuacion) == 0.0:
	base = base * 0.0
	nivel = "INAPCETABLE"
	print(f"Su nivel es: {nivel}, catidad correspondiente: {base}€.")
else:
	if float(puntuacion) == 0.4:
		base = (base * 0.0) + (base * 0.4)
		nivel = "ACEPTABLE"
		print(f"Su nivel es: {nivel}, cantidad correspondiente: {base}€.")
	elif float(puntuacion) >= 0.6:
		base = (base*0.0) + (base*0.4) + (base*0.6)
		nivel = "MERITORIO"
		print(f"Su nivel es: {nivel}, cantidad correspondiente: {base}€.")
	else:
		print("¡Puntuación No Válida!")