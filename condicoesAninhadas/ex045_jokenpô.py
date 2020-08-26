"""045- Crie um programa que faça o computador
jogar JOKENPÔ com você"""

import random
from time import sleep
print('Vamos jogar JOKENPÔ?')
print('-'*20)
print('\033[0;33m1-Pedra\n'
      '2-Papel\n'
      '3-Tesoura\033[m\n')
pedra=1
papel=2
tesoura=3

jogador=int(input('Informe sua escolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

if jogador==1:
    print('Você escolheu pedra!')
elif jogador ==2:
    print('Você escolheu papel')
elif jogador==3:
    print('Você escolheu tesoura')

computador=random.randint(1,4)
if computador==1:
    print('Computador escolheu pedra!')
elif computador ==2:
    print('Computador escolheu papel!')
elif computador==3:
    print('Computador escolheu tesoura!')

if jogador ==1 and computador==3 or jogador==2 and computador==1 or jogador==3 and computador==2:
    print('\033[0;32mParabéns você ganhou!\033[m')
elif jogador ==3 and computador==1 or jogador==1 and computador==2 or jogador==2 and computador==3:
    print('\033[0;34mComputador ganhou!\033[m')
else:
    print('\033[0;35mOps! Parece que tivemos um empate!\033[m')