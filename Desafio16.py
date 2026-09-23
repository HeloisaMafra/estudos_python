#Desafio 16:
#Crie um programa que leia um numero real qualquer e mostre na tela a sua porção inteira:

import math
num = float(input('Digite um numero real: '))
inteiro = math.trunc(num)
print('O numero inteiro é {}'.format(inteiro))

