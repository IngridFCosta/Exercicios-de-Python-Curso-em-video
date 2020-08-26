"""104- Crie um programa que tenha a função
leiaint(), que vai funcionar de forma semelhante
à função input() do Python. Só que fazendo a
validação para aceitar apenas um valor númerico.
ex: n=leiaint('Digite um n ')
"""

def leiaint(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('\033[0;31mErro! Digite um número válido.\033[m')
        if ok:
            break
    return  valor



#programa principal
n= leiaint('Digite um numero:')
print(f'Você digitou o numero {n}')