"""108- Adapte o código do desafio 107, criando uma função
adiconal chamada moeda() que consiga mostrar os valores como
um valor monetário."""

def aumentar(valor,taxaAumento):
    percentual=(valor*taxaAumento)/100
    return valor+percentual


def dobro(valor):
    return valor*2


def diminuir(valor, taxaDecrescimo):
    percentual = (valor * taxaDecrescimo) / 100
    return valor-percentual


def metade(valor=0):
    return valor/2


def moeda(valor=0,moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')
