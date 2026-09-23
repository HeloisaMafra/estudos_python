#Desafio 13:
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15%:

salario = float(input('Digite seu salário: '))
novo_salario = salario + (salario * 0.15)
print('Antes o seu salário era de {}, mas agora com 15% de aumento, passou a ser {}'.format(salario, novo_salario))
