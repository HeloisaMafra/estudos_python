#Desafio 33:
#Crie um programa que leia 3 numeros e mostre qual o maior e o menor:
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
if num1 > num2 and num1 > num3:
    print('O maior número é:', num1)
if num2 > num1 and num2 > num3:
    print('O maior número é:', num2)
if num3 > num1 and num3 > num2:
    print('O maior número é:', num3)
if num1 < num2 and num1 < num3:
    print('O menor número é:', num1)
if num2 < num1 and num2 < num3:
    print('O menor número é:', num2)
if num3 < num1 and num3 < num2:
    print('O menor número é:', num3)

