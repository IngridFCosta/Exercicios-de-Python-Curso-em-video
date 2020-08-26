"""-58- Melhore o DESAFIO 028 onde o computador vai 'pensar
em um numero  entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites
foram necessárias para vencer'"""

import random
palpite=0
numero=int(input('Escreva um numero entre 0 e 10: '))
numSorteado= random.randint(0,10)

while numero != numSorteado:
    print('Você perdeu! Tente novamente!')
    numero = int(input('Escreva um numero entre 0 e 10: '))
    if numero==numSorteado:
        print('Você ganhou!')
    palpite+=1
print(f'O total de palpites foi: {palpite}')

