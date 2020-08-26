"""049- Refaça o desafio 009, mostrando a tabuada de um numero
 escolhido pelo usuario , só que agora utilizando o laço for
"""
numero=int(input('\033[0;32mEscreva um numero qualquer para ser escrita a tabuada:\033[m '))
limiteTab=int(input('\033[0;32mEscreva o limite da sua tabuada:\033[m'))

for contador in range(1,limiteTab+1):
    print(numero, 'X', contador,'= ',numero*contador)
