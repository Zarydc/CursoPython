#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para:
#a) Farenheit; b)Kelvin

print('\n\nGRAUS CELSIUS -> GRAUS FARENHEIT & GRAUS KELVIN\n\n')

Tc = float(input('Temperatura em °C: '))

Tf = ((1.8*Tc)+32)

Tk = Tc + 273


print('\n\nConversão de Temperatura: \n{:.2f}°C -> {:.2f}°F\n{:.2f}°C -> {:.2f}°K\n'.format(Tc, Tf, Tc, Tk))
print('\n----------------------------------------------------------------------\n')

