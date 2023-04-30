# OPERAÇÕES ARITMÉTICAS - OPERADORES ARITMÉTICOS parte 02
# + (soma)
# - (subtração)
# * (multiplicação)
# ** (potência)
# / (divisão)
# // (divisão inteira)
# % (resto da divisão)

num1 = int(input('\nDigite um número: '))
num2 = int(input('\nDigite outro valor: '))

s = num1 + num2
sub = num1 - num2
d = num1 / num2
di = num1 // num2
m = num1 * num2
p = num1 ** num2
rd = num1 % num2

print('\n{} + {} = {} \n{} - {} = {} \n{} x {} = {} \n{} / {} = {:.2f}\n'.format(num1, num2, s, num1, num2, sub, num1, num2, m, num1, num2, d) )

print('\nA divisão inteira entre {} e {} vale: {} \nO resto desta divisão é {} '.format(num1, num2, di, rd))

print('\nA potenciação de {} elevado a {} é igual a {}\n\n'.format(num1, num2, p))
