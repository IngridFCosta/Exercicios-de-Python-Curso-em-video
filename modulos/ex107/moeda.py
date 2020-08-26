"""107- Crie um modulo chamado moeda.py
que tenha funções incorporadas aumentar(),
diminuir(), dobro() e metade().
Faça também um programa que importe esses módulos e use
algumas funções.
"""

def aumentar(valor,taxaAumento):
    percentual=(valor*taxaAumento)/100
    return valor+percentual


def dobro(valor):
    return valor*2


def diminuir(valor, taxaDecrescimo):
    percentual = (valor * taxaDecrescimo) / 100
    return  valor-percentual


def metade(valor):
    return valor/2


