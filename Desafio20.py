#Desafio 20:
#O professor quer sortear a ordem de apresentação dos 4 alunos:

import random
apresentacao1 = str(input('Digite o tema: '))
apresentacao2 = str(input('Digite o tema: '))
apresentacao3 = str(input('Digite o tema: '))
apresentacao4 = str(input('Digite o tema: '))
temas = [apresentacao1, apresentacao2, apresentacao3, apresentacao4]
random.shuffle(temas)
print('A ordem das apresentações será: ')
print(temas)