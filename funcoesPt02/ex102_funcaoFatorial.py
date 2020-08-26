"""102- Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro que indique o número
a calcular e o outro chamado show, que será um valor lógico
(opcional) inidicando se será mostrado ou não na tela o
processo de cálculo fatorial."""

def fatorial(num, show=False):
    """
    Função que calcula o fatorial
    :param num: Numero a ser calculado
    :param show: Paramêtro opcional- Mostar ou não a fórmula
    :return: retorna o valor do fatorial de num
    """
    fat=1
    for cont in range(num, 0,-1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print('  = ', end='')
        fat *= cont
    return fat



print(fatorial(5, show=True))
help(fatorial)