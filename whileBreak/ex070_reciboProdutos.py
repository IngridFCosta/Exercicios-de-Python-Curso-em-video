"""070- Crie um programa que leia o nome e o preço
de vários produtos. O programa deverá perguntar
se o usuário vai continuar. No final, mostre:
a) Qual é o total gasto na compra
b) Quantos produtos custam mais de R$ 1000
c) Qual é o nome do produto mais barato
"""

totCompra=0
prodMil=0
prodBarato=' '
cont=menor=0
while True:
    nome=str(input('Escreva o nome do produto: '))
    preco=float(input('Escreva o preço do produto R$: '))
    cont += 1
    totCompra = preco + totCompra

    if preco > 1000:
        prodMil+=1
    if cont==1:
        menor=preco
        prodBarato=nome
    else:
        if preco < menor:
            menor=preco
            prodBarato=nome
    continuar = ' '
    while continuar not in 'SN':
        continuar=str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar =='N':
        break
print(f'O produto mais barato é:{prodBarato}')
print(f'Produtos acima de R$ 1000: {prodMil}')
print(f'Total da compra: {totCompra}')




