"""077- Crie um programa que tenha uma tupla
com várias palavras (não usar acentos)

Depois disso, você deve mostrar, para
cada palavra, quais são suas vogais"""

palavras=('programaçao','e','a','profissao','do','futuro')

for palavra in palavras:
    print(f'\nA palavra {palavra.upper()} tem as vogais:',end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')