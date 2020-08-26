"""103- Faça um programa que tenha uma função
chamada ficha(), que receba dois parâmetros
opcionais: o nome de um jogador e quantos gols
ele marcou.
O programa deverá ser capaz de mostrar a ficha
do jogador, mesmo que algum dado não tenha sido
informado corretamente."""


def ficha(nome='Desconhecido', totalGols=0):
    return print(f'O Jogador {nome} marcou {totalGols} gols.')



nomeJogador=str(input('Escreva o nome do Jogador: '))
totgols=str(input('Escreva o total de gols: '))
if totgols.isnumeric():
    totgols=int(totgols)
else:
    totgols=0
if nomeJogador.strip()=='':
    ficha(totalGols=totgols)
else:
    ficha(nomeJogador, totgols)

