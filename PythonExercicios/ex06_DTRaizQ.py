#06- Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
from math import sqrt

numero=int(input("Escreva o número:"))
dobro=numero*2
triplo=numero*3
raizQuadrada= sqrt(numero)

print('Número: {}'.format(numero))
print('Dobro: {}'.format(dobro))
print('Triplo: {}'.format(triplo))
print('Raiz quadrada: {}'.format(raizQuadrada))