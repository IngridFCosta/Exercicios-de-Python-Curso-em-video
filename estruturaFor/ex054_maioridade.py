"""054- Crie um programa que leia o ano de nascimento de sete
pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.
"""

from datetime import date
maior=0
menor=0
for contagem in range(1,8):
    anoNascimento=int(input('Escreva a sua data de nascimento: '))
    maioridade= date.today().year-anoNascimento
    if maioridade >=18:
        maior+=1
    else:
        menor+=1
print('{} pessoas já atingiram a maioridade e {} pessoas ainda não não maiores'.format(maior, menor))





