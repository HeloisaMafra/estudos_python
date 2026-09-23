#Desafio 7:
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média:

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: ' ))
soma = nota1 + nota2
media = (nota1 + nota2) /2
print('A primeira nota foi {}, a segunda nota foi {}, tendo como média {}'.format(nota1, nota2, media))