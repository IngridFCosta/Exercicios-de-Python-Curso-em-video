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

def linha(tam=42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('Menu principal')
    c=1
    for item in lista:
        print(f'{c}-{item}')
        c+=1
    print(linha())
    opc=leiaint('Sua opção')
    return opc