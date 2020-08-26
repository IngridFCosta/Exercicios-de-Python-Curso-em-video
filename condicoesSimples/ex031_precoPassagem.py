"""031-Desenvolva um programa que pergunte a distância de uma viagem em km
Calcule o preço da passagem, cobrando RS 0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas.
"""
distancia=float(input('Escreva a distância da viagem em KM'))
if distancia <= 200.00:
    passagem= 0.50*distancia
    print('O preço da passagem é igual a {:.2f}'.format(passagem))
else:
    passagem=0.45*distancia
    print('O preço da passagem é igual a {:.2f}'.format(passagem))