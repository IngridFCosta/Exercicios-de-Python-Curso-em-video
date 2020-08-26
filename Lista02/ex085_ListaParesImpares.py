"""085- Crie um programa onde o usuário possa
digitar sete valores numéricos e cadastre-os em
uma lista única que mantenha separados os valores
 pares e impares. No final, mostre os valores
 pares e impares em ordem crescente"""

listaNumero=[[],[]]
valor=0
for cont in range(0,7):
    valor=int(input(f'Escreva o {cont+1}º valor:'))
    if valor%2==0:
        listaNumero[0].append(valor)
    else:
        listaNumero[1].append(valor)
listaNumero[0].sort()
listaNumero[1].sort()
print(f'Lista completa: {listaNumero}')
print(f'Lista de pares: {listaNumero[0]}')
print(f'Lista de impares: {listaNumero[1]}')
