l = []
while True:
	a = input("Que quieres hacer: ")
	if a == "insertar":
		l.append(input("Nom: "))
		l.append(input("Ingredient Principal: "))
		l.append(input("Calorias: "))
		l.append(input("Dificauldad (Del 0 al 5): "))
		l.append(input("Explicacion: "))
		continue
	elif a == "Mostrar":
		for i in range(len(l)):
			for a in l:
				print(i[l])
	