"""080- Crie um programa onde o usuário possa
digitar cinco valores númericos e cadastre-os
em uma lista, já na posição correta de inserção
(sem usar o sort)
No final, mostre a lista ordenada na tela.
"""
#1º passo: criar a lista
#2º passo: Ler numeros com for

listaNumero=list()
for cont in range(0,5):
    numero=int(input('Escreva um valor: '))
    if cont==0: #verificar primeiro
        listaNumero.append(numero)
    elif numero > listaNumero[len(listaNumero)-1]:# Se numero for maior que o numero do ultimo elemento
        listaNumero.append(numero)
    else:# verificar em cada posição se o numero que será inserido é menor ou igual a ele
        pos=0
        while pos < len(listaNumero):
            if numero <= listaNumero[pos]:
                listaNumero.insert(pos, numero)
                break
            pos+=1
print(f'Os Valores da lista são: {listaNumero}')
