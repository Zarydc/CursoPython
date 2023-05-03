#DESAFIO 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor 
# do seno, cosseno e tangente desse ângulo.

from math import cos, sin, tan
ang = float(input('\n\nInsira um ângulo: '))

Cos = cos(ang)
Sin = sin(ang)
Tan = tan(ang)

print('\n\nO ângulo é {}°\ncos({}°) = {}\nsin({}°) = {}\ntan({}°) = {}\n\n\n'.format(ang, ang, Cos, ang, Sin, ang, Tan))