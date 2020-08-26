"""060- Faça um programa que leia um numero qualquer
 e mostre seu FATORIAL

 ex- 5!=5x4x3x2x1=120
 """
#Metodo 01
"""from math  import factorial
numero=int(input('Escreva um numero para ser calculado seu fatorial: '))
fat=factorial(numero)
print(f'O fatorial  é {fat}')"""


#Metodo 02
numero=int(input('Escreva um numero para ser calculado seu fatorial: '))
cont=numero
fatorial=1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial=fatorial*cont
    cont-=1
print('{}'.format(fatorial))
