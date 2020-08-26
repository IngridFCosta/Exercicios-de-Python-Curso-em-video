"""093- Crie um programa que gerencie o aproveitamento
de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols
feitos em cada partida. No final, tudo isso será guardado em um
dicionário, incluindo o total de gols feitos durante o campeonato."""

dadoJogador={}
totalGols=0
listaGol=[]
dadoJogador['Nome']=str(input("Escreva o nome do Jogador: "))
qtdPartidas=int(input('Número de partidas jogadas: '))

for cont in range(1, qtdPartidas+1):
    numeroGols=int(input(f'Número de gols da {cont}ª partida: '))
    listaGol.append(numeroGols)
dadoJogador['Partidas']=qtdPartidas
dadoJogador['Gols']=listaGol

for valor in listaGol:
  totalGols+=valor
  dadoJogador['Total de Gols']=totalGols

print('-'*20, end='')
print('Dados do Jogador', end=' ')
print('-'*20)
print(dadoJogador)
print('-'*70)

for k, v in dadoJogador.items():
    print(f'=> {k} tem valor {v}')
print('-'*30)
print(f'{dadoJogador["Nome"]} jogou {dadoJogador["Partidas"]} partidas')
for pos, valor in enumerate(listaGol):
    print(f'Na {pos+1}º partida o jogador {dadoJogador["Nome"]} marcou {valor} gols')

