print("Hola")
llargada = int(input("Dime la llargada"))
altura = int(input("Dime la altura"))
anchura = int(input("Dime la anchura"))
a = (llargada*llargada*anchura) + (llargada*anchura*altura) + (llargada*altura*llargada)
lp = llargada*anchura
alp =	llargada*altura
anp = altura*anchura
if lp < alp and lp < anp:
	p = lp
	print(a + p)
elif alp < lp and alp < anp:
	p = alp
	print(a + p)
elif anp < lp and anp < alp:
	p = anp
	print(a + p)