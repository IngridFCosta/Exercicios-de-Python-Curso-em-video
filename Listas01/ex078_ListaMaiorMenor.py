"""078- Faça um programa que leia 5 valores e
guarde-os em uma lista.
No final, mostre qual foi o maior e o menor
valor digitados e as suas respectivas
posições na lista."""

listaNumero=list()
for cont in range(0,5):
    listaNumero.append(int(input('Escreva um número: ')))
print(f'Lista dos números {listaNumero}')

print(f'O maior valor é {max(listaNumero)} nas posições ', end='')
for posicao, valor in enumerate(listaNumero):
    if valor==max(listaNumero):
        print(f'{posicao+1}ª ...', end='')
print()
print(f'O menor valor é {min(listaNumero)} e está nas posições ', end='')
for posicao, valor in enumerate(listaNumero):
    if valor==min(listaNumero):
        print(f'{posicao+1}ª...', end='')

