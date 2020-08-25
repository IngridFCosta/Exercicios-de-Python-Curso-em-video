"""025- Crie um programa que leia o nome
de uma pessoa e diga se ela tem 'SILVA'"""

nome=str(input('Escreva seu nome completo:')).strip().upper()
if 'SILVA' in nome:
    print('Você possui o sobrenome SILVA')
else:
    print('Você não possui o sobrenome SILVA')
