#09- Faça um programa que leia um numero inteiro qualquer e mostre a sua tabuada na tela

numero=int(input('Escreva um número:'))
limiteTab=int(input('Escreva o limite da tabuada:'))

i=0
while i <=limiteTab:
    print('{} + {} = {}'.format(numero,i,numero+i))
    i=i+1


