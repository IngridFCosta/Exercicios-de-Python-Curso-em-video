"""030- Crie um porograma que leia um numero inteiro e
mostre na tela se ela é PAR ou IMPAR"""

numero=int(input('Escreva um número inteiro:'))

if numero % 2==0:
    print('O numero {} é par'.format(numero))
else:
    print('O numero {} é impar'.format(numero))