"""039- Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
-Se é hora de se alistar
- Se já passou da hora de se alistar
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
"""
from datetime import date
anoAtual=date.today().year
dataNascimento=int(input('Escreva seu ano de nascimento: '))
idade=anoAtual-dataNascimento

if idade < 18:
    print('Você ainda irá se alistar! faltam {} anos para o alistamento'.format(18-idade))
elif idade == 18:
    print('Você ja tem {} anos! Está na hora de se alistar!'.format(idade))
else:
    print('Parece que seu alistamento não aconteceu no prazo! Você está {} anos atrasado!'.format(idade-18))


