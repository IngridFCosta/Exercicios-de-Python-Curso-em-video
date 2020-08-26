"""041- A Confederação Nacional de natação precisa
de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima de 20: MASTER
"""
anoAtual=2020
anoNascimento=int(input('Escreva o ano de nascimento do atleta: '))
idade=anoAtual-anoNascimento

if idade <=9:
    print('CATEGORIA MIRIM')
elif idade > 9 and idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade > 14 and idade < 19:
    print('CATEGORIA JUNIOR')
elif idade >=19 and idade <=20:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')