#Faça um pogramaque solitice a data de nascimento dd/mm/aaaa e imprima com o nome do mês por extenso. dd de Mês de aaaa
#TWP286 2.1 - TWP286 Strings Exercício Mês por Extenso
dia, mês, ano = input("Data (dd/mm/aaaa): ").split('/')
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
print('Você nasce em:')
print("%s de %s de %s" %(dia, meses[int(mês) -1], ano))
