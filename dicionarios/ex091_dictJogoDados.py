"""091- Crie um programa onde 4 jogadores joguem
um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário. No final, coloque esse
dicionário em ordem, sabendo que o vencedor tirou o maior
número no dado."""

from random import randint
from time import sleep
from operator import itemgetter
resultados={}
ranking=list()
resultados['Jogador 01']=jogador1=randint(1,6)
resultados['Jogador 02']=jogador2=randint(1,6)
resultados['Jogador 03']=jogador3=randint(1,6)
resultados['Jogador 04']=jogadador4=randint(1,6)

print('-'*20, end=' ')
print('RESULTADO', end='')
print('-'*20)
for jogador, valor in resultados.items():
    print(f'O numero sorteado pelo {jogador} é {valor}')
    sleep(1)
ranking=sorted(resultados.items(), key=itemgetter(1), reverse=True)

print('=='*10, end=' ')
print('RANKING',end=' ')
print('=='*10)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
