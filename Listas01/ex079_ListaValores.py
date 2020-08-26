"""079- Crie um programa onde o usuario possa
digitar vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro, ele
não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""

listaNumeros=list()
while True:
    numero=(int(input('Digite um numero: ')))
    if numero not in listaNumeros:
        listaNumeros.append(numero)
    else:
        print('O valor já existe na lista! Não será adicionado')
    continuar =''
    continuar = str(input('Deseja continuar? S/N ')).upper().strip()[0]
    while continuar not in 'SN':
        print('Você informou um dado invalido! Tente novamente')
        continuar = str(input('Deseja continuar? S/N ')).upper().strip()[0]
    if continuar =='N':
        print('Programa encerrado!')
        break
print(f'Os valores da lista são :{listaNumeros}')
listaNumeros.sort()
print(f'Os valores da lista em ordem crescente: {listaNumeros}')


