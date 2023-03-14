# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#
# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10001€ y 20000€	15%
# Entre 20001€ y 35000€	20%
# Entre 35001€ y 60000€	30%
# Más de 60001€	45%
#
# Escribir un programa que pregunte al usuario su renta anual
# y muestre por pantalla el tipo impositivo que le corresponde.

print("::: Tramos impositivos :::")

print("Cuál es su renta anual?")
rentaanual = input("=> ")

if int(rentaanual) > 60000:
	print(f"Su tipo impositivo correspontiente a: {rentaanual}€, es del 45%.")
else:
	if int(rentaanual) > 35000:
		print(f"Su tipo impositivo correspontiente a: {rentaanual}€, es del 30%.")
	else:
		if int(rentaanual) > 20000:
			print(f"Su tipo impositivo correspontiente a: {rentaanual}€, es del 20%.")
		else:
			if int(rentaanual) > 10000:
				print(f"Su tipo impositivo correspontiente a: {rentaanual}€, es del 15%.")
			else:
				print(f"Su tipo impositivo correspontiente a: {rentaanual}€, es del 5%.")


