#-------------------Exercício 007--------------MÉDIA ARITMÉTICA----------------#

#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

p1 = float(input('Nota da Avaliação 1: '))
p2 = float(input('Nota da Avaliação 2: '))

ma = ((p1 + p2)/2)

print('\n\nA média entre {:.2f} e {:.2f} é: {:.2f}\n\n\n'.format(p1, p2, ma))
