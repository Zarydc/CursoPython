#Faça um algoritmo que leia o preço de uma produto e mostre o seu novo preço, com 5% de desconto.

preco = float(input('\n\nValor do produto: R$ '))
desc = (preco - (0.05*preco))
print('\n\nO valor com 5% de desconto é R$ {:.2f}.\n\n'.format(desc))

