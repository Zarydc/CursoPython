###DESAFIO 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
print('\n\nCÁLCULO DA HIPOTENUSA DE UM TRIÂNGULO RETÂGULO\n\n\nInsira os valores pedidos abaixo: \n')
co = float(input('\nCATETO OPOSTO: '))
ca = float(input('\nCATETO ADJACENTE: '))

hip = math.sqrt((pow(co, 2) + pow(ca, 2)))

print('\n\nCateto oposto = {}\nCateto adjacente = {}\nHipotenusa = {}\n\n\n\n'.format(co, ca, hip))


####IMPORTANDO APENAS ALGUMAS FUNÇÕES DA BIBLIOTECA MATH

from math import sqrt, pow

print('\n\nCÁLCULO DA HIPOTENUSA DE UM TRIÂNGULO RETÂGULO\n\n\nInsira os valores pedidos abaixo: \n')
cO = float(input('\nCATETO OPOSTO: '))
cA = float(input('\nCATETO ADJACENTE: '))

hiP = sqrt((pow(cO, 2) + pow(cA, 2)))

print('\n\nCateto oposto = {}\nCateto adjacente = {}\nHipotenusa = {}\n\n\n\n'.format(cO, cA, hiP))


####SEM IMPORTAR A BIBLIOTECA MATH

print('\n\nCÁLCULO DA HIPOTENUSA DE UM TRIÂNGULO RETÂGULO\n\n\nInsira os valores pedidos abaixo: \n')

Co = float(input('\nCATETO OPOSTO: '))
Ca = float(input('\nCATETO ADJACENTE: '))

Hip = ((Co**2) + (Ca**2))**(1/2)

print('\n\nCateto oposto = {}\nCateto adjacente = {}\nHipotenusa = {}\n\n\n\n'.format(Co, Ca, Hip))
