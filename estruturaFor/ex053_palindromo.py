"""053- Crie um programa que leia uma frase
e diga se ela é um palindromo desconsiderando os espaços.
"""
frase=str(input('Escreva uma frase: ')).replace(" ","")
inverso=frase[::-1].replace(" ","")

if frase == inverso:
    print('A frase representa um palindromo')
else:
    print('A frase não representa um palindromo')