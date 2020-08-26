"""
ex20- O mesmo professor do desafio anterior quer sortear  a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
"""
import random
aluno1=input('Escreva o nome do aluno:')
aluno2=input('Escreva o nome do  aluno:')
aluno3=input('Escreva o nome do aluno: ')
aluno4=input('Escreva o nome do aluno: ')

lista=[aluno1, aluno2,aluno3,aluno4]
random.shuffle(lista)
print('A ordem de apresentação é:{}'.format(lista))