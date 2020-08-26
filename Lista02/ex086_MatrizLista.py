"""086- Crie um programa que leia uma matriz
de dimensão 3x3 e preencha com valores lidos
pelo teclado.No final, mostre a matriz na
tela, com a formatação correta.

"""

matriz=[]
lista01=[]
lista02=[]
lista03=[]
for x in  range(0,3):
    lista01.append(int(input('Escreva um numero: ')))
for x in  range(0,3):
    lista02.append(int(input('Escreva um numero: ')))
for x in  range(0,3):
    lista03.append(int(input('Escreva um numero: ')))
matriz.append(lista01)
matriz.append(lista02)
matriz.append(lista03)

print('Matriz Formatada')
for lista in matriz:
    for indice in lista:
        print(indice, end='  ')
    print()

