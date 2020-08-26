"""087- Aprimore o desafio anterior(086)
mostrando no final:
a) A soma de todos os valores pares digitados
b) A soma  dos valores da terceira coluna
c) O maior valor da segunda linha"""


matriz=[]
lista01=[]
lista02=[]
lista03=[]
somaPares=somaTerceira=0
for x in  range(0,3):
   valor=(int(input('Escreva um numero: ')))
   lista01.append(valor)
for x in  range(0,3):
    valor=(int(input('Escreva um numero: ')))
    lista02.append(valor)
for x in  range(0,3):
    valor=(int(input('Escreva um numero: ')))
    lista03.append(valor)

matriz.append(lista01)
matriz.append(lista02)
matriz.append(lista03)

print('Matriz Formatada')
for lista in matriz:
    for indice in lista:
        print(indice, end='  ')
    print()
#a
for lista in matriz:
    for indice in lista:
        if indice%2==0:
            somaPares+=indice
print(f'A soma dos números pares é: {somaPares}')

#b
print(f'A soma dos valores da terceira coluna é: {matriz[0][2]+matriz[1][2]+matriz[2][2]}')

#c
print(f'Maior valor da segunda linha: {max(matriz[1])}')
