# Faça um algoritmo que leia o salário de uma funcionário e mostre o seu novo salário, com 15% de aumento.

salario = float(input('\n\nSalário: R$ '))
aumento = (salario + (0.15*salario))
print('\n\nSalário com reajuste de 15%: R${:.2f}\n\n\n'.format(aumento))