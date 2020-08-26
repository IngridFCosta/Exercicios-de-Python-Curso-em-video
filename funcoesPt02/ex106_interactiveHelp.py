"""106-Faça um mini-sistema que utilize o
INTERACTIVE HELP  do Python. O usuário vai digitar
a palavra 'FIM', o programa se encerrará.
Obs: Use cores
"""
from time import sleep
cores=('\033[m',  #0-Sem cores
'\033[0;30;41m', #1- Vermelho
'\033[0;30;42m', #2-Verde
'\033[0;30;43m', #3-Amarelo
'\033[0;30;44m', #4-Azul
'\033[0;30;45m', #5-Roxo
'\033[7;30m'    #6-Branco
 );

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'',4)
    print(cores[6], end='')
    help(comando)
    print(cores[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tamanho =len(msg)+4
    print(cores[cor], end='')
    print('~'*tamanho)
    print(f'{msg}')
    print('~'*tamanho)
    print(cores[0], end='')
    sleep(1)


# Programa principal
comand=''
while True:
    titulo('SISTEMA DE AJUDA PyHELP',2)
    comand=str(input("Função ou Biblioteca > "))
    if comand.upper() =='FIM':
        break
    else:
        ajuda(comand)
titulo('SO LONG AND GOODBYE', 1)
