#Desafio 8:
#Escreva um programa que leia o valor em metros e o exiba convertido em centimentros e milimetros:
num = float(input('Digite um valor em metros: '))
centimetros = num * 100
milimetros = num * 1000
print('O valor em metros: {} foi convertido em {} centimetros e {} milimetros'.format(num, centimetros, milimetros))
