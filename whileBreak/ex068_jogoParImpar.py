"""068- Faça um programa que jogue PAR ou IMPAR com  o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo """

import random
resultado='GANHOU'
vitorias=0
print('Vamos jogar par ou impar?\n'
      '0-Par\n'
      '1-Impar')
while resultado!='PERDEU':
    jogador=int(input('Informe sua escolha: (0 ou 1)? '))
    if jogador==0:
        print('Você escolheu par')
    elif jogador==1:
        print('Você escolheu impar')


    jogadaPlayer=int(input('Informe um numero: '))
    jogadaComputador=random.randint(0,10)
    print(f'Computador escolheu: {jogadaComputador}')

    par=jogadaPlayer+jogadaComputador
    print('-' * 20)
    if par%2==0:
        print('Deu par!')
    else:
        print('Deu impar!')
    print('-' * 20)

    if jogador ==0 and par%2==0 or jogador==1 and par%2!=0:
        print('Parabéns você ganhou!')
        print('-'*20)
        resultado='GANHOU'
        vitorias=vitorias+1
    else:
        resultado = 'PERDEU'
        print('Computador ganhou!')
print(f'O seu numero de vitorias é: {vitorias}')