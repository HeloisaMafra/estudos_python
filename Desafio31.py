#Desafio 31:
#Crie um programa que calcule o preço da viagem, 0,50 por km ou 0,45 acima de 200km + preço passagem:
distancia = float(input('Digite a distancia da sua viagem: '))
if distancia >= 200:
    print('O preço por km é de R$ 0,45 por isso a distancia totalizou: ', distancia * 0.45 )
else:
    print('O preço por km é de R$ 0.50 por isso seu custo de distancia totalizou: ', distancia * 0.50 )
valor_total = distancia + 32.50
print('O valor total da viagem saiu a {}'. format(valor_total))
