"""037- Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal
"""
print('-'*30)
print('Bases de conversão')
print('-'*30)
print('[1]- Binário\n'
      '[2]-Octal\n'
      '[3]-Hexadecimal\n')
numero=int(input('Escreva um numero para ser convertido:  '))
base= int(input('Escreva a base de conversão como foi citado acima:'))

if base== 1:
  binario=bin(numero)
  print('O numero {} convertido para binário é igual a: {}'.format(numero, binario[2:]))
elif base ==2:
    octal=oct(numero)
    print('O numero {} convertido para octal é igual a: {}'.format(numero, octal[2:]))
elif base==3:
    hexadecimal=hex(numero)
    print('O numero {} convertido para hexadecimal é igual a: {}'.format(numero, hexadecimal[2:]))