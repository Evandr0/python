#TWP053 - 7.1
>>> print ('Alô') #Isto é um comentário
Alô
>>> #Calcular quantos digitos tem 2 ** 1000000
>>> 2**10
1024
>>> 1**100
1
>>> 2**100
1267650600228229401496703205376
>>> a = str(2**100)
>>> len(a)
31
>>> a = str(2**1000000)
>>> len(a)
301030
>>> 

#Ou pode ser usado da seguinte forma

a = len(str(2**1000000)))
#============================================
#TWP100
#Tomando decisões de qual código rodar em Python
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
if a>b:
    print('O primeiro número é o maior, ele é:', a)
if b>a:
    print('O segundo número é o maior, ele é:', b)

#=====Carro velho
velho = 3
idade = int(input('Digite a idade do seu carro: '))
if idade <=velho:
    print('Seu carro é novo')
if idade >velho:
    print('Seu carro é velho')


#==== Verifica a velocidade permitida e aplica multa de 5 reais por km acima da velocidade permitida
vl_p = 110 #Velocidade permitida = 110
velocidade = int(input('Digite a velocidade: '))
if velocidade <= vl_p:
    print('Velocidade permitida')
if velocidade > vl_p:
    multa = 5*(velocidade - vl_p)
    print('Você foi multado no valor de R$%i,00' %multa)

##Conta telefonica meu código
print('Conta telef empresa TCHAU')
abx200 = 0.20
medio = 0.18
acima = 0.15
minutos1 = int(input('Digite quantos minutos foram gastos:'))
if minutos1 < 200:
    gasto = minutos1*abx200
    print('O valor gasto foi R$%.2f' %gasto)
if 400 > minutos1 > 200:
    gasto = minutos1*medio
    print('O valor gasto foi R$%.2f' %gasto)
else:
    gasto = minutos1*acima
    print('O valor gasto foi R$%.2f' %gasto)
	
#código da aula

if minutos < 200:
    preço = 0.20
else:
    if minutos <= 400:
        preço = 0.18
    else:
        preço = 0.15
print('Connta telefônica: R$%5.2f' %(minutos*preço)) #%5.2fsignifica 5 posições no float sendo 2 depois do ponto


#Plano 800 0.08 usando elif

minutos = int(input('Digite os minutos gastos:'))
if minutos < 200:
    preço = 0.20
elif minutos <= 400:
    preço = 0.18
elif minutos <= 800:
    preço = 0.15
else:
    preço = 0.08
print('Connta telefônica: R$%6.2f' %(minutos*preço))

#TWP200 - Loop - Repetição
x =1
while x<=3:
    print (x)
    x = x+1

	
#Imprima de 1 até um número digitado pelo usuário
x =1
numero = int(input('Digite um número:'))
while x<= numero:
    print (x)
    x = x+1


#Imprima os numeros pares.
x =1
numero = int(input('Digite um número:'))
while x<= numero:
    if x %2==0:
        print (x)
    x = x+1


#TWP230 - Acumuladores
#TWP230 - Acumuladores
n = 1
soma = 0
while n<=10:
    x = int(input('Digite o %d número: ' %n))
    soma = soma + x
    n = n + 1
print ('Soma: %d' %soma)

#while true

soma = 0
while True:
    x = int(input('Digite o número (ZERO PARA SAIR): '))
    if x == 0:
        break
    soma = soma +x
print ('Soma: %d' %soma)


#TWP260 Repetições aninhadas, Tabuada de 10
tabuada = 1
while tabuada <=10:
    n =1
    print ('Tabuada do %d' %tabuada)
    while n<=10:
        print ("%d x %d = %d" %(tabuada, n, tabuada * n))
        n = n +1
    tabuada = tabuada +1
    
'''
Comentário 
de várias
linhas
Faça um programa que leia três números e mostre o maior deles.
'''
'''
Faça um programa que leia três números e mostre o maior deles.
Comentário de várias linhas
'''
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o primeiro número: '))
c = int(input('Digite o primeiro número: '))

if a>= b and a >= c:
    print ("O primeiro número é o maior %d" %a)
elif b >=c:
    print ("O segundo número é o maior %d" %b)
else:
    print ("O terceiro número é o maior %d" %c)

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

'''Verificar se é um triangulo e dizer
qual tipo do triangulo'''
a= int(input('Lado a: '))
b= int(input('Lado b: '))
c= int(input('Lado c: '))
if a> b + c or b>a+c or c>a+b:
    print('Não pode ser um triângulo')
    print('Um dos lados é maior que a soma dos outros')
elif a == b == c:
    print('Equilátero')
elif a== b or b==c or a==c:
    print('Isósceles')
else:
    print('Escaleno')
#TWP140 - Parei nesse.

