while True:
	temp = int(input("Cuantos grados hacen: (entre -10ºc a 30ºc): "))
	if temp < -10 and temp > 30:
		continue
	elif temp >= -10 and temp <= 30:
		if temp < 0:
			print("Polar")
		elif temp >= 0 and temp <= 9:
			print("Bufanda y Guantes")
		elif temp >= 10 and temp <= 19:
			print("Manga corta")
		elif temp >= 20:
			print("Bañador")
		break