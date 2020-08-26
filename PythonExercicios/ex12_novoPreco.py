"""
012- Faça um algoritmo que leia o preço de um produto
e  mostre seu novo preço, com 5% de desconto
"""
preco=float(input('Escreva o preço do produto:'))
novoPreco=preco-(preco*5/100)
print('O novo preço é igual a: {}'.format(novoPreco))