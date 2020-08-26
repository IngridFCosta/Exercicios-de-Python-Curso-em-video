"""112-Dentro do pacote utiliadadesCeV que criamos no
desafio 111, temos um módulo chamado dado. CRie uma função
chamada leiaDinheiro() que seja capaz de funcionar como a função
input(), mas como uma validação de dados oara aceitar apenas
valores monetários."""

def leiaDinheiro(msg):
    valido=False
    while not valido:
        entrada=str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada=='':
            print(f'\033[0;31mErro! {entrada} não é válido\033[m')
        else:
            valido=True
            return float(entrada)



