#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Em 25/04/2023 - Dólar = 5,07
real = float(input('\nQuanto dinheiro você tem na carteira, reais: R$  '))
dolar = real / 5.07
euro = real / 5.56
won = real / 0.0038

print('\n\nCom R${:.2f} você pode comprar US${:.2f} (Dólar Americano).'.format(real, dolar))
print('\n\nCom R${:.2f} você pode comprar €${:.2f} (Euro).'.format(real, euro))
print('\n\nCom R${:.2f} você pode comprar ₩${:.2f} (Won sul coreano).\n\n'.format(real, won))