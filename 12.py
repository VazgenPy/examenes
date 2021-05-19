'''
def Upper(text):
	nou_text = ""
	uppr = True
	for i in text:
		if uppr == True:
			nou_text = nou_text + i.upper()
			if i != " ":
				uppr = False
		elif uppr == False:
			nou_text = nou_text + i
		if i == ".":
			uppr = True
	return nou_text


text = input("Dime el texto: ")

print(Upper(text))

'''

def checkUpper(text):
	nouText=text[0]
	#Codi per transformar a majúscules
	nouText = text[0].upper()
	for pos in range(1,len(text)):
		if (text[pos-1] == ".")  or (text[pos-2] == "."):
			nouText=nouText+text[pos].upper()
		else:
			nouText=nouText+text[pos]
	return nouText

text=input("Entra el text")
print(checkUpper(text))


