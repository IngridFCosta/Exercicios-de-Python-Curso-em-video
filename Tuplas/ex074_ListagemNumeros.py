"""074-Crie um programa que vai gerar cinco
números aleatórios e colocar em uma tupla

Depois disso, mostre a listagem de numeros
gerados e também indique o menor e o maior
valor que estão na tupla
"""
import random
tuplaAleatorio=(random.randint(0,5),random.randint(0,5),random.randint(0,5),
                random.randint(0,5), random.randint(0,5))

print(tuplaAleatorio)
print(f'O maior é : {max(tuplaAleatorio)}')
print(f'O menor valor é: {min(tuplaAleatorio)}')

