import random
while True:
	a = random.randint(1,9)
	b = random.randint(1,9)
	print("Resuelve esta equacion: " , a , "x +" , b , "= 0")
	resultado = float(-(b) / a)
	respuesta = float(input("Cual es la respuesta: "))
	if "{0:.2f}".format(respuesta) == ("{0:.2f}".format(resultado)):
		print("Bien no eres un robot ")
		break
	elif "{0:.2f}".format(respuesta) != ("{0:.2f}".format(resultado)):
		print("Mal eres un robot, vuelve a intentarlo ")
		continue