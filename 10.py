def comptar_lletra(adn , lletra):
	return(adn.count(lletra))
	

adn = ["A","A","A","G","A","A","A","G","T","C","T","G","A","C","T","C","T","G","A","C"]
letra = input("Entra la lletra que vols comptar: ").upper()


print(comptar_lletra(adn,letra))