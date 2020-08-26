"""083- Crie um programa onde o usuario digite uma
expressão qualquer que use parenteses. Seu aplicativo
 deverá analisar se a expressão passsada está com os
 parênteses abertos e fechados na ordem correta."""

expressao=str(input('Escreva uma expressão:'))
lista=[]
for simbolo in expressao:
    if simbolo =='(':
        lista.append('(')
    elif simbolo ==')':
        lista.pop()
if len(lista)==0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão é inválida!')