==========

#Listas []

edifício = ["Familia Souza", "Familia Brito", "Sr Jorge", "Familia Tanaka"]
print (edifício[0])
print (edifício[1])


my_words = ["Dudes", "and"]
my_words.append("Bettys") #Irá adicionar a palavra Bettys na variavel my_words
"""podem ser adicionadas vários tipos de variáveis"""
print(my_words) # ['Dudes', 'and', 'Bettys']

print(my_words[2]) ##==Bettys



list = [] #Lista vazia 

notas = [7.5, 9, 8.3]

print (notas[0]) #Acessando a notas
notas [0] = 8.7 #Mudando a primeira nota, editar nota + posição.

print (notas[0])


#Fazer exercicio final do video TWP270

#Exercicio TWP270
notas = [7.5, 8, 6, 8.4, 9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print ("Média: %5.2f" % (soma/x))

#TWP271


#Ver video TWP273
#Faça um programa que leia um vetor de dez numeros reais e mostre-os na ordem inversa

vetor = []
i = 1
while i <=10:
	n = float(input("Digiteum número: "))
	vetor.append(n)
	i += 1
i = 9
while i >=0:
	print (vetor[i])
	i -= 1
#################
#TWP274
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

#outra forma de fazer 274
notas = []
media = 0
i = 1
while i <=4:
	n = float(input("Nota: "))
	notas.append(n)
	media += n
	i += 1
print ("Notas:", notas)
print ("Média: ", media/4)
####

# TWP275 Contar consoantes

letras = []
i = 1
while i<=10:
    letras.append(input("Letra: "))
    i += 1
i = 0
cont = 0
while i<=9:
    if letras[i] not in 'aeiou':
        cont += 1
    i += 1
print ("Foram lidos %d consoantes" %cont)
####

# TWP280 Strings
#Fatiamento
x = "0123456789"
print (x[0:2])
>>> 
01
print (x[1:2])
1
print (x[2:4])
23
print (x[0:5])
01234
print (x[4:-1]) #-1 = último
45678
print (x[4:]) #Do 4 até o fim.

#Usar incremento ao fatir a string
texto = "batatinha quando nasce"
texto[::2] #Inicio até o final, pulando de 2 em 2.
'bttanqd ac'
texto[::-1] #-1 neste caso inverte a frase.
'ecsan odnauq ahnitatab'


#TWP282 Strings Palíndromes
# TWP280 Strings - TWP282 Strings Palíndromes
#verifique se uma palavra é palindrome
palavra = input("Palavra: ")
if palavra == palavra[::-1]:
    print ("%s é palindrome" %palavra)
else:
    print ("%s não é palindrome" %palavra)

#TWP283 Strings são imutáveis
texto = 'Alô Mundo'
texto = '@' + texto[1:0]
print (texto)
>>>
#@lô Mundo

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

arquivo = 'prog.py'
arquivo.startswith ('p') #Começa com p ?
True
arquivo.endswith ('py') #Termina com py?
True

resposta = "Sim"
resposta.lower()
'sim'
resposta.upper()
'SIM'
resposta.lower() in 'sim não yes no'
True

#find e replace
>>> s = 'um tigre, dois tigres, três tigres'
>>> s.find('tigre')
3
>>> s.find('tigre', 4)
15
>>> s.find('tigre', 15)
15
>>> s.find('tigre', 16)
28
>>> s.replace('tigre','gato')
'um gato, dois gatos, três gatos'
>>> s
'um tigre, dois tigres, três tigres'
>>> s = s.replace('tigre','gato')
>>> s
'um gato, dois gatos, três gatos'
>>> 

#split e join  (split = separa e join = junta)
>>> txt = 'batatainha quando nasce'
>>> txt.split()
['batatainha', 'quando', 'nasce']
>>> data = '21/02/2011'
>>> data.split('/')
['21', '02', '2011']
>>> ip = '192.188.10.144'
>>> ip.split('.')
['192', '188', '10', '144']
>>> ip.split()
['192.188.10.144']
>>> split()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    split()
NameError: name 'split' is not defined
>>> ip
'192.188.10.144'
>>> 
>>> times = ['Figueirense','Palmeiras','Santos']
>>> '/'.join(times)
'Figueirense/Palmeiras/Santos'
#2.1 - TWP285 String Métodos
#Faça um pogramaque solitice a data de nascimento dd/mm/aaaa e imprima com o nome do mês por extenso. dd de Mês de aaaa
dia, mês, ano = input("Data (dd/mm/aaaa): ").split('/')
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
print('Você nasce em:')
print("%s de %s de %s" %(dia, meses[int(mês) -1], ano))


#2.1 - TWP286 Strings Exercício Mês por Extenso





























