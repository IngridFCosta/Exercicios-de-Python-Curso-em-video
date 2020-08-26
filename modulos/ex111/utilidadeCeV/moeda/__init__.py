"""111-Crie um pacote chamado utilizadadesCeV
qe tenha dois módulos internos chamados moeda e dado.

tranferia todas as funções utlizadasnos desafios 107,
108, e 109 para o primeiro pacote e mantenha tudo funcionando.
"""
def aumentar(valor,taxaAumento,formatar=False):
    resposta=valor+(valor*taxaAumento)/100
    return resposta if formatar==False else moeda(resposta)


def dobro(valor, formatar=False):
    resposta=valor*2
    return resposta if formatar==False else moeda(resposta)

def diminuir(valor, taxaDecrescimo, formatar=False):
    resposta=valor-(valor*taxaDecrescimo)/100
    return resposta if formatar==False else moeda(resposta)


def metade(valor=0, formatar=False):
    resposta=valor/2
    return resposta if formatar==False else moeda(resposta)


def moeda(valor=0,moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')



def resumo(valor,aumento=20,decrescimo=10):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado ------\t {moeda(valor)}')
    print(f'Dobro do preço ------ \t{dobro(valor,True)}')
    print(f'Metade do preço ------ \t{metade(valor, True)}')
    print(f'Aumento ------------ \t{aumentar(valor,aumento, True)}')
    print(f'Decrescimo -------- \t{diminuir(valor,decrescimo, True)}')
