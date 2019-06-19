#TWP285 String Métodos

#Faça um programa que leia uma palavra e troque as vogais por "*"

palavra = input("Palavra: ")
k = 0
troca = ""
while k < len(palavra): #len(palavra) len conta o tamanho da palavra
    if palavra[k] in "aeiou":
        troca = troca + "*"
    else:
        troca = troca + palavra[k]
    k+=1
print ("Nova palavra %s" %troca)
