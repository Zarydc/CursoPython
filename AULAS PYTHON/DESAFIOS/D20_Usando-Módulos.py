# O mesmo professor do desafio anterior quer sortear 
#a ordem de apresentação dos trabalhos dos alunos.
# Faça um programa que leia o nome dos QUATRO alunos 
#e mostre a ordem sorteada.

from random import shuffle #shuffle significa embaralhar

a1 = str(input('\n\n1° aluno: ')) 
a2 = str(input('\n2° aluno: '))
a3 = str(input('\n3° aluno: '))
a4 = str(input('\n4° aluno: '))

lista = [a1, a2, a3, a4]
shuffle(lista)

#print('\nA ordem de apresentação é: {}'.format(lista)) #Forma 1 de mostrar

print('\nA ordem de apresentação é: ')
print(lista)

