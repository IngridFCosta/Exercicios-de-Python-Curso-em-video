"""075- Desenvolva um programa que leia quatros valores
pelo teclado e guarde-os em uma tupla. No final mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3
c) Quais foram os numeros pares
"""
numero1=int(input('Escreva o primeiro numero: '))
numero2=int(input('Escreva o segundo numero: '))
numero3=int(input('Escreva o terceiro numero: '))
numero4=int(input('Escreva o quarto número: '))

tNumeros=(numero1,numero2, numero3, numero4)

#a
valor9=tNumeros.count(9)
print(f'O valor 9 apareceu {valor9} vez(es)')

#b
if 3 in tNumeros:
    valor3=tNumeros.index(3)
    print(f'O numero 3 aparece a primeira vez na posição {valor3}')
else:
    print('O numero não existe na tupla')
#c
print('Os pares são:', end=' ')
for cont in tNumeros:
    if cont %2==0:
        print(f'{cont}',end=' ')
