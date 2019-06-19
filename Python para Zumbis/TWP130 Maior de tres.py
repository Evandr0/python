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
