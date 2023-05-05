# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#from math import trunc
#num = float(input('\n\nDigite um número decimal qualquer: '))
#print('\n\nO número {} tem a parte inteira igual a {}.\n\n'.format(num, trunc(num)))

#######CONCLUÍDO#######

#OUTRA FORMA DE FAZER O CÓDIGO: forma 01

#import math

#n2 = float(input('\n\nDigite um valor: '))

#print('O valor digitado foi: {}.\nA parte inteira do valor é: {}.\n\n\n'.format(n2, math.trunc(n2)))

####FORMA 2: SEM IMPORTAR A BIBLIOTECA MATH.

n2 = float(input('\n\nDigite um valor: '))
print('O valor digitado foi: {}.\nA parte inteira do valor é: {}.\n\n\n'.format(n2, int(n2)))