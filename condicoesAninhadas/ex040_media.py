"""040- Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final, de acordo com a média
atinginda
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÂO
- Média 7.0 ou superior: APROVADO
"""
nota1=float(input('Escreva a primeira nota: '))
nota2=float(input('Escreva a segunda nota: '))
media=(nota1+nota2)/2

if media < 5.0:
    print('\033[mREPROVADO!')
elif media == 5.0 or media <=6.9:
    print('RECUPERAÇÃO')
elif media >=7.0:
    print('APROVADO!')