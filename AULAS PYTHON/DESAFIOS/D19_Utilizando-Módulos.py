#Um professor quer sortear um dos seus QUATRO alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
a1 = str(input('\n\n1° aluno: ')) 
a2 = str(input('\n2° aluno: '))
a3 = str(input('\n3° aluno: '))
a4 = str(input('\n4° aluno: '))

lista = [a1, a2, a3, a4]

sorteio = random.choice(lista)

print('\n\nO aluno que vai apagar o quadro será: {}'.format(sorteio))

