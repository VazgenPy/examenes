def Comptar_Purina(adn):
	string = "".join(adn)
	return(string.count("GA"))


adn = ["A","A","A","G","A","A","A","G","T","C","T","G","A","C","T","C","T","G","A","C","G","A"]


print("Hi ha purina" , Comptar_Purina(adn) , "cops")