#Desafio 12:
#Faça um algoritmo de um produto que leia o preço e calcule 5% de desconto mostrando seu novo preço:

preco = float(input('Digite o preço do produto: '))
desconto = preco - (preco * 0.05)
print('O preço original era {}, mas agora com desconto de 5% fica {}'.format(preco, desconto))