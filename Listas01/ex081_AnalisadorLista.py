"""081- Crie um programa que vai ler vários números
e colocar em uma lista. Depois disso mostre:

a) Quantos  números foram digitados
b) A lista de valores ordenados de forma decrescente
c) Se o valor 5 foi digitado e está ou não na lista
 """
listaNumeros=list()
while True:
    listaNumeros.append(int(input('Escreva um numero: ')))
    continuar=''
    continuar=str(input('Deseja continuar? S/N ')).upper(). strip()[0]
    while continuar not in 'SN':
        print('Você informou um dado invalido!Tente novamente')
        continuar = str(input('Deseja continuar? S/N ')).upper().strip()[0]
    if continuar =='N':
        print('Programa encerrado!')
        break
if 5 in listaNumeros:
    print('O número 5 foi digitado na lista!')
else:
    print('O número 5 não está na lista!')

print(f'Total de números: {len(listaNumeros)}')
print(f'lista-> {listaNumeros}')
print(f'Ordem decrescente-> {sorted(listaNumeros, reverse=True)}')