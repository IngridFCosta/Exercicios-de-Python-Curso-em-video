"""101- Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma
pessoa tem voto NEGADO, OPCIONAL, ou OBRIGATÓRIO nas eleições."""



def voto(anoNascimento):
    from datetime import date
    anoAtual = date.today().year
    idade=anoAtual-anoNascimento
    if idade < 18:
        return f'Com {idade} anos o voto é negado'
    elif idade < 18 and idade >=16 or idade > 65:
        return f'Com {idade} anos o voto é opcional'
    elif idade >=18:
        return f'Com {idade} anos o voto é  obrigatório'

nascimento=int(input('Qual sua data de nascimento?'))
print(voto(nascimento))