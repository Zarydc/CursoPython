#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

h = float(input('\n\nAltura da parede, em metros: '))
l = float(input('\n\nLargura da parede, em metros:'))

area = h * l
Qtinta = area / 2

print('\n\nA parede tem {:.4f} m².\n'.format(area))
print('São necessários {:.4f} litros de tinta para pintar uma parede de {:.4f} m².\n\n\n'.format(Qtinta, area))