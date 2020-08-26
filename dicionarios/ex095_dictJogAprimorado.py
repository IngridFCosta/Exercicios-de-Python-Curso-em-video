"""095- Aprimore o desafio 093 para que ele
funcione com vários jogadores, incluindo um sistema
de visualização de detalhes do aproveitamento de
 cada jogador."""

dadoJogador={}
listaGol=[]
listaJogadores=[]

while True:
    dadoJogador.clear()
    dadoJogador['Nome']=str(input("Escreva o nome do Jogador: "))
    qtdPartidas=int(input(f'Número de partidas de {dadoJogador["Nome"]}: '))
    listaGol.clear()
    for cont in range(1, qtdPartidas+1):
       listaGol.append(int(input(f'Número de gols da {cont}ª partida: ')))
    dadoJogador['Gols']=listaGol[:]
    dadoJogador['total']=sum(listaGol)
    listaJogadores.append(dadoJogador.copy())

    continuar=' '
    continuar = str(input('Deseja continuar? (S/N)')).upper().strip()[0]
    while continuar not in 'SN':
        print('Você digitou um dado inválido!Tente novamente!')
        continuar = str(input('Deseja continuar? (S/N)')).upper().strip()[0]
    if continuar == 'N':
        print('Programa encerrado!')
        break
#Cabeçalho- Mostrando resultados
print('-'*45)
print('Cod ', end='')
for i in dadoJogador.keys():
    print(f'{i:<15}', end='')
print()
for i, valor in enumerate(listaJogadores):
    print(f'{i:>3} ', end='')
    for d in valor.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    opcao=int(input('Mostrar dados de qual jogador? 999 para parar '))
    if opcao==999:
        print('Programa encerrado!')
        break
    elif opcao >=len(listaJogadores):
        print('Erro! Jogador não cadastrado!')
    else:
        print(f'Levantamento do jogador {listaJogadores[opcao]["Nome"]}:')
        for indice, gols in enumerate(listaJogadores[opcao]["Gols"]):
            print(f'Na {indice+1}ª partida fez {gols} gols.')
        print('-'*30)
