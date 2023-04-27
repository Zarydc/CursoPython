#--------------DESAFIO 008 ----CONVERSOR DE MEDIDAS-----------------------#

#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros e todas as outras medidas de metros.

# km hm dam m dm cm mm


v = float(input('\n\n Insira um valor (em metros): ')) #chama um objeto numérico pertencente ao conjunto dos números reais.

km = v*(10**-3) #converte o objeto "v" para quilômetros
hm = v*(10**-2) #converte o objeto "v" para hectômetros
dam = v*(10**-1) #converte o objeto "v" para decâmetros
dm = v*(10**1) #converte o objeto "v" para decímetros
cm = v*(10**2) #converte o objeto "v" para centímetros
mm = v*(10**3) #converte o objeto "v" para milímetros


print('\n\n {:.1f} metros equivale a:\n {:.1f} km\n {:.1f} hm\n {:.1f} dam\n {:.1f} dm\n {:.1f} cm\n {:.1f} mm\n\n'.format(v, km, hm, dam, dm, cm, mm))

