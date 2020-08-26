"""
ex16-  Crie um programa que leia um numero real qualquer e mostre na tela sua porção inteira
"""
from math import trunc
numero=float(input('Escreva um numero real:'))
print('a parte inteira é igual a:{}'.format(trunc(numero)))
