""""090- Faça um programa que leia nome e média de uma aluno,
guardando também a situaçõa em um dicionario. No final, mostre
o conteúdo da estrutura na tela."""

dadosAluno={}

dadosAluno['Nome']=str(input('Escreva o nome: '))
dadosAluno['Média']=float(input('Escreva a média:'))

if dadosAluno['Média']>=7:
    dadosAluno['Situação']='Aprovado'
else:
    dadosAluno['Situação']='Reprovado'
print(dadosAluno)