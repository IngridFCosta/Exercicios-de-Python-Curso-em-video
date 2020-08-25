"""022- Crie um programa que leia o nome
completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas e minusculas
-Quantas letras ao todo sem considerar espaços
-Quantas letras tem o primeiro nome"""

nome=str(input('Escreva seu nome completo: ')).strip()

print('Seu nome em letras maiusculas é: {}'.format(nome.upper()))
print('Seu nome em letras minusculas é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro tem {} letras'. format(nome.find(' ')))