"""
Faça um programa que leia a largura e a altura de uma parede em metros.
Calcule a sua area e a quantidade de tinta necessária para pintá-la, sabendo
que cada litro de tinta pinta uma area de 2m²
"""
largura=float(input('Escreva a largura:'))
altura=float(input('Escreva a altura'))
area=altura*largura

print('Area:{}'.format(area))
qtdTinta=area/2
print('A quantidade de tinta necessária é igual a:{} litro(s)'.format(qtdTinta))

