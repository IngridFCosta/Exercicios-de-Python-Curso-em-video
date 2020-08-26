"""055- Faça um programa que leia o peso
de cinco pessoas. No final, mostre qual foi o
 maior e menor peso lidos"""

maiorPeso=0
menorPeso=1000
for contagem in range(1,4):
    peso=float(input('Escreva o peso:'))
    if peso > maiorPeso:
        maiorPeso=peso
    elif peso < menorPeso:
        menorPeso=peso
print('O maior peso foi {:.2f} e o menor foi de {:.2f}'.format(maiorPeso, menorPeso))
