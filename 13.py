import random


nom = input("Entra el teu nom: ")
primer = input("Entra el teu primer congnom: ")
segon = input("Entre el tru segon congnom: ")


usuari = ""
password = ""


def usuari(nom , primer , segon):
	usuari = nom[0] + nom[1] + primer[0] + primer[len(primer)-1] + segon[len(segon)-2] + segon[len(segon)-1]
	return usuari.lower()



def password(nom , primer):
	letras = ["#" , "@" , "!"]
	password = []
	for i in range(4):	
		password.append(random.randint(1,9))
	password.append(nom[0].upper())  
	password.append(primer[0].lower()) 
	password.append(random.sample(letras , 1))
	return "".join(map(str, password))

print(usuari(nom,primer,segon))
print(password(nom , primer))