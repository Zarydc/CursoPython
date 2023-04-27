#Exercício 004 do curso de PYTHON (Dissecando uma variável) - Faça um programa que leia algo pelo teclado e mostre na tela
#o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ') 
# 'a' é um objeto que possui caracteristicas e tipos

print(f'O tipo primitivo de {a} é ', type(a)) 
#vai dizer qual o tipo do que foi digitado.

print('O que foi digitado só tem espaços? ', a.isspace()) 
#vai dizer se o que foi digitado em 'a' fora espaço ou não.

print(f'{a} é um número? ', a.isnumeric())  
# vai dizer se o que foi digitado é um número ou não.

print(f'{a} é alfabético? ', a.isalpha())  
#vai dizer se o que foi digitado é alfabético ou não.

#se o que foi digitado não conter somente letras, então deve-se fazer o seguinte print()

print(f'{a} é alfanumérico? ', a.isalnum()) 
# vai dizer se o que foi digitado é alfanumérico.

print(f'{a} está em maiúsculo? ', a.isupper()) 
# vai dizer se o que foi digitado está em maiúsculo.

print(f'{a} está em minúsculo? ', a.islower()) 
# vai dizer se o que foi digitado está em minúsculo.

print(f'{a} está capitalizada?', a.istitle())  
# Capitalizada quer dizer se a inicial do que foi digitado é maiúscula ou não.

