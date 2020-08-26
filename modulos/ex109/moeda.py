"""109- Modifique as funções que foram criadas
no desafio 107 para que eles aceitem um parametro
a mais , informando ser o valor retornado por eles vai
ser ou não formatado pela função moeda(), desenvolvida no
desafio 108."""


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
