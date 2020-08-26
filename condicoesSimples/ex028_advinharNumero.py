"""028-Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random
numero=int(input('Escreva um numero inteiro menor ou igual a 5:'))
numSorteado=random.randint(0,5)

if numero > 5:
    print('\033[0;31mVocê digitou um numero acima de 5.Tente novamente:\033[m')
    numero = int(input('Escreva um numero inteiro:'))
    if numero == numSorteado:
        print('\033[0;32mParabéns, você ganhou! Acertou o numero que o computador pensou!\033[m')
    else:
        print('Que pena, você perdeu!')
        print('O numero sorteado pelo computador foi: {}'.format(numSorteado))
else:
    if numero == numSorteado:
        print('Parabéns, você ganhou! Acertou o numero que o computador pensou!')
    else:
        print('Que pena, você perdeu!')
        print('O numero sorteado pelo computador foi: {}'.format(numSorteado))