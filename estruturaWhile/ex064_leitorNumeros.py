"""064- Crie um programa que leia vários
números inteiros pelo teclado. O programa só
vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a SOMA entre eles
(desconsiderando o flag).
"""

soma=0
numero=0
qtdNumero=0
numero=int(input('Escreva um numero [999 pra parar]:'))
while numero != 999:
    soma+=numero
    qtdNumero+=1
    numero = int(input('Escreva um numero [999 pra parar]:'))
print('Quantidade de numeros: {}'.format(qtdNumero))
print('A soma é : {}'.format(soma))