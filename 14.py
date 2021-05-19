def rimaPoesia(poesia):
    text = "no té rima"
    numFrase = 0
    for frase in poesia:
        for pos in range(numFrase+1,len(poesia)):
            if frase[-3:].lower() == poesia[pos][-3:].lower() :
                print(frase)
                print(poesia[pos])
                return "té rima"
        numFrase = numFrase +1    
    return text


poesia1 = ["A la porta", "hi ha una noia"," que camina torta"]
poesia2 = ["Pel camí", "vaig cantant","em trobo un pi", "i callo"]
poesia3 = ["Today jianjing", "is playing", "and  singing","while it's raining"]

print("La poesia ",poesia1,rimaPoesia(poesia1))
print("La poesia ",poesia2,rimaPoesia(poesia2))
print("La poesia ",poesia3,rimaPoesia(poesia3))