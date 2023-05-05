#DESAFIO 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor 
# do seno, cosseno e tangente desse ângulo.

from math import cos, sin, tan, radians
ang = float(input('\n\nInsira um ângulo: '))

Cos = cos(radians (ang))
Sin = sin(radians(ang))
Tan = tan(radians(ang))

print('\n\nO ângulo é {}°\ncos({}°) = {}\nsin({}°) = {}\ntan({}°) = {}\n\n\n'.format(ang, ang, Cos, ang, Sin, ang, Tan))

####IMPORTANDO TODA A BIBLIOTECA MATH

import math
ângulo = float(input('\n\n\nInsira um ângulo: '))

coss = math.cos(math.radians(ângulo))
seno = math.sin(math.radians(ângulo))
tang = math.tan(math.radians(ângulo))

print('\n\n\nSeno({}°) = {}\nCosseno({}°) = {}\nTangente({}°) = {}'.format(ângulo, seno, ângulo, coss, ângulo, tang))