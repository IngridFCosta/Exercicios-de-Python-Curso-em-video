"""082- Crie um programa que vai ler vários números
e colocar em uma lista. Depois disso, crie duas
listas extras que vão contar apenas os valores pares e
impares digitados, respectivamente.
No final, mostre o conteúdo das três listas geradas.
"""

listaNumeros=list()
listaPares=list()
listaImpares=list()

while True:
    numero=int(input('Insira um número inteiro: '))
    listaNumeros.append(numero)
    continuar=' '
    continuar=str(input('Deseja continuar? S/N ')).upper().strip()[0]
    while continuar not in 'SN':
        print('Você informou um dado invalido!Tente novamente')
        continuar = str(input('Deseja continuar? S/N')).upper().strip()[0]
    if continuar =='N':
        print('Programa encerrado!')
        break
for i in range(0,len(listaNumeros)):
    if listaNumeros[i]%2==0:
        listaPares.append(listaNumeros[i])
    else:
        listaImpares.append(listaNumeros[i])
print(listaNumeros)
print(f'Lista pares: {listaPares}')
print(f'Lista Impares: {listaImpares}')