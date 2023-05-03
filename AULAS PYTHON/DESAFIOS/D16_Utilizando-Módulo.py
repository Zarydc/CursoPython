# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
num = float(input('\n\nDigite um número decimal qualquer: '))
print('\n\nO número {} tem a parte inteira igual a {}.\n\n'.format(num, trunc(num)))

#######CONCLUÍDO#######