#Desafio 36:
#Crie um programa com if, else e elif que pergunte o nome e dê uma mensagem na tela:
nome = str(input('Qual o seu nome? '))
if nome == 'Gustavo':
    print('Que nome mais lindo! {}'. format(nome))
elif nome == 'Helena':
    print('Acho lindo o significado desse nome {}'.format(nome))
else:
    print('Esse nome eu não conheço! {}'.format(nome))
