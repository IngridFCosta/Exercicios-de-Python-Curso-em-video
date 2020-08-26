"""038- Escreva um programa que leia dois números inteiros e compare-os
mostrando na tela uma mensagem:
- O primeiro é o maior
- O segundo é o maior
- Não existe valor maior , os dois valores são iguais
"""
num1=int(input('Escreva o primeiro numero:'))
num2=int(input('Escreva o segundo numero: '))

if num1 > num2:
    print('O primeiro é o maior!')
elif num2 > num1:
    print('O segundo é o maior!')
else:
    print('Não existe valor maior, os dois valores são iguais!')