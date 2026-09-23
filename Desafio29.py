#Desafio 29:
#Escreva um programa que leia a velocidade do carro e se passar de 80km/h deve ser multado a 7,00 cada km acima do limite:
velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('você excedeu a velocidade permitida nessa via!')
    print('Você receberá uma multa de {}'.format(multa))
else:
    print('Continue dirigindo, você está dentro da velocidade permitida')