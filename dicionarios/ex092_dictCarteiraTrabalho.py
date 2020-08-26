"""092- Crie um programa que leia nome, ano de nascimento
e carteira de trabalho e cadastre-os(com idade) em um
dicionário se por caso a CTPS for diferente de zero, o
dicionário receberá também o ano de contratação e o sálario.
Calcule e acrescente, além da idade, com quantos anos a
pessoa vai se aposentar."""

from datetime import date
anoAtual=date.today().year
anosContribuicao=35
cadastro={}

cadastro['Nome']=str(input('Escreva o nome: '))
cadastro['Ano de Nascimento']=int(input('Escreva o ano de nascimento: '))
cadastro['idade']=anoAtual-cadastro['Ano de Nascimento']
cadastro['CTPS']=int(input('Escreva o número da Carteira de Trabalho: '))

if cadastro['CTPS']!=0:
    cadastro['Ano De Contratacao']=int(input('Escreva o ano de contratação: '))
    cadastro['Salario']=float(input('Escreva o sálario: '))

tempContribuicao=anoAtual-cadastro['Ano De Contratacao']
cadastro['Idade de aposentadoria']=cadastro['idade']+anosContribuicao-tempContribuicao
for k, v in cadastro.items():
    print(f'{k} => {v}')