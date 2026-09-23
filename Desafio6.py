#Desafio 6:
#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('O numero {} tem como dobro {} triplo {} e raiz quadrada {}'.format(num, dobro, triplo, raiz))