"""052- faça um programa que leia um numero inteiro
e diga se ele é ou não um numero primo"""
total=0
numero=int(input('Escreva um número qualquer: '))
for contagem in range(1, numero+1):
    if numero%contagem==0:
        total+=1 #variavel que armazena o numero total de divisões exatas (resto 0)
if total==2: #se o numero tiver apenas duas divisões exatas( 1 e ele mesmo) ele será primo
    print('O numero é primo!')
else:
    print('O numero não é primo!')

