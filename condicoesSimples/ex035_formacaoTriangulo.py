"""035- Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem ou não formar um triangulo
"""
reta1=float(input('Escreva o comprimento da primeira reta: '))
reta2=float(input('Escreva o comprimento da segunda reta: '))
reta3=float(input('Escreva o comprimento da terceira reta: '))

if reta1+reta2 > reta3 and reta1+reta3 > reta2 and reta2+reta3 > reta1:
    print('\033[4;31mAs medidas informadas atendem as exigências para formação do triangulo')
else:
    print('\033[4;31mAs medidas informadas não atendem as exigências para formação do triangulo')