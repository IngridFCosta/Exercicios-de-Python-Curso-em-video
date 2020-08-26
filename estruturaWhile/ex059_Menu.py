""""059- Crie um programa que leia dois valores e mostre
um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

seu programa deverá realizar a operação solicitada
em cada caso.
"""

valor1= int(input('Informe o primeiro valor: '))
valor2=int(input('Informe o segundo valor: '))
print('-'*50)
print('Escolha uma opção do menu para realizar uma operação:')
print(
'\033[0;31m[1] Somar\n'
'[2] Multiplicar\n'
'[3] Maior\n'
'[4] Novos números\n'
'[5] Sair do programa\033[m')
print('-'*50)

menu=0
while menu != 5:
    menu = int(input('Opção:'))
    if menu ==1:
        soma=valor1+valor2
        print(f'A soma é: {soma}')
    elif menu==2:
        mult=valor1*valor2
        print(f'A valor da multiplicação é: {mult}')
    elif menu==3:
        if valor1 > valor2:
            print(f'{valor1} é o maior')
        elif valor2 >valor1:
            print(f'{valor2} é o maior')
        else:
            print('Não há valor maior!')
    elif menu==4:
        print('Informe os valores novamente!')
        valor1 = int(input('Informe o primeiro valor: '))
        valor2 = int(input('Informe o segundo valor: '))
    elif menu==5:
        print('Programa encerrado!')
    else:
        print('Opção inválida. Tente Novamente:')


