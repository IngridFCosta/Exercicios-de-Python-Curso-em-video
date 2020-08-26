"""088- Faça um programa que ajude um jogador
da MEGA SENA a criar palpites. O programa vai
perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 a 60 para cada jogo, cadastrando
tudo em uma lista composto."""

from random import randint
from time import sleep
listaNumSorteados=[]
jogos=[]
total=1
numJogos=int(input('Quantos jogos você deseja gerar? '))
while total <=numJogos:
    contador=0
    while True:
        numeroSorteado=randint(1,60)
        if numeroSorteado not in jogos:
            jogos.append(numeroSorteado)
            contador+=1
        if contador>=6:
            break
    jogos.sort()
    listaNumSorteados.append(jogos[:])
    jogos.clear()
    total+=1
print('-'*30, f'SORTEANDO {numJogos} jogos', '-'*30)

for i, l in enumerate(listaNumSorteados):
    print(f' Jogo {i+1}: {l}')
    sleep(1)
print('PROGRAMA ENCERRADO')
