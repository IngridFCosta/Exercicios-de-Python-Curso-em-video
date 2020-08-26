"""099- faça um programa que tenha uma função
chamda maior(), que receba vários parametros
com valores inteiros.
Seu programa tem que analisar todos os valores
e dizer qual deles é o maior.
"""
#1ª soluçõa
'''def maior(*num):
    maior=max(*num)
    print(f'O maior valor é: {maior}')


maior(100,2,3,4,5,6,7,8,39,20)'''
#2ª solução

def maior2(*num):
    cont=maior=0
    for valor in num:
        print(f'{valor}', end=' ')
        if cont==0:
            maior=valor
        else:
            if valor>maior:
                maior=valor
        cont+=1
    print()
    print(f'O maior valor informado foi {maior}')
maior2(100,200,2,3,4,1,1000)
