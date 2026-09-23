#Desafio 46:
#Cria um programa com for que leia um numero na tela e vá diminuindo -1 até chegar em 0:
n = int(input('Digite um número inteiro: '))

for c in range(n, -1, -1):
    print(c)

print('Fim')