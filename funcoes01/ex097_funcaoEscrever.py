"""097- Faça um programa que tenha uma função
chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem  com tamanho
adaptável.
Ex: escreva('Olá, Mundo!')
saida:
       -----------
       Olá, Mundo!
       -----------
"""
def escreva(txt):
    print('-'*len(txt))
    print(txt)
    print('-' * len(txt))


escreva('I love Python!!!')