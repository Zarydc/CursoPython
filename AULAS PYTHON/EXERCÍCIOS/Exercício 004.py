#----------------DESAFIOS!!!!-----------------

# DESAFIO 005: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antessessor.
# DESAFIO 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#-----------------------------------------DESAFIO 005---------------------------------------

#n = int(input('\nDigite um número inteiro:'))

#print('\nVocê digitou {}\n'.format(n))
#print('\nO antecessor de {} é {}\n'.format(n, n - 1))
#print('\nO sucessor de {} é {}\n\n'.format(n, n + 1))


#-----------------------------------------DESAFIO 006---------------------------------------

#n = int(input('\nDigite um número inteiro:'))

#print('\nVocê digitou {}\n'.format(n))
#print('\nO dobro de {} é {}\n'.format(n, 2 * n))
#print('\nO triplo de {} é {}\n\n'.format(n, 3 * n))
#print('\nA raiz quadrada de {} é {}\n\n'.format(n, n ** 0.5))

#---------------------------------------DESAFIO 007--------------------------------------
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#print("\n PRODUTOS DA LOJA\n\nA - Camisa R$34,49\nB - Calça R$79,90,00\nC - Cinto R$9,90\nD - Boné R$49,00")
#print('\nE - Vestido R$79,98\nF - Saia R$15,90\nG - Sapato boho R$99,90')

#A = (34.49 - (34.49*0.05))
#B = (79.90 - (79.90*0.05))
#C = (9.90 - (9.90*0.05))
#D = (49.90 - (49.90*0.05))
#E = (79.98 - (79.98*0.05))
#F = (15.90 - (15.90*0.05))
#G = (99.90 - (99.90*0.05))


#p = int(input('\nDigite a LETRA do produto desejado: '))

#print('O seu produto é {}\n'.format(p, )) # código não finalizado. Saber sobre laços for, if, else ou coisa do tipo.

#----------------------------------------------------------------------------------------------------------------------------
#----------------DESAFIO 007 - SIMPLIFICADO----------------------------------------------------------------------------------

#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#valor = int(input('\nValor do Produto: R$ '))

#d = (valor - (valor*0.05))

#print('\n O valor do produto é: R${}\nValor com 5% de desconto: R${}\n'.format(valor, d))


#----------------DESAFIO 008 ----------------------------------------------------------------------------------

#Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento.


nome = input('\nNome do funcionário: ')
salario = int(input('\n\nSalário de {}: R$ '.format(nome)))

aumento = (salario + (salario*0.15))

print('\n\nSalário de {} com 15% de aumento: R${}\n\n\n'.format(nome, aumento))
