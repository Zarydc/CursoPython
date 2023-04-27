#-----------------TABUADA---------------------

#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('\n\nInsira um número inteiro para ver a sua tabuada: '))
print('{} x {} = {}\n'.format(n, 1, n*1))
print('{} x {} = {}\n'.format(n, 2, n*2))
print('{} x {} = {}\n'.format(n, 3, n*3))
print('{} x {} = {}\n'.format(n, 4, n*4))
print('{} x {} = {}\n'.format(n, 5, n*5))
print('{} x {} = {}\n'.format(n, 6, n*6))
print('{} x {} = {}\n'.format(n, 7, n*7))
print('{} x {} = {}\n'.format(n, 8, n*8))
print('{} x {} = {}\n'.format(n, 9, n*9))
print('{} x {} = {}\n\n\n\n'.format(n, 10, n*10))

#Calculadora de Multiplicação de dois números

n1 = float(input('\nDigite um número: '))
n2 = float(input('Digite outro número: '))

mult = n1*n2

print('Resultado da multiplicação:\n\n {:^10.2f} x {:^10.2f} = {:^10.2f}'.format(n1, n2, mult))