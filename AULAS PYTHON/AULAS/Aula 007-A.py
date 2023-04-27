#OPERAÇÕES ARITMÉTICAS - OPERADORES ARITMÉTICOS - parte 01

nome = input('Qual é o seu nome?\n')

print('Prazer em te conhecer, {:20}!' .format(nome)) 
# O '{:20}' vai fazer a string aparecer em um espaço de 20 caracteres.

# COMANDOS DE ALINHAMENTO - ESQUERDA, DIREITA E CENTRO.
# O '{:<20} fará a string aparecer mais a ESQUERDA, em 20 caracteres'
# O '{:>20} fará a string aparecer mais a DIREITA, em 20 caracteres'
# O '{:^20} fará a string aparecer NO MEIO, em 20 caracteres'
# O '{:=^20}' fará a string aparecer ENTRE o sinal de igualdade, em 20 espaços.
# O '{:=>20}' fará a string aparecer a DIREITA do sinal de igualdade, em 20 espaços.
# O '{:=<20}' fará a string aparecer a ESQUERDA do sinal de igualdade, em 20 espaços.

print('Prazer em te conhecer, {:<20}!'.format(nome))
print('Prazer em te conhecer, {:^20}!'.format(nome))
print('Prazer em te conhecer, {:=^20}!'.format(nome))
print('Prazer em te conhecer, {:=>20}!'.format(nome))
print('Prazer em te conhecer, {:=<20}!\n'.format(nome))
