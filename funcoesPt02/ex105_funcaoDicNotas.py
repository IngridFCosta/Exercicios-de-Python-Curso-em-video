"""105- Faça um programa que tenha uma função
notas() que pode receber várias notas de aluno
e vai retornar um dicionário com as seguintes
informações:
- Quantidade de notas
- A maior nota
- A menor nota
-A média da turma
- A situação (opcional)
Adicione também as docsstrings da função.
"""
notasAlunos={}

def notas(*notas,sit=False):
    """
    :param notas: Recebe uma quantidade indefinida de notas
    :param sit: Recebe um parâmetro opcional sobre a situação do aluno
    :return: Retorna os dados dentro de um dicionário com as informações do aluno
    """
    media=0
    soma=0
    for cont in notas:
        soma+=cont
    media=soma/len(notas)
    maior=max(notas)
    menor=min(notas)
    notasAlunos['Quantidade de notas']=len(notas)
    notasAlunos['Maior nota']=maior
    notasAlunos['Menor nota']=menor
    notasAlunos['Média'] = media
    if sit:
        if media >= 7:
           notasAlunos['Situação'] = 'Aprovado'
        elif media < 7 and media > 5:
           notasAlunos['Situação'] = 'Em recuperação'
        else:
           notasAlunos['Situação'] = 'Reprovado'

    return print(notasAlunos)



notas(3.0,3.0,6.0,10, sit=True)
help(notas)