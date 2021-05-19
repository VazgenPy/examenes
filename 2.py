import random
print("Bienvenido")
print("""
1)Son goku
2)Jakie Chun
3)Krilin
4)Tenshinjan
			""")
e = int(input("Elige: "))
son = random.randint(80,90)
jak = random.randint(50,80)
kri = random.randint(20,50)
ten = random.randint(40,70)
satan = random.randint(0,80)
if e == 1:
	if son > satan:
		print("Has ganado")
		print(son , satan)
	elif son < satan:
		print("Has perdido")
		print(son , satan)
	elif son == satan:
		print("Nulo")
		print(son , satan)
elif e == 2:
	if jak > satan:
		print("Has ganado")
		print(jak , satan)
	elif jak < satan:
		print("Has perdido")
		print(jak , satan)
	elif jak == satan:
		print("Nulo")
		print(jak , satan)
elif e == 3:
	if kri > satan:
		print("Has ganado")
		print(kri , satan)
	elif kri < satan:
		print("Has perdido")
		print(kri , satan)
	elif kri == satan:
		print("Nulo")
		print(kri , satan)
elif e == 4:
	if ten > satan:
		print("Has ganado")
		print(ten , satan)
	elif ten < satan:
		print("Has predido")
		print(ten , satan)
	elif ten == satan:
		print("Nulo")
		print(ten , satan)