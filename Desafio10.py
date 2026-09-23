#Desafio 10:
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar:
#Considerando o dólar a 3,27:

valor = float(input('Digite quanto valor você tem na carteira: '))
dolar = valor / 3.27
print('O valor que você tem {}, pode comprar {} dólares.'.format(valor, dolar))
