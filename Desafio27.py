#Desafio 27:
#Crie um programa na tela, em que o aluno digite suas duas notas, mostre a média e diga se está aprovado ou não:
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 6:
    print('Você foi aprovado! com média = ', media)
else:
    print('Você está reprovado! com média = ', media)