"""
ex19- Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
"""
import random
aluno1=input('Escreva o primeiro nome: ')
aluno2=input('EScreva o segundo nome: ')
aluno3=input('Escreva o terceiro nome:')
aluno4=input('Escreva o quarto numero: ')

lista=[aluno1,aluno2, aluno3,aluno3,aluno4]
escolhido=random.choice(lista)
print('O aluno escolhido para apagar o quadro foi: {}'.format(escolhido))