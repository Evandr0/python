#Programa das latas
m = int(input("Metros: "))
if m % 54 !=0:
    latas1 = int(m/54) +1
else:
    latas1 = m/54
elatas = "latas"
if latas1 <= 1:
	elatas = "Lata"
else:
	elatas = "Latas"
	
valor = latas1 * 80

print ("%d %s a um custo de %.2f" %(latas1, elatas, valor))
