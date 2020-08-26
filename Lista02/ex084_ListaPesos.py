"""084- Faça um programa que leia nome e peso de várias
pessoas, guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves

"""
listaPesoTemp=list() #lista temporaria
listaPeso=[]
maior=menor=0
while True:
    listaPesoTemp.append(str(input('Escreva o nome: ')))
    listaPesoTemp.append(float(input('Escreva o peso: ')))
    if len(listaPeso)==0:
        maior=menor=listaPesoTemp[1]
    else:
        if listaPesoTemp[1]>maior:
            maior=listaPesoTemp[1]
        if listaPesoTemp[1]<menor:
            menor=listaPesoTemp[1]
    listaPeso.append(listaPesoTemp[:])# Recebe uma copia da lista
    listaPesoTemp.clear()
    continuar=' '
    continuar=str(input('Deseja continuar? S/N ')).upper().strip()[0]
    while continuar not in 'SN':
        print('Você digitou um dado inválido. Tente novamente!')
        continuar = str(input('Deseja continuar? S/N')).upper().strip()[0]
    if continuar=='N':
        print('Programa encerrado!')
        break
print('-'*40)
print(f'Total de pessoas cadastradas = {len(listaPeso)}')
print(f'Lista dos mais pesados:', end=' ')
for p in listaPeso:
    if p[1] ==maior:
        print(f'[{p[0]}]', end='')
print()
print(f'Lista dos mais leves: ', end=' ')
for p in listaPeso:
    if p[1]==menor:
        print(f'[{p[0]}]', end='')

