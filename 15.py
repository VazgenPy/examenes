archivo = open("a1.txt" , "r")
lista = []


def media(lista):
	medias = []
	suma = 0
	for linea in archivo:
		lista.append(linea.split())
	for i in range(len(lista)):
		a = lista[i][1:len(lista[i])]
		for j in range(len(a)):
			suma = int(a[j]) + suma
		if suma == 0:
			break
		medias.append([lista[i][0] , suma/4])
		suma = 0
	print(max(medias) , "Tiene la media mas alta")
	return(lista)


def numero(lista):
	for linea in lista:
		for i in range(len(linea)):
			if linea[i] == "9":
				print(linea[0] , "Ha sacado un: 9")
			if linea[i] < "5":
				print(linea[0] , "Ha suspendido con un: " , linea[i])


numero(media(lista))


for i in lista:
	print(i)
