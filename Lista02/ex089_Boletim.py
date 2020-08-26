"""089- Crie um programa que leia nome e duas notas
de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e
permita que  usuário possa mostrar as notas de cada aluno
individualmente."""

listaAluno=[]

while True:
    nome=str(input('Nome do aluno(a):'))
    nota1=float(input('Primeira nota: '))
    nota2=float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    listaAluno.append([nome, [nota1, nota2],media])

    continuar = ' '
    continuar = str(input('Deseja continuar? S/N ')).upper().strip()[0]
    while continuar not in 'SN':
        print('Você digitou um dado inválido. Tente novamente!')
        continuar = str(input('Deseja continuar? S/N')).upper().strip()[0]
    if continuar == 'N':
        break
print('-'*30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i, a in enumerate(listaAluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opcao= int(input('Mostrar notas de qual aluno? '))
    if opcao==999:
        print('Programa encerrado!')
        break
    if opcao <=len(listaAluno)-1:
        print(f'Notas de {listaAluno[opcao][0]} são {listaAluno[opcao][1]}')