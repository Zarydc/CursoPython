#Escreva um programa que pergunte a quantidade em Km percorridos por um carros alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
#o carro custa R$60 por dia e R$0,15 por Km rodado.

print('\n\n------------ALUGUEL DE CARROS------------\n\n')
Qd = int(input('\nQuantidade de dias: '))
Qkm = float(input('\nQuantidade de quilômetros rodados: '))

Va = ((Qd*60)+(Qkm*0.15))

print('\nValor do aluguel: R${:.2f}\n\n'.format(Va))