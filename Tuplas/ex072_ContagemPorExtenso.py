"""072- Crie um programa que tenha uma tupla totalmente
preenchido com uma contagem por extenso, de zero até vinte.

Seu programa deverá  ler um numero pelo teclado( entre  0 e 20)
e mostrá-la por EXTENSO
"""
contagemExtenso=('Zero','Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito','Nove', 'Dez',
          'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
          'Dezenove', 'Vinte')
while True:
     numero=int(input('Escreva um número  entre 0 e 20 '))
     if 0 <= numero <=20:
         break
     print('Tente novamente.', end='')
print(f'Você digitou o numero {contagemExtenso[numero]}')
