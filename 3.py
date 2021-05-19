while True:
	jugar = str(input("Quieres jugar: "))
	if jugar == "adeu" or jugar == "Adeu" or jugar == "ADEU":
		print("Adeu, que tengas un buen dia")
		break
	elif jugar == "si" or jugar == "Si" or jugar == "SI":
		cops = int(input("Quantas veces lo quieres repetir: "))
		palabra = str(input("Que quieres decir: "))
		for i in range(cops):
			print(palabra , end =" ")
		print("  ")
		continue