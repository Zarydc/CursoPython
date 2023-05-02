#------MÓDULO 4: AULA 08 - UTILIZANDO MÓDULOS------
import math #Importa TODOS os itens da bliblioteca 'math' 
num = int(input("\nDigite um número inteiro: "))
raiz = math.sqrt(num) #Chama a função para calcular raiz quadrada (sqrt).

print('\nA raiz quadrada de {} é igual a {}.\n'.format(num, raiz)) #mostrará a raiz quadrada com todas as casas decimais.

print('\nResultados da raiz quadrada de {}:\n\n (a) Arredondado para cima: {:.2f}'.format(num, math.ceil(raiz))) #Mostrará o resultado da raiz arredondado para cima.
print('\n (b) Arredondado para baixo: {:.2f}'.format(math.floor(raiz))) #Mostra a raiz arredondada para baixo.
print('\n (c) Sem arredondamento: {:.2f}'.format(raiz))


#------------IMPORTANDO APENAS UM ÚNICO OU ITENS ESPECÍFICOS ITEM DA BIBLIOTECA ------------

from math import pow, sqrt, floor, ceil

n2 = int(input('\n\nDigite um número inteiro: '))
pot = pow(n2, 2)
Rq = sqrt(n2)

print('\n\nA potência do número {}² é: {:.3f}\n\n'.format(n2, pot))
print('-----------------------------\nArredondado para Cima: {}\n'.format(ceil(pot)))
print('\nArredondado para Baixo: {}\n\n-----------------------------------------------------'.format(floor(pot)))

print('\n\n A raiz quadrada de {} é: {:.3f}\n\n'.format(n2, Rq))

print('Arredondando para Baixo: {:.2f} '.format(floor(Rq)))
print('\nArredondamento para Cima: {:.2f}'.format(ceil(Rq)))

