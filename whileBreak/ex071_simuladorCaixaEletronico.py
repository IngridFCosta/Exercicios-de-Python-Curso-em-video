"""
071- Crie um programa que simule o funcionamento de um caixa
eletronico. No inicio pergunte ao usuario qual será o valor a ser
sacado ( numero inteiro) e o programa vai informar quantas  cedulas
de cada algarismo serão entregues.
"""
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor=int(input('Que valor você quer sacar? R$ '))
total=valor
ced=50
totalCed=0
while True:
    if total>=ced:
        total-=ced
        totalCed+=1
    else:
        if totalCed>0:
            print(f'Total de {totalCed} cedulas de R${ced} reais')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        totalCed=0
        if total==0:
            break