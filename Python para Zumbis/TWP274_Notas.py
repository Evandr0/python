#Faça um programa que leia quatro nota, mostra as notas e a média na tela
notas = []
i = 1
while i <=4:
    n = float(input("Digite a nota: "))
    notas.append(n)
    i += 1
media = 0
i = 0
while i<=3:
    media+= notas[i]
    i += 1
print ("Notas:", notas)
print ("Média: ", media/4)
