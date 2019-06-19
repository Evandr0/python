#Exercicio TWP270
notas = [7.5, 8, 6, 8.4, 9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print ("Média: %5.2f" % (soma/x))
