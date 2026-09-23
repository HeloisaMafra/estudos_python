#Desafio 11:
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantiade de tinta para pintá-lo, sabendo que cada litro faz 2m²:

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
capacidade_litro = area / 4
print('Sendo a altura {} e a largura {}, a área dessa parede é de {} precisando de {} litros de tinta'.format(altura, largura, area, capacidade_litro))
