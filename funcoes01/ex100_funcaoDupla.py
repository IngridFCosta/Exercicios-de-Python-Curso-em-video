"""100- Faça um programa que tenha uma lista chamada
numeros e duas funções chamadas sorteia() e somaPar().
A primeira vai sortear 5 numeros e vai coloca-los
dentro da lista e a segunda função vai mostrar a soma
entre todos os valores PARES sorteados pela função anterior."""

from random import randint
from time import sleep
numero=list()

def sorteia():
    for cont in range(1,6):
        sorteio = randint(0, 10)
        numero.append(sorteio)
    print(numero)

def somaPar():
    soma = 0
    for cont in numero:
        if cont%2==0:
            soma=soma+cont
    print(f'A soma dos pares é: {soma}')

print('-='*30)
print('Lista com os números sorteados: ', end='')
sorteia()
somaPar()
print('-='*30)