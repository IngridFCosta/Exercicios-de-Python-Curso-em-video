# 04- Faça um programa  que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as infomações
#possiveis sobre ele

entrada=input("Digite algo:")
tipo=type(entrada)
print('O tipo primitivo é: {}'.format(tipo))
espaco=entrada.isspace()
print('Só tem espaço? {}'.format(espaco))
numerico=entrada.isalnum()
print('É numerico? {}'.format(numerico))
alfabetico= entrada.isalpha()
print('É alfabetico? {}'.format(alfabetico))
alfaNum=entrada.isalnum()
print('É alfanumérico?{}'.format(alfaNum))
maiusculo=entrada.isupper()
print('Está em maiúsculo? {}'.format(maiusculo))
minusculo=entrada.islower()
print('Está em minusculo? {}'.format(minusculo))
