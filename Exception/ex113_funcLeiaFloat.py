"""113- Reescreva a função leiaint() que fizemos no desafio 104,
incluindo agora a possibilidade de digitação de um número
de tipo inválido. Aproveite e crie a também uma função
leiafloat() com a mesa funcionalidade."""


def leiaint(msg):
    while True:
        try:
            num=int(input(msg))
        except (TypeError,ValueError):
            print('Erro! Por favor, digite um número válido!')
            continue
        except(KeyboardInterrupt):
            print('O usuário preferiu nao digitar um numero')
            return 0
        else:
            return  num


def leiafloat(msg):
    while True:
        try:
            num=float(input(msg))
        except(TypeError, ValueError):
            print('Erro! POr favor,digite um número válido')
            continue
        except(KeyboardInterrupt):
            print('O usuário preferiu nao digitar um numero')
            return 0
        else:
            return num



numero=leiaint('Digite um numero: ')
numFloat=leiafloat('Digite um numero:')
print(f'O numero inteiro digitado foi {numero} e o numero de ponto flutuante foi {numFloat}')

