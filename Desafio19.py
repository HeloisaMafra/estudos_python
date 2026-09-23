#Desafio 19:
#Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escolhendo algum.
import random
aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(alunos)
print('O aluno sorteado foi: {}'.format(sorteado))